"""Service for stack."""

import json
import uuid
from typing import Any

from app.core.stack import Stack


class StackService[T]:
    """Stack service handling various operations."""

    def __init__(self, db_client: Any) -> None:
        """Init the Stack service.

        Args:
            db_client: Database client

        """
        self.db = db_client

    def create_stack(
        self, initial_values: list[T] | None = None
    ) -> tuple[str, Stack[T]]:
        """Create a stack.

        Args:
            initial_values: List of values to be inserted in the stack.

        """
        ...

    def push_value(self, stack_id: str, value: T) -> Stack[T]:
        """Push value onto the stack."""
        ...

    def pop_value(self, stack_id: str) -> Stack[T]:
        """Pop a value off the stack."""
        ...

    def _load_from_db(self, stack_id) -> Stack[T]:
        """Load a stack from the database."""
        ...

    def _save_to_db(self, stack_id: str, target_stack: Stack[T]) -> None:
        """Save a stack to the database."""
        ...
