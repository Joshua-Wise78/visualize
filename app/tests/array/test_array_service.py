"""Test Array Service persistence and orchestration features."""

import json
from typing import Any

import pytest

from app.core.array import StaticArray
from app.core.database import InMemoryStorage
from app.services.array_service import ArrayService


def test_create_array_persists_to_db(
    array_service: ArrayService[Any], db_client: InMemoryStorage
) -> None:
    """Test the create array service correctly saves to the database."""
    size = 5
    initial_values = ["apple", "banana", "cherry"]

    array_id, target_array = array_service.create_array(size, initial_values)

    assert isinstance(array_id, str)
    assert isinstance(target_array, StaticArray)

    # Validate DB persistence
    raw_db_data = db_client.get(array_id)
    assert raw_db_data is not None

    parsed_data = json.loads(raw_db_data)
    assert parsed_data["size"] == 5
    assert parsed_data["_data"][0] == "apple"
    assert parsed_data["_data"][2] == "cherry"


def test_insert_updates_db(
    array_service: ArrayService[Any], db_client: InMemoryStorage
) -> None:
    """Test insertion through the service updates the database client."""
    array_id, _ = array_service.create_array(3, ["first"])

    updated_array = array_service.insert_value(
        array_id, index=1, value="second"
    )

    assert "Inserted second at index: 1" in updated_array.last_action

    db_data = db_client.get(array_id)
    assert db_data is not None

    parsed_data = json.loads(db_data)
    assert parsed_data["_data"][1] == "second"
    assert parsed_data["last_action"] == "Inserted second at index: 1"


def test_delete_updates_db(
    array_service: ArrayService[Any], db_client: InMemoryStorage
) -> None:
    """Test deletion through the service updates the database."""
    array_id, _ = array_service.create_array(3, ["first", "second", "third"])

    updated_array = array_service.delete_value(array_id, 1)

    assert "Deleted second at index: 1" in updated_array.last_action

    db_data = db_client.get(array_id)
    assert db_data is not None

    parsed_data = json.loads(db_data)
    assert parsed_data["_data"][1] is None
    assert parsed_data["last_action"] == "Deleted second at index: 1"


def test_load_nonexistent_array(array_service: ArrayService[Any]) -> None:
    """Test loading a non-existent array from the database raises an error."""
    with pytest.raises(ValueError, match="not found in database"):
        array_service._load_from_db("fake-uuid-9000")


def test_multi_type_array_persistence(
    array_service: ArrayService[Any], db_client: InMemoryStorage
) -> None:
    """Test an array with multiple data types serializes correctly."""
    array_id, _ = array_service.create_array(4, [])

    array_service.insert_value(array_id, index=0, value=42)  # Integer
    array_service.insert_value(array_id, index=1, value="hello world")  # String
    array_service.insert_value(array_id, index=2, value=3.14159)  # Float
    array_service.insert_value(
        array_id, index=3, value={"status": "ok"}
    )  # Dictionary

    raw_db_data = db_client.get(array_id)
    assert raw_db_data is not None

    parsed_data = json.loads(raw_db_data)

    assert parsed_data["_data"][0] == 42
    assert parsed_data["_data"][1] == "hello world"
    assert parsed_data["_data"][2] == 3.14159
    assert parsed_data["_data"][3] == {"status": "ok"}
    assert "Inserted {'status': 'ok'} at index: 3" in parsed_data["last_action"]
