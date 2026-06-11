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


def test_insert(array_service: ArrayService, db_client: InMemoryStorage):
    """Test insertion of array and validate the database client."""
    array_id, _ = array_service.create_array(3, ["first"])

    updated_array = array_service.insert_value(array_id, index=1, value="second")

    assert updated_array.get_value(1) == "second"
    assert "Inserted second at index: 1" in updated_array.last_action

    db_data = db_client.get(array_id)

    assert db_data is not None

    parsed_data = json.loads(db_data)
    assert parsed_data["_data"][1] == "second"
    assert parsed_data["last_action"] == "Inserted second at index: 1"


def test_deletion(array_service: ArrayService, db_client: InMemoryStorage):
    array_id, _ = array_service.create_array(3, ["first", "second", "third"])

    updated_array = array_service.delete_value(array_id, 1)

    assert updated_array.get_value(1) is None
    assert "Deleted second at index: 1" in updated_array.last_action

    db_data = db_client.get(array_id)

    assert db_data is not None

    parsed_data = json.loads(db_data)
    assert parsed_data["_data"][1] is None
    assert parsed_data["last_action"] == "Deleted second at index: 1"
