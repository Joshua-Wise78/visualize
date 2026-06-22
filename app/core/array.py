"""Array core operations.

Author: Joshua Wise
"""

from app.core.exceptions import ArgumentualError
from app.core.mixins import BoundsCheckMixin


class StaticArray[T](BoundsCheckMixin):
    """Static array class to handle array data structures."""

    def __init__(self, size: int) -> None:
        """Make a new StaticArray object."""
        if size < 0:
            raise ValueError("Static Array cannpt be negative.")

        self._data: list[T | None] = [None] * size
        self.size: int = size
        self.last_action: str = "Initialized"

    def insert(self, value: T | None, index: int | None) -> bool:
        """Insert value into array.

        Arguments:
            index: the index location
            value: generic typing of the value to be inserted

        """
        if index is None:
            raise ValueError("Index cannot be None for StaticArray insertion")

        self._bounds_check(index)

        if value is None:
            raise ValueError("Value cannot be None.")

        self._data[index] = value
        return True

    def deletion(self, index: int, value: T | None) -> bool:
        """Delete a value from the array.

        Arguments:
            index: Location of deletion
            value: The value to be inserted

        Returns:
            boolean of true or false depending on deletion

        """
        if self._bounds_check(index):
            self._data[index] = None
        return True

    def get_value(self, index: int) -> T | None:
        """Get a value from the index.

        Arguments:
            index: Location of the value

        Returns:
            Value from the array

        """
        self._bounds_check(index)
        return self._data[index]

    def contains(self, value: T | None, index: int | None) -> bool:
        """Check if a value is contained inside of the array.

        Arguments:
            value: Generic typing of the value, optionally passed
            index: Index location of the value

        """
        if value is None and index is None:
            raise ArgumentualError(
                "Must pass at least value or index for contains."
            )

        if value is not None:
            return any(val == value for val in self._data)

        if index is not None and 0 <= index < len(self._data):
            return self._data[index] is not None

        return False

    def traversal(self, value: T | None, index: int | None) -> bool:
        """Traversal of the array.

        Defaults to traversing the entire array is no index is passed.
        Also allows traversal until a value is found.

        Arguments:
            value: The value to be traversed to.
            index: The index location of desired traversal.

        """
        if not self.size:
            return False

        if index is not None:
            self._bounds_check(index)
            for i in range(index + 1):
                current_item = self._data[i]
                # TODO Need to add some sort of item for now
            return True

        if value is not None:
            for i in range(self.size):
                current_item = self._data[i]
                # TODO Some function here

                if current_item == value:
                    return True
            return False

        for i in range(self.size):
            current_item = self._data[i]
            # TODO Need some function here

        return True

    def display(self, value: T, index: int | None) -> bool:
        """Display the array until the index given or value.

        Arguments:
            value: The value to be displayed to.
            index: The index to be displayed to

        """
        if not self.size:
            return False

        if index is not None:
            self._bounds_check(index)
            for i in range(index + 1):
                print(str(value))

        for i in range(self.size):
            print(str(self._data[i]))

        return True

    @property
    def is_full(self) -> bool:
        """Is full checker function."""
        return None not in self._data
