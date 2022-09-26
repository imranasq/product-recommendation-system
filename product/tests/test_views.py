import pytest
from rest_framework.reverse import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestProductViewSet:
    payload = {
        "title": "random data",
        "description": "random string",
        "price": 1234,
        "quantity": 50
    }

    def test_get_products_with_unauthentic_client(self, client):
        url = reverse("products-list")
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() is not None

    def test_get_products_with_authentic_client(self, auth_client):
        url = reverse("products-list")
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None

    def test_create_products_with_unauthentic_client(self, client):
        payload = self.payload
        url = reverse("products-list")
        response = client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() is not None

    def test_create_products_with_authentic_client(self, auth_client):
        payload = self.payload
        url = reverse("products-list")
        response = auth_client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() is not None

    def test_create_products_with_vendor_client(self, vendor_client):
        payload = self.payload
        url = reverse("products-list")
        response = vendor_client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() is not None

    def test_create_products_with_no_payload(self, vendor_client):
        url = reverse("products-list")
        response = vendor_client.post(url, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() is not None

    def test_update_products_with_vendor_client(self, vendor_client, product):
        payload = self.payload
        url = reverse("products-detail", kwargs={"pk": product.id})
        response = vendor_client.put(url, data=payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None

    def test_partial_update_products_with_vendor_client(self, vendor_client, product):
        payload = {
            "title": product.title,
            "price": 10
        }
        url = reverse("products-detail", kwargs={"pk": product.id})
        response = vendor_client.patch(url, data=payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None

    def test_partial_update_products_with_admin_client(self, admin_client, product):
        payload = {
            "title": product.title,
            "price": 10
        }
        url = reverse("products-detail", kwargs={"pk": product.id})
        response = admin_client.patch(url, data=payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None

    def test_delete_products_with_vendor_client(self, vendor_client, product):
        url = reverse("products-detail", kwargs={"pk": product.id})
        response = vendor_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_delete_products_with_admin_client(self, admin_client, product):
        url = reverse("products-detail", kwargs={"pk": product.id})
        response = admin_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestProductTypeViewSet:
    payload = {
        "name": "random data"
    }

    def test_get_product_types_with_unauthentic_client(self, client):
        url = reverse("product_types-list")
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() is not None

    def test_get_product_types_with_authentic_client(self, auth_client):
        url = reverse("product_types-list")
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None

    def test_create_product_types_with_unauthentic_client(self, client):
        payload = self.payload
        url = reverse("product_types-list")
        response = client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() is not None

    def test_create_product_types_with_authentic_client(self, auth_client):
        payload = self.payload
        url = reverse("product_types-list")
        response = auth_client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() is not None

    def test_create_product_types_with_admin_client(self, admin_client):
        payload = self.payload
        url = reverse("product_types-list")
        response = admin_client.post(url, data=payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() is not None

    def test_create_product_types_with_no_payload(self, admin_client):
        url = reverse("product_types-list")
        response = admin_client.post(url, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.json() is not None

    def test_update_product_types_with_admin_client(self, admin_client, product_type):
        payload = self.payload
        url = reverse("product_types-detail", kwargs={"pk": product_type.id})
        response = admin_client.put(url, data=payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] is not payload['name']

    def test_partial_update_product_types_with_admin_client(self, admin_client, product_type):
        payload = {
            "name": "new data"
        }
        url = reverse("product_types-detail", kwargs={"pk": product_type.id})
        response = admin_client.patch(url, data=payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] is not payload['name']

    def test_delete_product_types_with_admin_client(self, admin_client, product_type):
        url = reverse("product_types-detail", kwargs={"pk": product_type.id})
        response = admin_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestCustomerProductAPIViewSet:
    def test_get_customer_products_with_unauthentic_client(self, client):
        url = reverse("customer_products")
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.json() is not None

    def test_get_customer_products_with_authentic_client(self, auth_client):
        url = reverse("customer_products")
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() is not None

    def test_not_allowed_method_does_not_work_in_customer_product_api(self, auth_client):
        url = reverse("customer_products")
        get_response = auth_client.post(url)
        assert get_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert get_response.json() is not None

        put_response = auth_client.put(url)
        assert put_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert put_response.json() is not None

        patch_response = auth_client.patch(url)
        assert patch_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert patch_response.json() is not None

        delete_response = auth_client.delete(url)
        assert delete_response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert delete_response.json() is not None
