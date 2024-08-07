from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    
    path('', views.view_cart, name='view-cart'),
    path('add/<int:pk>/', views.add_item, name='add-item'),
    path('remove/<int:pk>/', views.remove_item, name='remove-item'),
]