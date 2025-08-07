import unittest
from app.highest_number_finder import HighestNumberFinder

class TestHighestNumberFinder(unittest.TestCase):
    def test_find_highest_in_list_of_one_expect_single_item(self):
        # Arrange
        numbers = [10]
        expected_result = 10
        cut = HighestNumberFinder() # Class Under Test

        # Act
        actual_result = cut.find_highest_number(numbers)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_find_highest_in_list_of_two_descending_expect_first_item(self):
        # Arrange
        numbers = [13, 4]
        expected_result = 13
        cut = HighestNumberFinder() # Class Under Test

        # Act
        actual_result = cut.find_highest_number(numbers)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_find_highest_in_list_of_two_ascending_expect_second_item(self):
        # Arrange
        numbers = [4, 13]
        expected_result = 13
        cut = HighestNumberFinder() # Class Under Test

        # Act
        actual_result = cut.find_highest_number(numbers)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_find_highest_in_list_of_many_expect_highest_item(self):
        # Arrange
        numbers = [4, 5, -8, 3, 11, -21, 6]
        expected_result = 11
        cut = HighestNumberFinder() # Class Under Test

        # Act
        actual_result = cut.find_highest_number(numbers)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_find_empty_list_throws_exception(self):
        # Arrange
        numbers = []
        # expected_result = 11
        cut = HighestNumberFinder() # Class Under Test

        # Act
        actual_result = self.assertRaises(ValueError, cut.find_highest_number, numbers)

        # Assert
        self.assertIsNone(actual_result)


if __name__ == "__main__":
    unittest.main()