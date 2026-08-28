import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_dashboard_view(client):
    url = reverse('dashboard')
    response = client.get(url)
    # the dashboard redirects to login if not authenticated
    assert response.status_code in [200, 302]

def test_math():
    assert 1 + 1 == 2
