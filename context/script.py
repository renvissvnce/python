import argparse
import os
from typing import Union, Iterator, List


def read_input(input_stream: str) -> Union[Iterator, str]:
    if os.path.isfile(input_stream):
        with open(input_stream, 'r+', encoding='utf-8') as file:
            return iter(file.readlines())
    else:
        return iter(str(input_stream).split(sep='\n'))


def string_validation_by_length(iter_data: Iterator, word_lenght: int) -> List[str]:
    unique_lines = []
    # Of course we can use set, but I'm too lazy, for rewriting and testing code :(
    while True:
        try:
            iterator = next(iter_data)
            for word in iterator.split():
                if iterator in unique_lines:
                    pass
                elif len(word) == word_lenght:
                    unique_lines.append(iterator)
        except StopIteration:
            return unique_lines


def write_to_output(output_stream: Union[str, None], validated_data: List[str]) -> None:
    if not isinstance(output_stream, str):
        print(validated_data,
              f'\nSummary strings with specified symbol number is - {len(validated_data)}')
    else:
        with open(output_stream, 'w+', encoding='utf-8') as file:
            file.writelines(validated_data)
            file.write(f'\nSummary strings with specified symbol number is - {len(validated_data)}')


def result(input_stream: Union[str, None], output_stream: Union[str, None], length_of_word: int) -> None:
    data = read_input(input_stream)
    validated_data = string_validation_by_length(data, length_of_word)
    write_to_output(output_stream, validated_data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input-file', type=str,
                        help='file must be txt format, OR you can just paste text into variable')
    parser.add_argument('-o', '--output-file', type=str,
                        help='file must be txt format IF variable is empty result will be printed in stdout')
    parser.add_argument('-n', '--number', type=int, required=True, default=10, help='number of symbols in word')
    args = parser.parse_args()
    result(input_stream=args.input_file, output_stream=args.output_file, length_of_word=args.number)


if __name__ == '__main__':
    main()
