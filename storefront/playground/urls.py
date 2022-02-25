from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('temp/action_page/', views.action_page),
    path('test/action_page/',views.action_page),
    path('test/', views.test),
    path('temp/', views.newtest),
    path('test/register', views.register),
]
