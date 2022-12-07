from django.urls import path, re_path
from web import views

urlpatterns = [
    re_path(r'^business_unit/list/', views.business_unit, name='business_unit'),
    re_path(r'^business_unit/add/', views.business_unit_change, name='business_unit_add'),
    re_path(r'^business_unit/edit/(\d+)/', views.business_unit_change, name='business_unit_edit'),

    re_path(r'^server/list/', views.server, name='server'),
    re_path(r'^server/add/', views.server_add, name='server_add'),
    re_path(r'^server/edit/(\d+)/', views.server_edit, name='server_edit'),
    re_path(r'^server/detail/(\d+)/', views.server_detail, name='server_detail'),
    re_path(r'^server/record/(\d+)/', views.server_record, name='server_record'),
]
