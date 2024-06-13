from rest_framework import serializers
from .models import Enterprise, Product


class EnterpriseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Enterprise
        fields = (
            'id',
            'name',
            'description',
            'location',
            'work_hours',
            'user',
        )


class ProductSerializer(serializers.ModelSerializer):
    enterprise = serializers.PrimaryKeyRelatedField(queryset=Enterprise.objects.all())

    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'description',
            'price',
            'quantity',
            'enterprise',
        )
        read_only_fields = ('enterprise',)
