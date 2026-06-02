from app.core.base import BaseDataStructure
from app.core.mixins import BoundsCheckMixin


class StaticArray[T](BoundsCheckMixin, BaseDataStructure):
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
        if self._bounds_check(index):
            self._data[index] = None
        return True

    def contains(self, value: T) -> bool:
        """Check if a value is contained inside of the array.

        Arguments:
            value: Generic typing of the value, optionally passed
        """
        if value in self._data:
            return True

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
