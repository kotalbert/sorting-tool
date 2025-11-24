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

class LineReader(Reader):
    """Reader for lines of text."""

    def __init__(self):
        self.data: list[str] = []

    def collect_data(self) -> None:
        """Collect lines of text from input."""

        while True:
            try:
                line = input()
                self.data.append(line)
            except EOFError:
                break

class WordReader(Reader):
    """Reader for words."""

    def __init__(self):
        self.data: list[str] = []

    def collect_data(self) -> None:
        """Collect words from input.

        Word is any number of characters separated by whitespace.
        """

        while True:
            try:
                line = input()
                words = line.split()
                self.data.extend(words)
            except EOFError:
                break