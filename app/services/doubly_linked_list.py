import json
import uuid

from typing import Any

from app.core.doubly_linked_list import DoublyLinkedList


class DoublyLinkedService:
    """Doubly Linked List service handling different operations,"""

    def __init__(self, db_client: Any):
        """Init the DoublyLinkedList Service"""
        self.db = db_client

    def create_doubly(
        self, size: int, initital_value: list[Any]
    ) -> tuple[str, DoublyLinkedList[Any]]:

        doubly_id = str(uuid.uuid4())
        target_doubly = DoublyLinkedList[Any](size)

        for i, val in enumerate(initital_value):
            if i < size:
                target_doubly.insert(value=val, index=i)

        self._save_to_db(doubly_id, target_doubly)
        return doubly_id, target_doubly

    def insert_value(self, doubly_id: str, index: int | None = None):
        # Will return a DoublyLinkedList
        pass

    def delete_value(self, doubly_id: str, index: int | None = None):
        # Will return a DoublyLinkedList
        pass

    def _save_to_db(self, doubly_id: str, doubly_obj: DoublyLinkedList[Any]):
        pass

    def _load_from_db(self, doubly_id: str, doubly_obj: DoublyLinkedList[Any]):
        pass
