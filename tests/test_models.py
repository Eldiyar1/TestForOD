import pytest
from apps.inventory.models import Enterprise, Product
from apps.users.models import User


@pytest.mark.django_db
def test_enterprise_model():
    user = User.objects.create(username="testuser")
    enterprise = Enterprise.objects.create(
        name="Test Enterprise",
        description="Test Description",
        location="Test Location",
        work_hours="9-18",
        user=user
    )
    assert enterprise.name == "Test Enterprise"
    assert enterprise.description == "Test Description"
    assert enterprise.location == "Test Location"
    assert enterprise.work_hours == "9-18"


@pytest.mark.django_db
def test_product_model():
    user = User.objects.create(username="testuser")
    enterprise = Enterprise.objects.create(
        name="Test Enterprise",
        description="Test Description",
        location="Test Location",
        work_hours="9-18",
        user=user
    )
    product = Product.objects.create(
        title="Test Product",
        description="Test Description",
        price=10.0,
        quantity=100,
        enterprise=enterprise
    )
    assert product.title == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 10.00
    assert product.quantity == 100
    assert product.enterprise == enterprise
