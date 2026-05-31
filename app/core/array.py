class TrackedArray[T]:
    def __init__(self, size: int):
        """Init function of the array.

        Arguments:
            self: context of the array
            size: The array size

        """
        self.size = size
        self._data: list[T | None] = [None] * size
        self.last_action: str = "Initalized"

    def insert(self, index: int, value: T) -> bool:
        """Insertion function for the array.

        Arguments:
            index: The index place to be inserted.
            value: Generic typic of the value to be inserted.

        """
        if index < 0 or index >= self.size:
            raise IndexError("Inded out of bounds")

        self._data[index] = value
        self.last_action = f"Inserted {value} at index {index}"
        return True

    def deletion(self, index: int) -> bool:
        """Deletion function for the array.

        Arguments:
            index: Location of deletion

        Returns:
            boolean of true or false depending on deletion

        """
        return False

    def read(self) -> list[T | None]:
        """Read function of the array.

        Returns:
            list of the generic array type

        """
        return self._data.copy()

    @property
    def is_full(self) -> bool:
        """Is full checker function."""
        return None not in self._data
