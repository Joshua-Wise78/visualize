"""Test core StaticArray data structure features."""

from typing import Any

import pytest

from app.core.array import StaticArray
from app.core.exceptions import ArgumentualError, StructuredOutOfBoundsError


def test_array_initialization(static_array: StaticArray[Any]) -> None:
    """Test that the array initializes with the correct size and empty slots."""
    assert static_array.size == 5
    assert static_array.last_action == "Initialized"
    assert not static_array.is_full

    # Ensure all elements are initialized to None
    for i in range(5):
        assert static_array.get_value(i) is None


def test_array_insert(static_array: StaticArray[Any]) -> None:
    """Test inserting values directly into the core array."""
    success = static_array.insert(value="apple", index=0)

    assert success is True
    assert static_array.get_value(0) == "apple"


def test_array_deletion(static_array: StaticArray[Any]) -> None:
    """Test deleting values from the core array."""
    static_array.insert(value="banana", index=2)
    assert static_array.get_value(2) == "banana"

    success = static_array.deletion(index=2, value="banana")

    assert success is True
    assert static_array.get_value(2) is None


def test_array_contains(static_array: StaticArray[Any]) -> None:
    """Test the contains method checks by value or index."""
    static_array.insert(value="cherry", index=3)

    # Check by value
    assert static_array.contains(value="cherry", index=None) is True
    assert static_array.contains(value="grape", index=None) is False

    # Check by index
    assert static_array.contains(value=None, index=3) is True
    assert static_array.contains(value=None, index=1) is False

    # Check ArgumentualError when passing both as None
    with pytest.raises(ArgumentualError):
        static_array.contains(value=None, index=None)


def test_array_out_of_bounds(static_array: StaticArray[Any]) -> None:
    """Test bounds checking for core array operations."""
    with pytest.raises(StructuredOutOfBoundsError):
        static_array.insert(value="out-of-bounds", index=10)

    with pytest.raises(StructuredOutOfBoundsError):
        static_array.get_value(-1)


def test_array_is_full() -> None:
    """Test the is_full property."""
    arr = StaticArray(2)
    assert not arr.is_full

    arr.insert("a", 0)
    arr.insert("b", 1)

    assert arr.is_full
