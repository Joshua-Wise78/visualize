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

    def _insert_between(
        self, value: T, predecessor: Node[T | None], successor: Node[T | None]
    ) -> None:
        """Univeral Helper method that will handle pointer logic.

        Arguments:
            value: The value of the new node.
            predecessor: The previous node.
            successor: The next node in line.
        """
        node = Node[T | None](value)

        node.prev = predecessor
        node.next = successor

        predecessor.next = node
        successor.prev = node

        self.size += 1

    def insert(self, value: T, index: int | None = None) -> None:
        """Insert a value inside of the doubly linked list.

        Arguments:
            value: The value to be inserted
            index: Optional value to insert mid list instead of appending.
        """
        if index is None or index >= self.size:
            assert self.tail.prev is not None
            self._insert_between(
                value, predecessor=self.tail.prev, successor=self.tail
            )
            return

        if index < 0:
            index = 0

        current: Node[T | None] | None = self.header.next

        for _ in range(index):
            if current is not None:
                current = current.next

        assert current is not None
        assert current.prev is not None

        self._insert_between(value, predecessor=current.prev, successor=current)

    def delete(self, value: T, index: int | None = None) -> None:
        """Delete a value inside of the doubly linked list.

        Arguments:
            value: The value to be deleted
            index: Optional int value of the node location

        """
        if index is None or index >= self.size:
            assert self.tail.prev is not None
            return

        if index < 0:
            index = 0

        current: Node[T | None] | None = self.header.next

        for _ in range(index):
            if current is not None:
                current = current.next

    def get_node(self, value: T, index: int | None = None):
        """Get a node from the doubly linked list."""
        pass

    def traversal(self, index: int | None = None):
        """Traverse the doubly linked list."""
        pass
