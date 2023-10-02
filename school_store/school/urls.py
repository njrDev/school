from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/',views.add_product,name='form'),
    path('get_subcategories/<int:category_id>/',views.get_subcategories,name='get_subcategories'),
    path('confirm', views.confirm, name='confirm'),
]
