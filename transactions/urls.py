from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_list, name='transaction_list'),  # Make sure there's a URL pattern for the root
    path('', views.home, name='home'),
    path('create/', views.create_transaction, name='create_transaction'),
    path('<int:pk>/', views.transaction_detail, name='transaction_detail'),
    path('<int:pk>/predict/', views.predict_fraud, name='predict_fraud'),
]
