from repository import models


def process_memory(info, server_list):
    # 更新内存
    # ## 提交的内存信息
    memory_info = info['memory']['data']

    # ##数据库内存信息
    server_obj = server_list.first()
    memory_db_info = server_obj.memory_list.all().values('slot')

    memory_slot_set = set(memory_info)
    db_slot_set = {i['slot'] for i in memory_db_info}

    # ##新增，更新，删除 内存信息
    add_slot_set = memory_slot_set - db_slot_set
    update_slot_set = memory_slot_set & db_slot_set
    delete_slot_set = db_slot_set - memory_slot_set

    if add_slot_set:
        memory_obj_list = []
        record_obj_list = []
        # for slot, data in memory_info.items():
        #     if slot in add_slot_set:
        #         memory_obj_list.append(models.Memory(**data, server=server_obj))
        #         # models.Memory.objects.create(**data, server=server_obj)
        for slot in add_slot_set:
            data = memory_info[slot]
            # print(data)

            memory_obj_list.append(models.Memory(**data, server=server_obj))

            """
            槽位 1，2，3 新增了一块内存，具体信息如下：
            """
            msg_list = []
            for name, value in data.items():
                verbose_name = models.Memory._meta.get_field(name).verbose_name
                msg_list.append('{} : {}'.format(verbose_name, value))

            # print(msg_list)
            record_obj_list.append(
                models.AssetRecord(
                    server=server_obj, content="槽位 {} 新增了一块内存，具体信息如下：{}".format(
                        slot, ", ".join(msg_list)
                    )
                )
            )

        if memory_obj_list:
            """
            槽位 1，2，3 新增了一块内存
            """
            models.AssetRecord.objects.bulk_create(record_obj_list, batch_size=64)

            models.Memory.objects.bulk_create(memory_obj_list, batch_size=64)

    if update_slot_set:
        record_obj_list = []
        # for slot, data in memory_info.items():
        #     if slot in update_slot_set:
        #         models.Memory.objects.create(**data, server=server_obj)
        for slot in update_slot_set:
            data = memory_info[slot]

            """
            槽位 1，2，3 内存信息更新了，判断数据是否更新
            """
            update_dict = {}

            msg_list = []
            obj = models.Memory.objects.get(server=server_obj, slot=slot)
            for name, value in data.items():
                old = getattr(obj, name)
                if value == old:
                    continue
                # print(name, value, old)
                verbose_name = models.Memory._meta.get_field(name).verbose_name

                update_dict[name] = value

                msg_list.append('{}：老数据 {}、新数据 {}'.format(verbose_name, old, value))

            if msg_list:
                models.Memory.objects.filter(slot=slot, server=server_obj).update(**update_dict)

                record_obj_list.append(
                    models.AssetRecord(
                        server=server_obj, content='槽位 {} 内存信息更新了，{}'.format(
                            # slot, msg_list
                            slot, ", ".join(msg_list)
                        )
                    )
                )

        if record_obj_list:
            models.AssetRecord.objects.bulk_create(record_obj_list, batch_size=64)

    if delete_slot_set:
        """
        槽位 1，2，3 的内存被移除
        """
        models.AssetRecord.objects.create(server=server_obj, content='槽位 {} 的内存被移除'.format(', '.join(delete_slot_set)))

        models.Memory.objects.filter(slot__in=delete_slot_set, server=server_obj).delete()


def process_disk(info, server_list):
    # 更新磁盘
    # ##提交的磁盘信息
    disk_info = info['disk']['data']

    # ##数据库磁盘信息
    server_obj = server_list.first()
    disk_db_info = server_obj.disk_list.all().values('slot')

    disk_slot_set = set(disk_info)
    db_slot_set = {i['slot'] for i in disk_db_info}

    # ##新增，更新，删除 磁盘信息
    add_slot_set = disk_slot_set - db_slot_set
    update_slot_set = disk_slot_set & db_slot_set
    delete_slot_set = db_slot_set - disk_slot_set

    if add_slot_set:
        disk_obj_list = []
        # for slot, data in disk_info.items():
        #     if slot in add_slot_set:
        #         disk_obj_list.append(models.Disk(**data, server=server_obj))
        #         # models.Disk.objects.create(**data, server=server_obj)
        for slot in add_slot_set:
            data = disk_info[slot]
            disk_obj_list.append(models.Disk(**data, server=server_obj))

        if disk_obj_list:
            models.Disk.objects.bulk_create(disk_obj_list, batch_size=64)

    if update_slot_set:
        # for slot, data in disk_info.items():
        #     if slot in update_slot_set:
        #         models.Disk.objects.create(**data, server=server_obj)
        for slot in update_slot_set:
            data = disk_info[slot]
            models.Disk.objects.filter(slot=slot, server=server_obj).update(**data)

    if delete_slot_set:
        models.Disk.objects.filter(slot__in=delete_slot_set, server=server_obj).delete()


def process_nic(info, server_list):
    # 更新网卡
    # ##提交的网卡信息
    nic_info = info['nic']['data']

    # ##数据库网卡信息
    server_obj = server_list.first()
    nic_db_info = server_obj.nic_list.all().values('name')

    nic_name_set = set(nic_info)
    db_name_set = {i['name'] for i in nic_db_info}

    # ##新增，更新，删除 网卡信息
    add_name_set = nic_name_set - db_name_set
    update_name_set = nic_name_set & db_name_set
    delete_name_set = db_name_set - nic_name_set

    if add_name_set:
        nic_obj_list = []
        # for name, data in nic_info.items():
        #     if name in add_name_set:
        #         nic_obj_list.append(models.NIC(**data, server=server_obj))
        #         # models.NIC.objects.create(**data, server=server_obj)
        for name in add_name_set:
            data = nic_info[name]
            data['name'] = name
            nic_obj_list.append(models.NIC(**data, server=server_obj))

        if nic_obj_list:
            models.NIC.objects.bulk_create(nic_obj_list, batch_size=64)

    if update_name_set:
        # for name, data in nic_info.items():
        #     if name in update_name_set:
        #         models.NIC.objects.create(**data, server=server_obj)
        for name in update_name_set:
            data = nic_info[name]
            data['name'] = name
            models.NIC.objects.filter(name=name, server=server_obj).update(**data)

    if delete_name_set:
        models.NIC.objects.filter(name__in=delete_name_set, server=server_obj).delete()
