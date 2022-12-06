from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# @csrf_exempt
# def asset(request):
#     # print(request.POST)
#     data = json.loads(request.body.decode('utf-8'))
#     print(data, type(data))
#     return JsonResponse({'status': '200'})


from django.views import View
from django.utils.decorators import method_decorator

# @method_decorator(csrf_exempt, name='dispatch')
# class Asset(View):
#
#     # def get(self, request):
#     #     data = json.loads(self.request.body.decode('utf-8'))
#     #     print(data, type(data))
#     #     return JsonResponse({'status': '200'})
#
#     def post(self, request):
#         print(request.POST)
#         data = json.loads(self.request.body.decode('utf-8'))
#         print(data, type(data))
#         return JsonResponse({'status': '200'})


# rest_ful 接口风格
from rest_framework.views import APIView
from rest_framework.response import Response
from repository import models
import datetime
from django.db.models import Q


class Asset(APIView):

    def get(self, request):
        now = datetime.datetime.now()
        host_list = models.Server.objects.filter(Q(latest_date__lt=now) | Q(latest_date__isnull=True)).values(
            'hostname')
        # print(host_list)
        return Response(host_list)

    def post(self, request):
        info = request.data
        action = info['action']
        hostname = info['basic']['data']['hostname']

        if action == 'update':
            # 只更新硬件信息
            print('只更新硬件信息')
            # print(info)

            # 更新 主板 + cpu + 基本信息 （这类信息只有1条数据）
            server_list = models.Server.objects.filter(hostname=hostname)
            # now = datetime.datetime.now()
            server_list.update(
                **info['basic']['data'],
                **info['cpu']['data'],
                **info['main_board']['data'],
                # latest_date=now,
            )

            from api.service import process_memory, process_disk, process_nic
            # 更新内存
            process_memory(info, server_list)
            # 更新磁盘
            process_disk(info, server_list)
            # 更新网卡
            process_nic(info, server_list)

        else:
            print('更新硬件信息+主机名')

            # 获取老的主机名
            cert = info['cert']

            # 更新 主板 + cpu + 基本信息 （这类信息只有1条数据）
            # 此处也更新了更新主机名 info['basic']['data'] 中存放了新的主机名
            server_list = models.Server.objects.filter(hostname=cert)
            # now = datetime.datetime.now()
            server_list.update(
                **info['basic']['data'],
                **info['cpu']['data'],
                **info['main_board']['data'],
                # latest_date=now,
            )

            # 更新主机名，所以此处需要重新获取下 server_list 信息
            server_list = models.Server.objects.filter(hostname=hostname)
            from api.service import process_memory, process_disk, process_nic
            # 更新内存
            process_memory(info, server_list)
            # 更新磁盘
            process_disk(info, server_list)
            # 更新网卡
            process_nic(info, server_list)

        return Response({'status': '200'})
