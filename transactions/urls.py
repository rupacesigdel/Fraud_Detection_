from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL pattern
    path('transactions/', views.transaction_list, name='transaction_list'),  # Transaction list
    path('transactions/create/', views.create_transaction, name='create_transaction'),  # Create transaction
    path('transactions/<int:pk>/', views.transaction_detail, name='transaction_detail'),  # Transaction detail
    path('transactions/<int:pk>/predict/', views.predict_fraud, name='predict_fraud'),  # Fraud prediction
]
