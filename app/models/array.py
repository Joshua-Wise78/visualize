from pydantic import BaseModel


class ArrayConfig(BaseModel):
    size: int
    inital_values: list[int] = []


class ArrayOperation[T](BaseModel):
    index: int
    value: T | None = None


class ArraStateResponse[T](BaseModel):
    current_state: list[T | None]
    last_operation: str
    is_full: bool
