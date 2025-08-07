from file_writer import FileWriter

class TopicScoreWriter:
    def __init__(self, file_writer=None):
        if file_writer is None:
            file_writer = FileWriter()
        self._file_writer = file_writer

    def write_scores(self, top_scores, filename="output.txt"):
        for tts in top_scores:
            data_to_write = f"{tts.get_topic_name()}, {tts.get_top_score()}"
            self._file_writer.write_line(data_to_write)
