"""This module provides classes for reading different types of data from input."""
from abc import ABC, abstractmethod


class Reader(ABC):
    """Abstract base class for data readers."""

    @abstractmethod
    def collect_data(self) -> None:
        """Collect data from input."""
        pass


class LongReader(Reader):
    """Reader for long integers."""

    def __init__(self):
        self.data: list[int] = []

    def collect_data(self) -> None:
        """Collect long integers from input."""

        while True:
            try:
                line = input()
                numbers = map(int, line.split())
                self.data.extend(numbers)
            except EOFError:
                break
