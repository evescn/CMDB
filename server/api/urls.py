from django.urls import path, re_path
from api import views

urlpatterns = [
    re_path('^asset/', views.aseet)
]