from argparse import ArgumentParser

from readers import LongReader, WordReader, LineReader


def main():
    parser = ArgumentParser()
    parser.add_argument('-dataType', type=str, default='long', choices=['long', 'word', 'line'])
    parser.add_argument('-sortingType', type=str, default='natural', choices=['natural', 'byCount'])
    args = parser.parse_args()

    reader = None
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

    reader.print_sorted_data(args.sortingType)


if __name__ == '__main__':
    main()
