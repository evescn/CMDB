from django.urls import path, re_path
from web import views

urlpatterns = [
    re_path(r'^server/list/', views.server, name='server'),
    re_path(r'^server/add/', views.server_add, name='server_add'),
    re_path(r'^server/edit/(\d+)/', views.server_edit, name='server_edit'),
]
