import os
import sys

mpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..", "find_highest_number"))
sys.path.insert(0, mpath)

from app.highest_number_finder import HighestNumberFinder
from topic_top_score import TopicTopScore

class TopicManager:
    def __init__(self):
        self._highest_number_finder = HighestNumberFinder()


    def find_topic_high_scores(self, topic_scores_list):
        top_scores = []

        if len(topic_scores_list) == 1:
            ts = topic_scores_list[0]
            top_score = self._highest_number_finder.find_highest_number(ts.get_scores())
            top_scores.append(TopicTopScore(ts.get_topic_name(), top_score))
        return top_scores
