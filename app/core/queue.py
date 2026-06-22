"""Queue core operations.

Author: Joshua Wise
"""

from __future__ import annotations


class Node[T]:
    """Generic node for queue."""

    def __init__(self, value: T) -> None:
        """Create a new node."""
        self.data: T = value
        self.next: Node[T] | None


class Queue[T]:
    """Queue core class."""

    def __init__(self) -> None:
        """Init a new Queue."""
        self.front: Node[T] | None = None
        self.rear: Node[T] | None = None
        self.size: int = 0

    def is_empty(self) -> bool:
        """Check for is empty."""
        return self.front is None

    def get_size(self) -> int:
        """Return size of the queue."""
        return self.size

    def enqueue(self, value: T) -> None:
        """Add an item to the rear of the queue.

        Args:
            value: The value to be inserted into the queue.

        """
        new_node = Node(value)

        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            if self.rear:
                self.rear.next = new_node
            self.rear = new_node

        self.size += 1

    def dequeue(self) -> T:
        """Remove and return the value at the front of the queue."""
        if self.is_empty():
            raise IndexError(
                "Queue Underflow: Cannot dequue from an empty queue"
            )

        removed_node = self.front

        assert removed_node is not None

        if self.front is None:
            self.rear = None

        self.size -= 1
        return removed_node.data
