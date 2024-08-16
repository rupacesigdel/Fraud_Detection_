from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('transactions/', views.transaction_list, name='transaction_list'),
    path('transactions/statistics/', views.statistics_view, name='statistics_view'),
    path('transactions/create/', views.create_transaction, name='create_transaction'),
    path('transactions/<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('transactions/<int:pk>/predict/', views.predict_fraud, name='predict_fraud'),
]
