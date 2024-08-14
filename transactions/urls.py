from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_transaction, name='create_transaction'),
    path('<int:pk>/', views.transaction_detail, name='transaction_detail'),
]
