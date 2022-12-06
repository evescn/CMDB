from django.urls import path, re_path
from api import views

urlpatterns = [
    # re_path('^asset/', views.asset)
    re_path('^asset/', views.Asset.as_view())
]