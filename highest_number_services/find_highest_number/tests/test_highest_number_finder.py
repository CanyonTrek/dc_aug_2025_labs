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

if __name__ == "__main__":
    unittest.main()