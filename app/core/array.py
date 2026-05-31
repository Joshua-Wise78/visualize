from app.core.base import BaseDataStructure
from app.core.mixins import BoundsCheckMixin


class Array[T](BoundsCheckMixin, BaseDataStructure):
    def __init__(self, size: int):
        super().__init__(size)

    def insert(self, index: int, value: T) -> bool:
        """Insertion function for the array.

        Arguments:
            index: The index place to be inserted.
            value: Generic typic of the value to be inserted.

        """
        self._bounds_check(index)

        if value is None:
            raise ValueError("Value cannot be None.")

        self._data[index] = value
        return True

    def deletion(self, index: int) -> bool:
        """Deletion function for the array.

        Arguments:
            index: Location of deletion

        Returns:
            boolean of true or false depending on deletion

        """
        return False

    def contains(self, value: T | None, index: int | None) -> bool:
        """Check if a value is contained inside of the array.

        Arguments:
            value: Generic typing of the value, optionally passed
            index: Index location of the item to check if it exists
        """
        return False

    def traversal(self, value: T | None, index: int | None) -> bool:
        """Traversal of the array.

        Arguments:
            value: The value to be traversed to.
            index: The index location of desired traversal.
        """
        return False

    def display(self, value: T, index: int | None) -> list[T | None]:
        """Display the array until the index given or value.

        Arguments:
            value: The value to be displayed to.
            index: The index to be displayed to
        """
        return []

    @property
    def is_full(self) -> bool:
        """Is full checker function."""
        return None not in self._data
