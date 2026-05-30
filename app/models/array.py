from pydantic import BaseModel


class ArrayConfig(BaseModel):
    size: int
    inital_values: list[int] = []


class ArrayOperation(BaseModel):
    index: int
    value: int | None = None


class ArraStateResponse(BaseModel):
    current_state: list[int | None]
    last_operation: str
    is_full: bool
