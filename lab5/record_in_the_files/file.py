from typing import List

INPUT_FILE = "string.in"
OUTPUT_FILE = "string.out"


def read_input_data_from_file() -> List:
    with open(INPUT_FILE, "string.in") as input_file:
        return input_file.read().splitlines()


def write_output_data_from_file(substring_limit: List) -> None:
    with open(OUTPUT_FILE, "string.out") as output_file:
        output_file.write(str(substring_limit))