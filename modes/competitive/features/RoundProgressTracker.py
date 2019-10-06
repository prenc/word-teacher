class RoundProgressTracker:
    def __init__(self, word_count):
        self.word_count = word_count

        self.progress = 0
        self.percentage = 0

    def _evaluate_progress(self, progressed_words):
        self.progress = self.percentage
        self.percentage = round(
            (1 - len(progressed_words) / self.word_count) * 100
        )
        self.progress = self.percentage - self.progress

    def progress_info(self, words):
        self._evaluate_progress(words)
        progress = f"(+{self.progress}%)" if self.progress else ""

        return f"You have guessed {self.percentage}%{progress} words so far.\n"
