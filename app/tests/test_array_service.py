"""Test Array features."""

import json
import pytest

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
    """Test deletion of values for array_service."""
    array_id, _ = array_service.create_array(3, ["first", "second", "third"])

    updated_array = array_service.delete_value(array_id, 1)

    assert updated_array.get_value(1) is None
    assert "Deleted second at index: 1" in updated_array.last_action

    db_data = db_client.get(array_id)

    assert db_data is not None

    parsed_data = json.loads(db_data)
    assert parsed_data["_data"][1] is None
    assert parsed_data["last_action"] == "Deleted second at index: 1"


def test_load_nonexistent_array(array_service: ArrayService):
    """Test loading a non-existent array from the database."""
    with pytest.raises(ValueError, match="not found in database"):
        array_service._load_from_db("fake-uuid-9000")


def test_get_value(array_service: ArrayService):
    """Test Getting a value that does and doesn't exist."""
    array_id, target_array = array_service.create_array(3, ["first", "second"])

    assert isinstance(array_id, str)
    assert isinstance(target_array, StaticArray)

    assert target_array.get_value(0) == "first"
    assert target_array.get_value(2) is None


def test_multi_type_array(array_service: ArrayService, db_client: InMemoryStorage):
    """Test an array with multiple data types."""
    array_id, _ = array_service.create_array(4, [])

    array_service.insert_value(array_id, index=0, value=42)  # Integer
    array_service.insert_value(array_id, index=1, value="hello world")  # String
    array_service.insert_value(array_id, index=2, value=3.14159)  # Float
    array_service.insert_value(array_id, index=3, value={"status": "ok"})  # Dictionary

    raw_db_data = db_client.get(array_id)

    assert raw_db_data is not None

    parsed_data = json.loads(raw_db_data)

    assert parsed_data["_data"][0] == 42
    assert parsed_data["_data"][1] == "hello world"
    assert parsed_data["_data"][2] == 3.14159
    assert parsed_data["_data"][3] == {"status": "ok"}

    assert "Inserted {'status': 'ok'} at index: 3" in parsed_data["last_action"]


def test_out_of_bounds(array_service: ArrayService):
    """Test out of bounds operations for array."""
    array_id, _ = array_service.create_array(3, ["a", "b", "c"])

    with pytest.raises(IndexError):
        array_service.insert_value(array_id, index=5, value="some val")

    with pytest.raises(IndexError):
        array_service.delete_value(array_id, index=-1)
