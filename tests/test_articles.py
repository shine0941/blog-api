import pytest
from blog.models import Article

@pytest.mark.django_db
def test_author_can_edit(auth_client, article):
    payload = {"title": "Updated by author"}
    response = auth_client.patch(f"/api/articles/{article.id}/", payload)
    assert response.status_code == 200
    assert response.data["title"] == "Updated by author"

@pytest.mark.django_db
def test_non_author_cannot_edit(auth_client_other, article):
    payload = {"title": "Hacked!"}
    response = auth_client_other.patch(f"/api/articles/{article.id}/", payload)
    assert response.status_code == 403

@pytest.mark.django_db
def test_anonymous_can_view(api_client, article):
    response = api_client.get(f"/api/articles/{article.id}/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_anonymous_cannot_create(api_client, category):
    payload = {
        "title": "Unauthorized post",
        "content": "Hack?",
        "category_id": category.id,
        "tag_ids": [],
    }
    response = api_client.post("/api/articles/", payload)
    assert response.status_code == 401  # 未登入
