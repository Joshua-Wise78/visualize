"""Local Storage database in memory use.

Author: Joshua Wise
"""


class InMemoryStorage:
    """Lightweight non-persistent storage."""

    def __init__(self) -> None:
        """Initialize the empty dict."""
        self._store: dict[str, str] = {}

    def save(self, key: str, json_string: str) -> None:
        """Save the string into memory."""
        self._store[key] = json_string

    def get(self, key: str) -> str | None:
        """Get serialzed state by unique key.

        Returns:
            Serialzied string that contains serialized string

        """
        return self._store.get(key)
