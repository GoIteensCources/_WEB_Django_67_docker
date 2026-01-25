from django.urls import path
from . import views

app_name = "order"

urlpatterns = [
    path('', views.order_view, name='order_form'),
    path('thanks/', views.order_thanks, name='order_thanks'),
]
