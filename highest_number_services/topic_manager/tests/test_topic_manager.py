import unittest

import os
import sys

#mpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app"))
#sys.path.insert(0, mpath)

from topic_manager.app.topic_manager import TopicManager
from topic_manager.app.topic_scores import TopicScores
from topic_manager.app.topic_top_score import TopicTopScore

class StubHighestNumberFinder:
    def find_highest_number(self, numbers):
        return 89 # Always RETURNS expected value for TESTING


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

    def test_find_highest_score_with_list_of_one_returns_list_of_one(self):
        # Arrange
        scores = [56, 67, 43, 89]
        topic_name = "Physics"
        topic_scores = [TopicScores(topic_name, scores)]
        expected_result = [TopicTopScore(topic_name, 89)]
        cut = TopicManager()

        # Act
        actual_result = cut.find_topic_high_scores(topic_scores)

        # Assert
        self.assertEqual(expected_result[0].get_topic_name(), actual_result[0].get_topic_name())
        self.assertEqual(expected_result[0].get_top_score(), actual_result[0].get_top_score())

    def test_find_highest_score_with_list_of_one_topic_using_stub(self):
        # Arrange
        scores = [56, 67, 43, 89]
        topic_name = "Physics"
        topic_scores = [TopicScores(topic_name, scores)]
        expected_result = [TopicTopScore(topic_name, 89)]

        hnf_stub = StubHighestNumberFinder()
        cut = TopicManager(hnf_stub)

        # Act
        actual_result = cut.find_topic_high_scores(topic_scores)

        # Assert
        self.assertEqual(expected_result[0].get_topic_name(), actual_result[0].get_topic_name())
        self.assertEqual(expected_result[0].get_top_score(), actual_result[0].get_top_score())


    def test_find_highest_score_with_list_of_many_returns_list_of_many_using_stub(self):
        # Arrange
        physics_scores = [56, 67, 43, 89]
        art_scores = [87, 66, 78]
        compsci_scores = [45, 88, 97, 56]

        topic_scores = [
            TopicScores("Physics", physics_scores),
            TopicTopScore("Art", art_scores),
            TopicTopScore("Comp Sci", compsci_scores)
        ]

        expected_result = [
            TopicScores("Physics", 89),
            TopicTopScore("Art", 89),
            TopicTopScore("Comp Sci", 89)
        ]

        hnf_stub = StubHighestNumberFinder()
        cut = TopicManager(hnf_stub)

        # Act
        actual_result = cut.find_topic_high_scores(topic_scores)

        # Assert
        for i in range(len(expected_result)):
            self.assertEqual(expected_result[i].get_topic_name(), actual_result[i].get_topic_name())
            self.assertEqual(expected_result[i].get_top_score(), actual_result[i].get_top_score())


if __name__ == "__main__":
    unittest.main()