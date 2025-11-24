from argparse import ArgumentParser

from readers import LongReader, WordReader, LineReader


def main():
    parser = ArgumentParser()
    parser.add_argument('-dataType', type=str, default='long', choices=['long', 'word', 'line'], )
    parser.add_argument('-sortIntegers', action='store_true', default=False)
    args = parser.parse_args()

    reader = None
    # guard against reading words or lines when sorting integers
    if args.sortIntegers:
        args.dataType = 'long'

    match args.dataType:
        case 'long':
            reader = LongReader()
        case 'word':
            reader = WordReader()
        case 'line':
            reader = LineReader()
        case _:
            reader = LongReader()

    reader.collect_data()

    if not args.sortIntegers:
        reader.analyze_data()
    else:

        num_of_ints = len(reader.data)
        reader.data.sort()
        sorted_str = ' '.join(map(str, reader.data))
        print(f'Total numbers: {num_of_ints}.')
        print(f'Sorted data: {sorted_str}')


if __name__ == '__main__':
    main()
