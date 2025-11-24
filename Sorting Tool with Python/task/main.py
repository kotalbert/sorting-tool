from collections import Counter

def main():
    numbers = []

    while True:
        try:
            data = input()
            new_nums = get_numbers(data)
            numbers.extend(new_nums)
        except EOFError:
            break

    n, maximum, n_of_max = analyze_numbers(numbers)
    print(f'Total numbers: {n}.\n'
          f'The greatest number: {maximum} ({n_of_max} time(s)).')

def analyze_numbers(numbers: list[int]) -> tuple[int, int, float]:
    """Analyze a list of integers and return
     - the numbers of integers
     - the maximum value
     - how often the maximum value occurs
     """
    maximum = max(numbers)
    number_of_integers = len(numbers)
    counts = Counter(numbers)
    number_of_max_occurrences = counts[maximum]


    return number_of_integers, maximum, number_of_max_occurrences


def get_numbers(d) -> list[int]:
    """Extracts integers from a given string."""
    strs = d.split()
    return list(map(int, strs))


if __name__ == '__main__':
    main()
