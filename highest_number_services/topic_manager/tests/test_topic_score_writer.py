import unittest
from unittest.mock import Mock, call

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

    def test_verify_topic_score_details_not_written(self):
        # Arrange
        top_scores = [] # Empty list to simulate no scores!

        mock_file_writer = Mock()
        cut = TopicScoreWriter(mock_file_writer)

        # Act
        cut.write_scores(top_scores)

        # Assert
        mock_file_writer.write_line.assert_not_called()

    def test_verify_topic_score_details_written_out_multiple_times(self):
        # Arrange
        physics = "Physics"
        art = "Art"
        comp_sci = "Comp Sci"

        physics_result = "Physics, 89"
        art_result = "Art, 87"
        comp_sci_result = "Comp Sci, 97"

        top_scores = [
            TopicTopScore(physics, 89),
            TopicTopScore(art, 87),
            TopicTopScore(comp_sci, 97),
        ]

        mock_file_writer = Mock()
        cut = TopicScoreWriter(mock_file_writer)

        # Act
        cut.write_scores(top_scores)

        # Assert
        expected_calls = [
            call.write_line(physics_result),
            call.write_line(art_result),
            call.write_line(comp_sci_result)
        ]
        mock_file_writer.write_line.assert_has_calls(expected_calls, any_order=False)
        self.assertEqual(mock_file_writer.write_line.call_count, 3)



if __name__ == "__main__":
    unittest.main()