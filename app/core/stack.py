"""Stack core operations.

Author: Joshua Wise
"""

from __future__ import annotations


class Node[T]:
    """Generic node for stack."""

    def __init__(self, value: T) -> None:
        """Create a new node."""
        self.data: T = value
        self.next: Node[T] | None


class Stack[T]:
    """Stack core class."""

    def __init__(self) -> None:
        """Init a new Stack."""
        self.top: Node[T] | None = None
        self.size: int = 0

    def is_empty(self) -> bool:
        """Check to see if the Stack is empty."""
        return self.top is None

    def push_value(self, value: T) -> None:
        """Push a new value onto the Stack."""
        new_node = Node(value)

        new_node.next = self.top

        self.top = new_node
        self.size += 1

    def pop_value(self) -> T:
        """Pop a value off of the stack."""
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack")

        popped_value = self.top

        assert popped_value is not None

        self.size -= 1
        return popped_value.data
