from app.core.exceptions import StructuredOutOfBoundsError


class BoundsCheckMixin:
    def _bounds_check(self, index: int) -> bool:
        """Bounds check for checking any class with size attribute

        Arguments:
            index: The index location that we want to manipulate on.

        Returns:
            True if we are in bounds.
        """
        size = getattr(self, "size", None)

        if size is not None:
            if index < 0 or index >= size:
                raise StructuredOutOfBoundsError("Index out of bounds.")

        return True
