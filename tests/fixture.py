import pytest


@pytest.fixture
def user():
    from django.contrib.auth.models import User
    return User.objects.create(email="some@any.com", password="123456")


@pytest.fixture
def token(user):
    from rest_framework.authtoken.models import Token
    token, _ = Token.objects.get_or_create(user=user)

    return token.key

@pytest.fixture
def client(token):
    from rest_framework.test import APIClient
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {token}')

    return client

@pytest.fixture
def category():
    from app.models import Category

    return Category.objects.create(name="Категория")


@pytest.fixture
def product(category):
    from app.models import Product

    return Product.objects.create(name="Продукт", category=category)

@pytest.fixture
def district():
    from app.models import District

    return District.objects.create(name="Район")

@pytest.fixture
def network():
    from app.models import NetworkEnterprise

    return NetworkEnterprise.objects.create(name="Сеть")

@pytest.fixture
def price(product):
    from app.models import ProductPrice

    return ProductPrice.objects.create(product=product, price=100)

@pytest.fixture
def enterprise(network, district, product):
    from app.models import Enterprise
    ent = Enterprise.objects.create(
        name="Организация",
        network=network,
    )
    ent.district.add(district)
    ent.product.add(product)

    return ent