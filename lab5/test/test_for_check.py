import unittest
from search_substring.substring_search import beginning_and_end_str


class TestForCheck(unittest.TestCase):
    def test_substring_not_found(self):
        input_string = "hhkhhkhhkhhkhhkhhkhhk"
        input_substring = "hhhk"
        substring_limit = beginning_and_end_str(input_string, input_substring)
        self.assertEqual([], substring_limit)

    def test_substring_in_find_the_word_in_the_sentence(self):
        input_string = "Chelsea_have_signed_Leicester_defender_Ben_Chilwell"
        input_substring = "defender"
        substring_limit = beginning_and_end_str(input_string, input_substring)
        self.assertEqual([(30, 37)], substring_limit)

    def test_substring_in_find_sequential_record(self):
        input_string = "tttttt"
        input_substring = "ttt"
        substring_limit = beginning_and_end_str(input_string, input_substring)
        self.assertEqual([(0, 2), (1, 3), (2, 4), (3, 5)], substring_limit)

    def test_substring_many_entries(self):
        input_string = "kickgoalforwardgoalmatchteamgoalkick"
        input_substring = "goal"
        substring_limit = beginning_and_end_str(input_string, input_substring)
        self.assertEqual([(4, 7), (15, 18), (24, 27)], substring_limit)

    def test_substring_in_find_identical_records(self):
        input_string = "Bernardo Silva became the top scorer this month. Fabio Silva gave the most assists in December."
        input_substring = "Silva"
        substring_limit = beginning_and_end_str(input_string, input_substring)
        self.assertEqual([(9, 13), (55, 59)], substring_limit)

    def test_empty_substring(self):
        input_string = "line"
        input_substring = ""
        substring_limit = beginning_and_end_str(input_string, input_substring)
        self.assertEqual([], substring_limit)

    def test_long_substring(self):
        input_string = "programming"
        input_substring = "programmin"
        substring_limit = beginning_and_end_str(input_string, input_substring)
        self.assertEqual([(0, 9)], substring_limit)

    def test_many_entries_of_one_letter(self):
        input_string = "work"
        input_substring = "w"
        substring_limit = beginning_and_end_str(input_string, input_substring)
        self.assertEqual([(0, 0), (1, 1), (2, 2), (3, 3)], substring_limit)


if __name__ == '__main__':
    unittest.main()
