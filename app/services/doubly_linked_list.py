"""Service for doubly linked lists."""

import json
import uuid
from typing import Any

from app.core.doubly_linked_list import DoublyLinkedList


class DoublyLinkedService[T]:
    """Doubly Linked List service handling different operations."""

    def __init__(self, db_client: Any) -> None:
        """Init the DoublyLinkedList Service.

        Args:
            db_client: The database client.

        """
        self.db = db_client

    def create_doubly(
        self, doubly_id: str, initial_values: list[T] | None = None
    ) -> None:
        """Create doubly linked list.

        Args:
            doubly_id: The doubly linked list id
            initial_values: The starting values of the array

        """
        ...

    def insert_value(
        self, doubly_id: str, value: T, index: int | None = None
    ) -> None:
        """Insert a value into the doubly linked list.

        Args:
            doubly_id: The id of the doubly linked list
            value: The value to be inserted
            index: Optional value to insert mid list

        """
        ...

    def remove_value(self, doubly_id: str, value: T) -> None:
        """Remove value from the doubly linked list.

        Args:
            doubly_id: The id of the doubly linked list
            value: The value to be removed

        """
        ...

    def pop_value(self, doubly_id: str, index: int = -1) -> None:
        """Pop a value from the middle of the doubly linked list.

        Args:
            doubly_id: The doubly linked list id
            index: Optional value to pop from some index location

        """
        ...

    def get_all_values(self, doubly_id: str) -> list[T]:
        """Get all the values from the doubly linked list.

        Args:
            doubly_id: The id of the linked list

        Returns:
            list: Values from the doubly linked list.

        """
        ...

    def _load_from_db(self, doubly_id: str) -> DoublyLinkedList[T]:
        """Load state from the database.

        Args:
            doubly_id: The doubly linked list id

        Returns:
            DoublyLinkedList[T]: Generic linked list state from the database.

        """
        ...

    def _save_to_db(
        self, doubly_id: str, linked_list: DoublyLinkedList[T]
    ) -> None:
        """Save some state of the list to the database.

        Args:
            doubly_id: The id of the linked list
            linked_list: The list that will be saved to the database

        """
