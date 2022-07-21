from django.urls import path
from .import views

urlpatterns = [
    path('',views.admin_login,name ='admin_login'),
    path('dashboard/',views.dashboard,name ='dashboard'),

    path('categories/',views.categories,name ='categories'),
    path('categories/add_categories/',views.add_categories,name ='add_categories'),
    path('categories/edit_categories/<str:slug>/',views.edit_categories,name ='edit_categories'),
    path('categories/delete_categories/<int:id>/',views.delete_categories,name ='delete_categories'),

    path('sub_categories/',views.sub_categories,name ='sub_categories'),
    path('sub_categories/add_subcategories/',views.add_subcategories,name ='add_subcategories'),
    path('sub_categories/edit_subcategories/<str:slug>/',views.edit_subcategories,name ='edit_subcategories'),
    path('sub_categories/delete_subcategories/<int:id>/',views.delete_subcategories,name ='delete_subcategories'),

    path('products/',views.products,name ='products'),
    path('products/add_products/',views.add_products,name ='add_products'),
    path('products/edit_products/<str:slug>/',views.edit_products,name ='edit_products'),
    path('products/delete_products/<int:id>/',views.delete_products,name ='delete_products'),

    path('customers/',views.customers,name ='customers'),
    path('customers/block_user/<int:id>/',views.block_user,name ='block_user'),

    path('orders/',views.orders,name ='orders'),
    path('orders/update_orders/<int:id>/',views.update_orders,name ='update_orders'),
    path('orders/order_details/<int:order_id>/',views.order_details,name ='order_details'),

    path('payments/',views.payments,name ='payments'),

    path('Review_Rating/',views.Review_Rating,name ='Review_Rating'),
    path('Review_Rating/delete_Review_Rating/<int:id>/',views.delete_Review_Rating,name ='delete_Review_Rating'),
  

]