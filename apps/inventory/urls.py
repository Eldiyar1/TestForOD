from django.urls import path
from .views import EnterpriseListCreate, EnterpriseRetrieveUpdateDestroy, ProductListCreate, \
    ProductRetrieveUpdateDestroy

urlpatterns = [
    path('enterprises/', EnterpriseListCreate.as_view(), name='enterprise-list-create'),
    path('enterprises/<int:pk>/', EnterpriseRetrieveUpdateDestroy.as_view(), name='enterprise-retrieve-update-destroy'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
]
