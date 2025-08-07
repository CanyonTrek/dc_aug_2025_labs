import unittest
from unittest.mock import Mock

from topic_top_score import TopicTopScore
from topic_score_writer import TopicScoreWriter


class TestTopicScoreWriter(unittest.TestCase):
    def test_verify_topic_score_writer_written_out_once(self):
        # Arrange
        physics = "Physics"
        expected_result = "Physics, 89"
        top_scores = [TopicTopScore(physics, 89)]

        mock_file_writer = Mock()
        cut = TopicScoreWriter(mock_file_writer)

        # Act
        cut.write_scores(top_scores)

        # Assert
        mock_file_writer.write_line.assert_called_once_with(expected_result)

if __name__ == "__main__":
    unittest.main()