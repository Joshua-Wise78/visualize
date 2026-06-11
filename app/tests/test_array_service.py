"""Test Array features."""

import json
import pytest
from typing import Any

from app.core.array import StaticArray
from app.services.array_service import ArrayService
from app.core.database import InMemoryStorage


@pytest.fixture
def db_client() -> InMemoryStorage:
    """Create a fresh database for use later.

    Returns:
        InMemoryStorage object to store data structures

    """
    return InMemoryStorage()


@pytest.fixture
def array_service(db_client: InMemoryStorage) -> ArrayService:
    """Array service init.

    Returns:
        ArrayService object for testing.

    """
    return ArrayService(db_client)


def test_create_array(array_service: ArrayService, db_client: InMemoryStorage):
    """Test the create array and basic functionallity for it."""
    size = 5
    initial_values = ["apple", "banana", "cherry"]

    array_id, target_array = array_service.create_array(size, initial_values)

    assert isinstance(array_id, str)
    assert isinstance(target_array, StaticArray)
    assert target_array.size == 5

    assert target_array.get_value(0) == "apple"
    assert target_array.get_value(2) == "cherry"
    assert target_array.get_value(4) is None

    raw_db_data = db_client.get(array_id)
    assert raw_db_data is not None

    parsed_data = json.loads(raw_db_data)
    assert parsed_data["size"] == 5
    assert parsed_data["_data"][0] == "apple"
