from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view()),
    path('products/info/', views.product_info),
    path('products/<int:pk>', views.ProductDetailAPIView.as_view()),
    path('orders/', views.OrderListAPIView.as_view()),    
]

# urlpatterns = [
#     path('products/', views.product_list),
#     path('products/info/', views.product_info),
#     path('products/<int:pk>', views.product_detail),
#     path('orders/', views.order_list),    
# ]
