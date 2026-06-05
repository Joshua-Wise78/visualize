import json
import uuid
from typing import Any

from app.core.array import StaticArray


class ArrayService:
    def __init__(self, db_client):
        self.db = db_client

    def create_array(self, size: int, inital_value: list) -> tuple[str, StaticArray]:
        array_id = str(uuid.uuid4())
        target_array = StaticArray(size)

        for i, val in enumerate(inital_value):
            if i < size:
                target_array.insert(i, val)

        self._save_to_db(array_id, target_array)
        return array_id, target_array

    def insert_value(self, array_id: str, index: int, value: Any) -> StaticArray:

        target_array = self._load_from_db(array_id)
        target_array.insert(index=index, value=value)
        target_array.last_action = f"Inserted {value} at index: {index}"

        self._save_to_db(array_id, target_array)

        return target_array

    def _save_to_db(self, array_id: str, array_obj: StaticArray):
        state_dict = {
            "size": array_obj.size,
            "_data": array_obj._data,
            "last_action": array_obj.last_action,
        }

        json_string = json.dumps(state_dict)
        self.db.save(array_id, json_string)

    def _load_from_db(self, array_id: str) -> StaticArray:
        raw_data = self.db.get(array_id)

        if not raw_data:
            raise ValueError(f"Array {array_id} not found in database")

        state_dict = json.loads(raw_data)

        reconstructed_array = StaticArray(size=state_dict["size"])
        reconstructed_array._data = state_dict["_data"]
        reconstructed_array.last_action = state_dict["last_action"]

        return reconstructed_array
