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
    def analyze_data(self) -> None:
        """Analyze collected data and print results."""
        pass

class LongReader(Reader):
    """Reader for long integers."""

    def analyze_data(self) -> None:
        """Analyze collected long integers and print results.

        - total number of integers
        - greatest value
        - number of occurrences of the greatest value
        - percentage of the greatest value occurrences
        """

        total = len(self.data)
        greatest = max(self.data)
        counts = Counter(self.data)
        num_of_greatest = counts[greatest]
        percentage = floor((num_of_greatest / total) * 100)

        print(f'Total numbers: {total}.')
        print(f'The greatest number: {greatest} ({num_of_greatest} time(s), {percentage:.0f}%).')

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

    def analyze_data(self) -> None:
        """Analyze collected lines of text and print results.

        - total number of lines
        - longest line
        - number of occurrences of the longest line
        - percentage of the longest line occurrences
        """

        total = len(self.data)
        longest_line = max(self.data, key=len)
        counts = Counter(self.data)
        num_of_longest = counts[longest_line]
        percentage = floor((num_of_longest / total) * 100)

        print(f'Total lines: {total}.')
        print('The longest line:')
        print(longest_line)
        print(f'({num_of_longest} times(s), {percentage:.0f}%).')

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

    def analyze_data(self) -> None:
        """Analyze collected words and print results.

        - total number of words
        - longest word
        - number of occurrences of the longest word
        - percentage of the longest word occurrences
        """

        total = len(self.data)
        longest_word = max(self.data, key=len)
        counts = Counter(self.data)
        num_of_longest = counts[longest_word]
        percentage = floor((num_of_longest / total) * 100)

        print(f'Total words: {total}.')
        print(f'The longest word: {longest_word} ({num_of_longest} time(s), {percentage:.0f}%).')

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
