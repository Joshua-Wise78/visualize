from pydantic import BaseModel


class QueueOperation[T](BaseModel):
    """Operation for editing data."""

    value: T


class QueueStateResponse[T](BaseModel):
    """Queue response."""

    current_state: list[T]
    last_operation: str
    size: int
