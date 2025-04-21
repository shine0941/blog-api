import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from blog.models import Category, Tag, Article

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='testpass')

@pytest.fixture
def auth_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def category(db):
    return Category.objects.create(name='Tech')

@pytest.fixture
def tag(db):
    return Tag.objects.create(name='Django')

@pytest.fixture
def article(user, category):
    article = Article.objects.create(
        title='Test Article',
        content='Some content',
        category=category,
        author=user
    )
    return article

@pytest.fixture
def another_user(db):
    return User.objects.create_user(username='otheruser', password='pass123')

@pytest.fixture
def auth_client_other(another_user):
    client = APIClient()
    client.force_authenticate(user=another_user)
    return client
