from typing import List
from record_in_the_files.file import read_input_data_from_file, write_output_data_from_file


def beginning_and_end_str(string: str, substring: str) -> List:
    substring_limit = []
    string_length = len(string)
    substring_length = len(substring)
    if substring_length == 0:
        return substring_limit
    for string_iterator in range(string_length - substring_length + 1):
        for substring_iterator in range(substring_length):
            if string[string_iterator + substring_iterator] != substring[substring_iterator]:
                break
        else:
            substring_limit.append((string_iterator, string_iterator + substring_length - 1))
    return substring_limit


if __name__ == "__main__":
    input_string, substring_to_find = read_input_data_from_file()
    substring_points = beginning_and_end_str(input_string, substring_to_find)
    write_output_data_from_file(substring_points)
