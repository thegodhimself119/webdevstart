from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),

    path('action_page.php/', views.action_page),
    path('test/', views.test),
    path('temp/', views.index)
]