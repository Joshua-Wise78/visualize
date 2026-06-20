"""Global fixtures for testing core classes and services."""

from typing import Any

import pytest

from app.core.array import StaticArray
from app.core.database import InMemoryStorage
from app.core.doubly_linked_list import DoublyLinkedList
from app.services.array_service import ArrayService
from app.services.doubly_linked_list import DoublyLinkedService


@pytest.fixture
def db_client() -> InMemoryStorage:
    """Create a fresh in-memory database for use in each test.

    Returns:
        InMemoryStorage: The fresh database client.

    """
    return InMemoryStorage()


@pytest.fixture
def array_service(db_client: InMemoryStorage) -> ArrayService[Any]:
    """Create a fresh ArrayService instance for testing.

    Args:
        db_client: The in-memory database client fixture.

    Returns:
        ArrayService: The initialized array service.

    """
    return ArrayService(db_client)


@pytest.fixture
def doubly_linked_service(
    db_client: InMemoryStorage,
) -> DoublyLinkedService[Any]:
    """Create a fresh DoublyLinkedService instance for testing.

    Args:
        db_client: The in-memory database client fixture.

    Returns:
        DoublyLinkedService: The initialized doubly linked list service.

    """
    return DoublyLinkedService(db_client)


@pytest.fixture
def static_array() -> StaticArray[Any]:
    """Create a basic StaticArray of size 5 for testing core logic.

    Returns:
        StaticArray: The core array structure.

    """
    return StaticArray(5)


@pytest.fixture
def doubly_linked_list() -> DoublyLinkedList[Any]:
    """Create a basic empty DoublyLinkedList for testing core logic.

    Returns:
        DoublyLinkedList: The core linked list structure.

    """
    return DoublyLinkedList()


@pytest.fixture
def populated_doubly_linked_list() -> DoublyLinkedList[str]:
    """Create a DoublyLinkedList pre-populated with basic values.

    Returns:
        DoublyLinkedList: A populated list containing string elements.

    """
    return DoublyLinkedList(["first", "second", "third"])
