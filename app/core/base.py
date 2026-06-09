"""Base module that defines data structures.

Author: Joshua Wise
"""

from abc import ABC, abstractmethod


class BaseDataStructure[T](ABC):
    """The base structure outline each structure will need.

    This is an outline and extra methods can be passed or just defaulted out.

    Arguments:
        ABC: The default abstraction method used to require defined functions

    """

    def __init__(self, size: int | None):
        """Init for data structure."""
        if size is None:
            # If the size is None aka Tree/Tries
            self._data: list[T | None]
        else:
            # If the size is not none aka Array like structures
            self._data: list[T | None] = [None] * size

        self.size = size
        self.last_action: str = "Initialized"

    @abstractmethod
    def insert(self, value: T, index: int | None) -> bool:
        """Add a value to the structure."""
        pass

    @abstractmethod
    def deletion(self, index: int, value: T | None) -> bool:
        """Delete a value from the structure."""
        pass

    @abstractmethod
    def contains(self, value: T | None, index: int | None) -> bool:
        """Contain method for the structure."""
        pass

    @abstractmethod
    def traversal(self, value: T | None, index: int | None) -> bool:
        """Traverse the structure for ease of user later."""
        pass

    @abstractmethod
    def display(self, value: T, index: int | None) -> bool:
        """Display the structure to the console."""
        pass
