from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.inventory.models import Enterprise, Product
from apps.users.models import User


class EnterpriseViewTests(APITestCase):
    def setUp(self):
        # Create a sample user
        self.user = User.objects.create(username="testuser")

        # Create a sample enterprise for testing
        self.enterprise = Enterprise.objects.create(
            name="Test Enterprise",
            description="A test enterprise",
            location="Test Location",
            work_hours="9-18",
            user=self.user
        )

        # Authenticate the client
        self.client.force_authenticate(user=self.user)

    def test_enterprise_list_create(self):
        # Test the enterprise list endpoint
        url = reverse('enterprise-list-create')
        data = {
            "name": "New Enterprise",
            "description": "New Description",
            "location": "New Location",
            "work_hours": "8-17"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_enterprise_retrieve_update_destroy(self):
        # Retrieve an enterprise
        url = reverse('enterprise-retrieve-update-destroy', args=[self.enterprise.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update the enterprise
        data = {
            "name": "Updated Enterprise",
            "description": "Updated Description",
            "location": "Updated Location",
            "work_hours": "10-19"
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete the enterprise
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ProductViewTests(APITestCase):
    def setUp(self):
        # Create a sample user
        self.user = User.objects.create(username="testuser")

        # Create a sample enterprise for testing
        self.enterprise = Enterprise.objects.create(
            name="Test Enterprise",
            description="A test enterprise",
            location="Test Location",
            work_hours="9-18",
            user=self.user
        )

        # Create a sample product for testing
        self.product = Product.objects.create(
            title="Test Product",
            description="A test product",
            price="10.00",
            quantity=100,
            enterprise=self.enterprise
        )

        # Authenticate the client
        self.client.force_authenticate(user=self.user)

    def test_product_list_create(self):
        # Test the product list endpoint
        url = reverse('product-list-create')
        data = {
            "title": "New Product",
            "description": "New Product Description",
            "price": "15.00",
            "quantity": 50,
            "enterprise": self.enterprise.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_product_retrieve_update_destroy(self):
        # Retrieve a product
        url = reverse('product-retrieve-update-destroy', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update the product
        data = {
            "title": "Updated Product",
            "description": "Updated Product Description",
            "price": "20.00",
            "quantity": 150,
            "enterprise": self.enterprise.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete the product
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
