from django.urls import path
from . import views

urlpatterns = [
    path ("", views.home, name='market-home'),
    path ("about/", views.about, name='market-about'),
    path ("product/", views.product, name='market-product'),
    path("product/<int:product_id>/", views.product, name='product'),
]