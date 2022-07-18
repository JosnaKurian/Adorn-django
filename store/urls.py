from django.urls import path
from .import views

urlpatterns = [
    path('all_products',views.all_products,name ='all_products'),
    path('category/<slug:category_slug>/',views.shop, name ='products_by_category'),
    path('category/<slug:category_slug>/<slug:sub_category_slug>/',views.shop,name = 'products_by_sub_category'),
    path('category/<slug:category_slug>/<slug:sub_category_slug>/<slug:product_slug>/',views.product_detail,name = 'product_detail'),
    path('search/',views.search,name ='search'),
    path('submit_review/<int:product_id>/',views.submit_review,name ='submit_review'),
    
]