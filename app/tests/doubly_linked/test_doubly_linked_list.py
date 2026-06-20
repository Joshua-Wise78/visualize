"""Test core Doubly Linked List data structure features."""

from typing import Any

import pytest

from app.core.doubly_linked_list import DoublyLinkedList, Node


def test_initialization(doubly_linked_list: DoublyLinkedList[Any]) -> None:
    """Test the base initialization of an empty doubly linked list."""
    assert len(doubly_linked_list) == 0
    assert doubly_linked_list.header.next is doubly_linked_list.tail
    assert doubly_linked_list.tail.prev is doubly_linked_list.header


def test_initialization_with_iterable() -> None:
    """Test initializing a linked list with a pre-existing iterable."""
    dll = DoublyLinkedList(["A", "B", "C"])
    assert len(dll) == 3
    assert list(dll) == ["A", "B", "C"]


def test_append(doubly_linked_list: DoublyLinkedList[Any]) -> None:
    """Test appending values to the end of the list."""
    doubly_linked_list.append("first")
    doubly_linked_list.append("second")

    assert len(doubly_linked_list) == 2
    assert list(doubly_linked_list) == ["first", "second"]


def test_insert(populated_doubly_linked_list: DoublyLinkedList[str]) -> None:
    """Test inserting values at specific indices."""
    # Insert at beginning
    populated_doubly_linked_list.insert(0, "zero")
    assert list(populated_doubly_linked_list)[0] == "zero"

    # Insert in middle
    populated_doubly_linked_list.insert(2, "one-and-a-half")
    assert list(populated_doubly_linked_list)[2] == "one-and-a-half"

    # Insert at end (out of bounds positive defaults to append)
    populated_doubly_linked_list.insert(100, "last")
    assert list(populated_doubly_linked_list)[-1] == "last"


def test_pop(populated_doubly_linked_list: DoublyLinkedList[str]) -> None:
    """Test popping values from the list."""
    # Default pop (end of list)
    popped = populated_doubly_linked_list.pop()
    assert popped == "third"
    assert len(populated_doubly_linked_list) == 2

    # Pop specific index
    popped_first = populated_doubly_linked_list.pop(0)
    assert popped_first == "first"
    assert len(populated_doubly_linked_list) == 1


def test_pop_empty(doubly_linked_list: DoublyLinkedList[Any]) -> None:
    """Test popping from an empty list raises an error."""
    with pytest.raises(IndexError, match="Cannot pop from empty list"):
        doubly_linked_list.pop()


def test_remove(populated_doubly_linked_list: DoublyLinkedList[str]) -> None:
    """Test removing a specific value by value matching."""
    populated_doubly_linked_list.remove("second")

    assert len(populated_doubly_linked_list) == 2
    assert "second" not in list(populated_doubly_linked_list)

    with pytest.raises(ValueError, match="not in the list"):
        populated_doubly_linked_list.remove("non-existent-value")


def test_get_node(populated_doubly_linked_list: DoublyLinkedList[str]) -> None:
    """Test retrieving a specific Node object by value or index."""
    # Get by value
    node_by_val = populated_doubly_linked_list.get_node(value="second")
    assert isinstance(node_by_val, Node)
    assert node_by_val.value == "second"

    # Get by index
    node_by_idx = populated_doubly_linked_list.get_node(value=None, index=0)
    assert node_by_idx.value == "first"
