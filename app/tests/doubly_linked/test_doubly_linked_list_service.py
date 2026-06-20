"""Test Doubly Linked List Service persistence and orchestration features."""

import json
from typing import Any

import pytest

from app.core.database import InMemoryStorage
from app.core.doubly_linked_list import DoublyLinkedList
from app.services.doubly_linked_list import DoublyLinkedService


def test_create_doubly_persists_to_db(
    doubly_linked_service: DoublyLinkedService[Any], db_client: InMemoryStorage
) -> None:
    """Test creating a doubly linked list saves state to the database."""
    initial_values = ["alpha", "beta", "gamma"]

    returned_id, target_list = doubly_linked_service.create_doubly(
        initial_values
    )

    assert isinstance(returned_id, str)
    assert isinstance(target_list, DoublyLinkedList)

    raw_db_data = db_client.get(returned_id)
    assert raw_db_data is not None

    parsed_data = json.loads(raw_db_data)
    assert "current_state" in parsed_data
    assert parsed_data["current_state"] == ["alpha", "beta", "gamma"]
    assert parsed_data["size"] == 3
    assert parsed_data["last_action"] == "Initialized"


def test_insert_value_updates_db(
    doubly_linked_service: DoublyLinkedService[Any], db_client: InMemoryStorage
) -> None:
    """Test inserting a value through the service updates the database."""
    test_id, _ = doubly_linked_service.create_doubly(["first"])

    doubly_linked_service.insert_value(test_id, value="second")

    db_data = db_client.get(test_id)
    assert db_data is not None

    parsed_data = json.loads(db_data)
    assert parsed_data["current_state"] == ["first", "second"]
    assert parsed_data["last_action"] == "Appended second"

    doubly_linked_service.insert_value(test_id, value="middle", index=1)

    db_data2 = db_client.get(test_id)
    assert db_data2 is not None

    parsed_data2 = json.loads(db_data2)
    assert parsed_data2["current_state"] == ["first", "middle", "second"]
    assert parsed_data2["last_action"] == "Inserted middle at index: 1"


def test_remove_value_updates_db(
    doubly_linked_service: DoublyLinkedService[Any], db_client: InMemoryStorage
) -> None:
    """Test removing a value through the service updates the database."""
    test_id, _ = doubly_linked_service.create_doubly(["keep", "drop"])

    doubly_linked_service.remove_value(test_id, value="drop")

    db_data = db_client.get(test_id)
    assert db_data is not None

    parsed_data = json.loads(db_data)
    assert "drop" not in parsed_data["current_state"]
    assert parsed_data["size"] == 1
    assert parsed_data["last_action"] == "Removed drop"


def test_pop_value_updates_db(
    doubly_linked_service: DoublyLinkedService[Any], db_client: InMemoryStorage
) -> None:
    """Test popping a value through the service updates the database."""
    test_id, _ = doubly_linked_service.create_doubly(["a", "b", "c"])

    popped_val = doubly_linked_service.pop_value(test_id, index=0)
    assert popped_val == "a"

    db_data = db_client.get(test_id)
    assert db_data is not None

    parsed_data = json.loads(db_data)
    assert parsed_data["current_state"] == ["b", "c"]
    assert parsed_data["last_action"] == "Popped a"


def test_get_all_values(
    doubly_linked_service: DoublyLinkedService[Any],
) -> None:
    """Test retrieving all values as a standard Python list."""
    test_id, _ = doubly_linked_service.create_doubly(["x", "y", "z"])

    values = doubly_linked_service.get_all_values(test_id)

    assert isinstance(values, list)
    assert values == ["x", "y", "z"]


def test_load_nonexistent_doubly_list(
    doubly_linked_service: DoublyLinkedService[Any],
) -> None:
    """Test loading a non-existent list from the database raises an error."""
    with pytest.raises(ValueError, match="not found in database"):
        doubly_linked_service._load_from_db("fake-uuid-9000")
