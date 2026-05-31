from abc import ABC, abstractmethod


class BaseDataStructure[T](ABC):
    @abstractmethod
    def insert(self, value: T, index: int | None) -> bool:
        """Add a value to the structure"""
        pass

    @abstractmethod
    def deletion(self, index: int, value: T | None) -> bool:
        """Delete a value from the structure"""
        pass

    @abstractmethod
    def contains(self, value: T | None, index: int | None) -> bool:
        """Contain method for the structure"""
        pass

    @abstractmethod
    def traversal(self, value: T | None, index: int | None) -> bool:
        """Traverse the structure for ease of user later"""
        pass

    @abstractmethod
    def display(self, value: T, index: int | None) -> list[T | None]:
        """Display the structure to the console"""
        pass
