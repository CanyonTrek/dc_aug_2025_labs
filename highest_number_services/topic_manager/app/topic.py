class Topic:
    def __init__(self, topic_name, score):
        self._topic_name = topic_name
        self._score = score

    def get_topic_name(self):
        return self._topic_name

    def get_score(self):
        return self._score
