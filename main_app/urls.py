from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assets/', views.assets_index, name='assets_index'),
    
]