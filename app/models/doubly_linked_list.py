"""Pydantic models for Linked List."""

from __future__ import annotations


from pydantic import BaseModel


class LinkedListOperation[T](BaseModel):
    """Operation for editing data."""

    value: T
    index: int | None = None


class LinkedListStateResponse[T](BaseModel):
    """Linked list response returned to the client."""

    current_state: list[T]
    last_operation: str
    size: int
