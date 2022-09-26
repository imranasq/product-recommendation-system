import pytest
from django.urls import resolve, reverse

pytestmark = pytest.mark.django_db


def test_product_list_url():
    assert reverse("products-list") == "/products/"
    assert resolve("/products/").view_name == "products-list"


def test_product_detail_url(product):
    assert reverse("products-detail", kwargs={"pk": product.id}) == f"/products/{product.id}/"
    assert resolve(f"/products/{product.id}/").view_name == "products-detail"


def test_product_update_status_url(product):
    assert reverse("products-update-status", kwargs={"pk": product.id}) == f"/products/{product.id}/update-status/"
    assert resolve(f"/products/{product.id}/update-status/").view_name == "products-update-status"


def test_product_type_list_url():
    assert reverse("product_types-list") == "/product-types/"
    assert resolve("/product-types/").view_name == "product_types-list"


def test_product_type_detail_url(product_type):
    assert reverse("product_types-detail", kwargs={"pk": product_type.id}) == f"/product-types/{product_type.id}/"
    assert resolve(f"/product-types/{product_type.id}/").view_name == "product_types-detail"


def test_product_type_update_status_url(product_type):
    assert reverse("product_types-update-status",
                   kwargs={"pk": product_type.id}) == f"/product-types/{product_type.id}/update-status/"
    assert resolve(f"/product-types/{product_type.id}/update-status/").view_name == "product_types-update-status"


def test_customer_product_type_list_url():
    assert reverse("customer_products") == "/customer/products/"
    assert resolve("/customer/products/").view_name == "customer_products"
