import pytest


not_found = "Resource not found"
not_auth = "Authentication credentials were not provided"

class TestAppAPI:

    @pytest.mark.django_db()
    def test_organizations_not_found(self, client, district):
        response = client.get(f"/api/organizations/{district.id}/")
        assert response.status_code != 404, not_found

    @pytest.mark.django_db()
    def test_organizations_not_auth(self, client, district):
        response = client.get(f"/api/organizations/{district.id}/")
        assert response.status_code != 401, not_auth


    @pytest.mark.django_db()
    def test_organization_filter_category(self, client, district, category, enterprise):
        response = client.get(f"/api/organizations/{district.id}/?product__category__name={category.name}")
        assert response.json()[0]["product"][0]["category"]["name"] == category.name, (
            f"Category name must be {category.name}"
        )

    @pytest.mark.django_db()
    def test_organization_search_product(self, client, district, product, enterprise):
        response = client.get(f"/api/organizations/{district.id}/?search={product.name}")
        assert response.json()[0]["product"][0]["name"] == product.name, f"Product name must be {product.name}"

    @pytest.mark.django_db()
    def test_organization_detail_not_auth(self, client, enterprise):
        response = client.get(f"/api/organization/{enterprise.id}")
        assert response.status_code != 401, not_auth

    @pytest.mark.django_db()
    def test_organization_detail_not_found(self, client, enterprise):
        response = client.get(f"/api/organization/{enterprise.id}")
        assert response.status_code != 404, not_found

    @pytest.mark.django_db()
    def test_organization_detail(self, client, enterprise):
        response = client.get(f"/api/organization/{enterprise.id}")
        assert response.json()["id"] == enterprise.id, f"Enterprise id must be {enterprise.id}"

    @pytest.mark.django_db()
    def test_add_product_not_auth(self, client):
        data = {"category": {"name": "test category"}, "name": "test product"}
        response = client.post("/api/products/", data, format="json")
        assert response.status_code != 401, not_auth

    @pytest.mark.django_db()
    def test_add_product_not_found(self, client):
        data = {"category": {"name": "test category"}, "name": "test product"}
        response = client.post("/api/products/", data, format="json")
        assert response.status_code != 404, not_found

    @pytest.mark.django_db()
    def test_add_product(self, client):
        product = {"category": {"name": "test category"}, "name": "test product"}
        response = client.post("/api/products/", product, format="json")
        new_product = response.json()
        assert product["name"] == new_product["name"], f"Product name must be {new_product['name']}"
        assert product["category"]["name"] == new_product["category"]["name"], (
            f"Product name must be {new_product['category']['name']}"
        )

    @pytest.mark.django_db()
    def test_product_detail(self, client, product):
        response = client.get(f"/api/products/{product.id}/")
        assert response.status_code == 200, f"Response code must be 200"
        assert response.json()["name"] == product.name, f"Product name must be {product.name}"
