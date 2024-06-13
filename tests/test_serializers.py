import pytest
from decimal import Decimal
from apps.inventory.models import Enterprise
from apps.inventory.serializers import EnterpriseSerializer, ProductSerializer
from apps.users.models import User
from apps.inventory.models import Product


@pytest.mark.django_db
def test_enterprise_serializer():
    data = {
        "name": "Test Enterprise",
        "description": "Test Description",
        "location": "Test Location",
        "work_hours": "9-18"
    }
    serializer = EnterpriseSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data["name"] == "Test Enterprise"
    assert serializer.validated_data["description"] == "Test Description"
    assert serializer.validated_data["location"] == "Test Location"
    assert serializer.validated_data["work_hours"] == "9-18"


@pytest.mark.django_db
def test_product_serializer():
    user = User.objects.create(username="testuser")

    enterprise = Enterprise.objects.create(
        name="Test Enterprise",
        description="Test Description",
        location="Test Location",
        work_hours="9-18",
        user=user
    )

    data = {
        "title": "Test Product",
        "description": "Test Description",
        "price": Decimal("10.00"),
        "quantity": 100,
        "enterprise": enterprise.id
    }
    serializer = ProductSerializer(data=data)
    assert serializer.is_valid()
    serializer.save()
    product = Product.objects.get(id=serializer.data['id'])
    assert product.title == "Test Product"
    assert product.description == "Test Description"
    assert product.price == Decimal("10.00")
    assert product.quantity == 100
    assert product.enterprise == enterprise
