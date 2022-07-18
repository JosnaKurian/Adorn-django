from django.urls import path
from .import views

urlpatterns = [
    path('',views.wish_list,name ='wish_list'),
    path('add_to_wishlist/<int:id>/',views.add_to_wishlist,name ='add_to_wishlist'),
    path('remove_wishlist/<int:id>/',views.remove_wishlist,name ='remove_wishlist'),

]