"""This module provides classes for reading different types of data from input."""
from abc import ABC, abstractmethod
from collections import Counter
from math import floor


class Reader(ABC):
    """Abstract base class for data readers."""

    @abstractmethod
    def collect_data(self) -> None:
        """Collect data from input."""
        pass

    @abstractmethod
    def print_sorted_data(self, sorting_type: str) -> str:
        """Print sorted data based on the specified sorting type."""
        pass


class LongReader(Reader):
    """Reader for long integers."""

    def print_sorted_data(self, sorting_type: str):
        print(f'Total numbers: {len(self.data)}.')
        if sorting_type == 'natural':
            sorted_data = sorted(self.data)
            print('Sorted data: ' + ' '.join(map(str, sorted_data)))
        else:
            counts = Counter(self.data)
            counts = dict(sorted(counts.items(), key=lambda item: (item[1], item[0])))
            output = []
            for c in counts:
                percent = floor(counts[c] / len(self.data) * 100)
                output.append(f'{c}: {counts[c]} time(s), {percent:.0f}%')
            print('\n'.join(output))


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

    def print_sorted_data(self, sorting_type: str) -> str:
        print(f'Total lines: {len(self.data)}.')
        if sorting_type == 'natural':
            sorted_data = sorted(self.data)
            print('Sorted data:')
            print('\n'.join(sorted_data))
        else:
            counts = Counter(self.data)
            counts = dict(sorted(counts.items(), key=lambda item: (item[1], item[0])))
            output = []
            for c in counts:
                percent = floor(counts[c] / len(self.data) * 100)
                output.append(f'{c}: {counts[c]} time(s), {percent:.0f}%')
            print('\n'.join(output))

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

    def print_sorted_data(self, sorting_type: str) -> str:
        print(f'Total words: {len(self.data)}.')
        if sorting_type == 'natural':
            sorted_data = sorted(self.data)
            print('Sorted data: ' + ' '.join(sorted_data))
        else:
            counts = Counter(self.data)
            counts = dict(sorted(counts.items(), key=lambda item: (item[1], item[0])))
            output = []
            for c in counts:
                percent = floor(counts[c] / len(self.data) * 100)
                output.append(f'{c}: {counts[c]} time(s), {percent:.0f}%')
            print('\n'.join(output))

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
