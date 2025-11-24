from argparse import ArgumentParser

from readers import LongReader, WordReader, LineReader


def handle_argument_errors(args):
    if args.dataType == SENTINEL:
        print('No data type defined!')
        exit(1)
    if args.sortingType == SENTINEL:
        print('No sorting type defined!')
        exit(1)


SENTINEL = '_no_value_'

def main():
    parser = ArgumentParser()
    parser.add_argument('-dataType', type=str, nargs='?', const=SENTINEL, default=None)
    parser.add_argument('-sortingType', type=str, nargs='?', const=SENTINEL, default=None)
    parser.add_argument('-inputFile', type=str, nargs='?', const=None, default=None)
    parser.add_argument('-outputFile', type=str, nargs='?', const=None, default=None)

    args, unknown = parser.parse_known_args()

    for arg in unknown:
        print(f'"{arg}" is not a valid parameter. It will be skipped.')

    if args.sortingType is None:
        args.sortingType = 'natural'

    handle_argument_errors(args)

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

    reader.collect_data(args.inputFile)

    reader.print_sorted_data(args.sortingType)


if __name__ == '__main__':
    main()
