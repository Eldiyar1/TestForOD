from rest_framework import generics, permissions
from django.db.models import Count
from .models import Enterprise, Product
from .serializers import EnterpriseSerializer, ProductSerializer
from .permissions import IsOwnerOrReadOnly


class EnterpriseListCreate(generics.ListCreateAPIView):
    queryset = Enterprise.objects.select_related('user').all()
    serializer_class = EnterpriseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EnterpriseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    permission_classes = [IsOwnerOrReadOnly]


class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        enterprise = Enterprise.objects.get(user=self.request.user)
        serializer.save(enterprise=enterprise)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)

        total_products = Product.objects.aggregate(total=Count('id'))['total']
        response.data['total_products'] = total_products

        return response


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
