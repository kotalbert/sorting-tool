from collections import Counter
from argparse import ArgumentParser

from readers import LongReader, Reader


def main():
    parser = ArgumentParser()
    parser.add_argument('-dataType', type=str, default='long', choices=['long', 'word', 'line'], )
    args = parser.parse_args()

    match args.dataType:
        case 'long':
            reader = LongReader()
        case 'word':
            pass
        case 'line':
            pass
        case _:
            reader = LongReader()

    reader.collect_data()
    print(reader.data)


if __name__ == '__main__':
    main()
