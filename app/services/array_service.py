import json
import uuid
from app.core.array import StaticArray
from app.core.exceptions import StructuredOutOfBoundsError


class ArrayService:
    def __init__(self, db_client):
        self.db = db_client

    def create_array(self, size: int, inital_value: list) -> tuple[str, StaticArray]:
        array_id = str(uuid.uuid4())
        target_array = StaticArray(size)

        for i, val in enumerate(inital_value):
            if i < size:
                target_array.insert(i, val)

        # Database saving logic will go here

        return array_id, target_array

    def insert_value(self, array_id: str, index: int, value: any) -> StaticArray:
        # This will change mainly just to make the errors go away.
        target_array = StaticArray(index)
        return target_array

    def _save_to_db(self):
        pass

    def _load_from_db(self):
        pass
