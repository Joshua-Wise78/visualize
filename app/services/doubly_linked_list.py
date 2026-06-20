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
        self, initial_values: list[T] | None = None
    ) -> tuple[str, DoublyLinkedList[T]]:
        """Create doubly linked list.

        Args:
            initial_values: The starting values of the array

        """
        doubly_id = str(uuid.uuid4())
        target_doubly = DoublyLinkedList[T](
            initial_values if initial_values else []
        )
        self._save_to_db(doubly_id, target_doubly)
        return doubly_id, target_doubly

    def insert_value(
        self, doubly_id: str, value: T, index: int | None = None
    ) -> DoublyLinkedList[T]:
        """Insert a value into the doubly linked list.

        Args:
            doubly_id: The id of the doubly linked list
            value: The value to be inserted
            index: Optional value to insert mid list

        """
        target_doubly = self._load_from_db(doubly_id)

        if index is not None:
            target_doubly.insert(index, value)
            target_doubly.last_action = f"Inserted {value} at index: {index}"
        else:
            target_doubly.append(value)
            target_doubly.last_action = f"Appended {value}"

        self._save_to_db(doubly_id, target_doubly)
        return target_doubly

    def remove_value(self, doubly_id: str, value: T) -> DoublyLinkedList[T]:
        """Remove value from the doubly linked list.

        Args:
            doubly_id: The id of the doubly linked list
            value: The value to be removed

        """
        target_doubly = self._load_from_db(doubly_id)
        target_doubly.remove(value)

        target_doubly.last_action = f"Removed {value}"

        self._save_to_db(doubly_id, target_doubly)
        return target_doubly

    def pop_value(self, doubly_id: str, index: int = -1) -> T:
        """Pop a value from the middle of the doubly linked list.

        Args:
            doubly_id: The doubly linked list id
            index: Optional value to pop from some index location

        """
        target_doubly = self._load_from_db(doubly_id)
        popped_value = target_doubly.pop(index)

        target_doubly.last_action = f"Popped {popped_value}"

        self._save_to_db(doubly_id, target_doubly)
        return popped_value

    def get_all_values(self, doubly_id: str) -> list[T]:
        """Get all the values from the doubly linked list.

        Args:
            doubly_id: The id of the linked list

        Returns:
            list: Values from the doubly linked list.

        """
        target_doubly = self._load_from_db(doubly_id)
        return list(target_doubly)

    def _load_from_db(self, doubly_id: str) -> DoublyLinkedList[T]:
        """Load state from the database.

        Args:
            doubly_id: The doubly linked list id

        Returns:
            DoublyLinkedList[T]: Generic linked list state from the database.

        """
        raw_data = self.db.get(doubly_id)

        if not raw_data:
            raise ValueError(f"List {doubly_id} not found in database")

        parsed_json = json.loads(raw_data)
        reconstructed_list = DoublyLinkedList[T](parsed_json["current_state"])
        reconstructed_list.last_action = parsed_json.get(
            "last_action", "Initialized"
        )
        return reconstructed_list

    def _save_to_db(
        self, doubly_id: str, target_doubly: DoublyLinkedList[T]
    ) -> None:
        """Save some state of the list to the database.

        Args:
            doubly_id: The id of the linked list
            target_doubly: The list that will be saved to the database

        """
        state_dict = {
            "current_state": list(target_doubly),
            "last_action": target_doubly.last_action,
            "size": len(target_doubly),
        }

        json_string = json.dumps(state_dict)
        self.db.save(doubly_id, json_string)
