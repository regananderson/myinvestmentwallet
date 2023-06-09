from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assets/', views.assets_index, name='assets_index'),
    path('all/', views.assets_detail, name='assets_detail'),
    path('assets/<str:asset_type>/', views.asset_type, name='asset_type'),
    path('investments/<int:asset_id>/', views.investments_detail, name='investments_detail'),
    path('investments/create/', views.AssetCreate.as_view(), name='asset_create'),
    path('investments/<int:pk>/update', views.AssetUpdate.as_view(), name='asset_update'),
    path('investments/<int:pk>/delete', views.AssetDelete.as_view(), name='asset_delete'),
    path('acccounts/signup/', views.signup, name='signup')
]