"""Pydantic models for Array."""

from pydantic import BaseModel


class ArrayBase[T](BaseModel):
    """Base array model."""

    size: int
    initial_value: list[T | None] = []


class ArrayOperation[T](BaseModel):
    """Array operation model."""

    index: int
    value: T | None = None


class ArrayStateResponse[T](BaseModel):
    """Array State Response model."""

    current_state: list[T | None]
    last_operation: str
    is_full: bool
