from django.test import TestCase

# Create your tests here.
import pytest
from django.test import RequestFactory
from django.urls import reverse
from .models import Articles
from .views import post_list, post_create, post_update, post_delete, post_detail
from .forms import ArticlesForm

@pytest.fixture
def create_article():
    return Articles.objects.create(
        title='Test Title',
        content='Test Content',
        # Add other required fields as needed
    )

@pytest.mark.django_db
def test_post_list_view():
    request = RequestFactory().get(reverse('feeds:post_list'))
    response = post_list(request)
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_create_view():
    request = RequestFactory().post(reverse('feeds:post_create'))
    request.user = User.objects.create(username='testuser', is_staff=True)  # Create a staff user
    response = post_create(request)
    assert response.status_code == 302  # Check for a redirect after successful form submission

@pytest.mark.django_db
def test_post_update_view(create_article):
    request = RequestFactory().post(reverse('feeds:post_update', args=[create_article.id]))
    request.user = User.objects.create(username='testuser', is_staff=True)  # Create a staff user
    response = post_update(request, create_article.id)
    assert response.status_code == 302  # Check for a redirect after successful form submission

@pytest.mark.django_db
def test_post_delete_view(create_article):
    request = RequestFactory().post(reverse('feeds:post_delete', args=[create_article.id]))
    request.user = User.objects.create(username='testuser', is_staff=True)  # Create a staff user
    response = post_delete(request, create_article.id)
    assert response.status_code == 302  # Check for a redirect after successful form submission

@pytest.mark.django_db
def test_post_detail_view(create_article):
    request = RequestFactory().get(reverse('feeds:post_detail', args=[create_article.id]))
    request.user = User.objects.create(username='testuser', is_staff=True)  # Create a staff user
    response = post_detail(request, create_article.id)
    assert response.status_code == 200