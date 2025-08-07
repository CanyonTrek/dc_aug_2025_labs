import unittest

class TestTopicManager(unittest.TestCase):
    def test_find_highest_score_in_empty_list_returns_empty_list(self):
        # Arrange
        scores = []
        expected_result = []
        cut = TopicManager()

        # Act
        actual_result = cut.find_topic_high_scores(scores)

        # Assert
        self.assertEqual(expected_result, actual_result)

if __name__ == "__main__":
    unittest.main()