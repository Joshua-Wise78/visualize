from pydantic import BaseModel


class ArrayBase[T](BaseModel):
    size: int
    initial_value: list[T | None] = []


class ArrayOperation[T](BaseModel):
    index: int
    value: T | None = None


class ArrayStateResponse[T](BaseModel):
    current_state: list[T | None]
    last_operation: str
    is_full: bool
