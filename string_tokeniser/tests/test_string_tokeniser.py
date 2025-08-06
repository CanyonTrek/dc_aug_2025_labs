
import unittest
from app.string_tokeniser import StringTokeniser

class TestStringTokeniser(unittest.TestCase):
    def test_empty_string_result_empty_list(self):
        # 3A's = AAA - Arrange, Act, Assert
        # Arrange
        input_val = ""
        expected_result = []
        cut = StringTokeniser() # Class Under Test

        # Act
        actual_result = cut.tokenise(input_val)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_string_of_one_result_list_of_one(self):
        # AAA in testing - Arrange, Act, Assert
        # Arrange
        input_val = "csharp"
        expected_result = ["csharp"]
        cut = StringTokeniser() # Class Under Test

        # Act
        actual_result = cut.tokenise(input_val)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_string_of_two_items_result_list_of_two_items(self):
        # AAA in testing - Arrange, Act, Assert
        # Arrange
        input_val = "csharp,python"
        expected_result = ["csharp", "python"]
        cut = StringTokeniser() # Class Under Test

        # Act
        actual_result = cut.tokenise(input_val)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_string_of_many_items_result_list_of_many_items(self):
        # AAA in testing - Arrange, Act, Assert
        # Arrange
        input_val = "java,csharp,python"
        expected_result = ["java", "csharp", "python"]
        cut = StringTokeniser() # Class Under Test

        # Act
        actual_result = cut.tokenise(input_val)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_string_of_one_items_with_spaces_result_list_of_one_item_no_spaces(self):
        # AAA in testing - Arrange, Act, Assert
        # Arrange
        input_val = " csharp "
        expected_result = ["csharp"]
        cut = StringTokeniser() # Class Under Test

        # Act
        actual_result = cut.tokenise(input_val)

        # Assert
        self.assertEqual(expected_result, actual_result)

    def test_string_of_compound_items_with_no_result_list_of_many_items(self):
        # AAA in testing - Arrange, Act, Assert
        # Arrange
        input_val = "java byte code,csharp,python"
        expected_result = ["java byte code", "csharp", "python"]
        cut = StringTokeniser() # Class Under Test

        # Act
        actual_result = cut.tokenise(input_val)

        # Assert
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()
