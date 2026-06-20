"""Linked list core data structure."""

from collections.abc import Iterable, Iterator
from typing import cast


class Node[T]:
    """Node class for the dynamic linked list."""

    def __init__(self, value: T) -> None:
        """Create a node."""
        self.value: T = value
        self.next: Node[T] | None = None
        self.prev: Node[T] | None = None


class DoublyLinkedList[T]:
    """The doubly linted list class."""

    def __init__(self, iterable: Iterable[T] | None = None) -> None:
        """Create a doubly linked list."""
        self.header: Node[T] = cast(Node[T], Node(None))
        self.tail: Node[T] = cast(Node[T], Node(None))

        # Link sentinels
        self.header.next = self.tail
        self.tail.prev = self.header

        self.last_action: str = "Initialized"

        self._size = 0

        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __len__(self) -> int:
        """Return the current number of nodes in the list."""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Make native Python iteration over the linked list."""
        current = self.header.next
        while current is not None and current is not self.tail:
            yield current.value
            current = current.next

    def _insert_between(
        self, value: T, predecessor: Node[T], successor: Node[T]
    ) -> None:
        """Universal helper method that handles pointer logic."""
        node = Node[T](value)

        node.prev = predecessor
        node.next = successor

        predecessor.next = node
        successor.prev = node

        self._size += 1

    def append(self, value: T) -> None:
        """Add a value to the end of the doubly linked list.

        Args:
            value: The value that will be inserted

        """
        assert self.tail.prev is not None
        self._insert_between(
            value, predecessor=self.tail.prev, successor=self.tail
        )

    def insert(self, index: int, value: T) -> None:
        """Insert some value at a specific index."""
        if index < 0:
            index = max(0, index + self._size)

        if index >= self._size:
            self.append(value)
            return

        current = self.header.next
        for _ in range(index):
            assert current is not None
            current = current.next

        assert current is not None
        assert current.prev is not None

        self._insert_between(value, predecessor=current.prev, successor=current)

    def pop(self, index: int = -1) -> T:
        """Pop a node off from the middle of the doubly linked list.

        Args:
            index: The location of the node to be 'poped' Defaults to -1

        """
        if self._size == 0:
            raise IndexError("Cannot pop from empty list.")

        if index < 0:
            index += self._size

        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds.")

        current = self.header.next
        for _ in range(index):
            assert current is not None
            current = current.next

        assert current is not None
        assert current.prev is not None
        assert current.next is not None

        current.prev.next = current.next
        current.next.prev = current.prev
        self._size -= 1

        return current.value

    def remove(self, value: T) -> None:
        """Remove a node using the value param.

        Args:
            value: The value to be removed

        """
        current = self.header.next

        while current is not None and current is not self.tail:
            if current.value == value:
                assert current.prev is not None
                assert current.next is not None

                current.prev.next = current.next
                current.next.prev = current.prev
                self._size -= 1
                return
            current = current.next

        raise ValueError(f"{value} not in the list.")

    def get_node(self, value: T, index: int | None = None) -> Node[T]:
        """Get a node from the doubly linked list.

        Args:
            value: The value of the node.
            index: The index location of the node optional

        """
        if index is not None:
            if index < 0 or index >= self._size:
                raise IndexError("Index out of bounds.")

            current = self.header.next

            for _ in range(index):
                assert current is not None
                current = current.next

            assert current is not None
            assert current.prev is not None
            assert current.next is not None

            return current

        if value is not None:
            current = self.header.next

            while current is not self.tail and current is not None:
                if current.value == value:
                    return current

                current = current.next

        raise ValueError("Node not found.")

    def traversal(self, index: int | None = None) -> None:
        """Traverse through the doubly linked list to do something.

        Args:
            index: The optional index location of where to traverse up to.

        """
        if index is not None:
            if index < 0 or index >= self._size:
                raise IndexError("Index out of bounds.")

            current = self.header.next

            for _ in range(index):
                assert current is not None
                current = current.next

                # TODO Add some function here for the traversal

        current = self.header.next

        while current is not self.tail and current is not None:
            # TODO Some method here for some function
            current = current.next
