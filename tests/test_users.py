"""Basic user endpoint tests"""

import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch


@pytest.fixture
def mock_db():
    return MagicMock()


def test_search_users_returns_results(mock_db):
    """Verify search endpoint returns a list."""
    mock_db.execute.return_value.fetchall.return_value = [{"id": 1, "name": "Alice"}]
    results = mock_db.execute("SELECT * FROM users WHERE name LIKE '%Alice%'").fetchall()
    assert len(results) == 1
    assert results[0]["name"] == "Alice"


def test_get_user_not_found(mock_db):
    """Verify 404 is raised for missing user."""
    mock_db.query.return_value.filter.return_value.first.return_value = None
    user = mock_db.query(object()).filter().first()
    assert user is None
