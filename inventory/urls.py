from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('sales-report/', views.sales_report, name='sales_report'),
]