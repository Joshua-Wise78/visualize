"""Linked list core data structure."""


class Node[T]:
    """Node class for the dynamic linked list."""

    def __init__(self, value: T):
        """Create a node."""
        self.value: T = value
        self.next: Node[T] | None = None
        self.prev: Node[T] | None = None


class DoublyLinkedList[T]:
    """The doubly linted list class."""

    def __init__(self):
        """Create a doubly linked list."""
        self.header = Node[T | None](None)
        self.tail = Node[T | None](None)

        # Link sentinels
        self.header.next = self.tail
        self.tail.prev = self.header

        self.size = 0

    def insert(self, value: T, index: int | None = None) -> None:
        """Insert a value inside of the doubly linked list.

        Arguments:
            value: The value to be inserted
            index: Optional value to insert mid list instead of appending.
        """
        pass

    def delete(self, value: T, index: int | None = None) -> None:
        """Delete a value inside of the doubly linked list."""
        pass

    def get_node(self, value: T, index: int | None = None):
        """Get a node from the doubly linked list."""
        pass

    def traversal(self, index: int | None = None):
        """Traverse the doubly linked list."""
        pass

    def _insert_between(
        self, value: T, predecessor: Node[T], successor: Node[T]
    ) -> None:
        """Univeral Helper method that will handle pointer logic.

        Arguments:
            value: The value of the new node.
            predecessor: The previous node.
            successor: The next node in line.
        """
        node = Node(value, prev=predecessor, next=successor)
        predecessor.next = node
        successor.prev = node
        self.size = self.size + 1
