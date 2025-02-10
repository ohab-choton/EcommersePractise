from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homePage'),
    path('category-list/',views.category_list,name='category_listPage'),
    path('brand/',views.brand_list,name='brand_listPage'),
    path('product/',views.product_list,name='product_listPage'),
    path('category-product-list/<int:cat_id>/',views.category_product_list,name='category_product_listPage'),
    path('brand-product-list/<int:brand_id>/',views.brand_product_list,name='brand_product_listPage'),
    path('product-detail/<str:slug>/<int:id>/',views.product_detail,name='product_detailPage'),
    path('search/',views.search,name='searchPage'),
    path('filter-data/',views.filter_data,name='filter-data'),


]