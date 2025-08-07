class TopicTopScore:
    def __init__(self, topic_name, score):
        self._topic_name = topic_name
        self._top_score = score

    def get_topic_name(self):
        return self._topic_name

    def get_top_score(self):
        return self._top_score
