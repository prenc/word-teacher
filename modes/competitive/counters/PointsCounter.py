class PointsCounter:
    MAX_POINTS_FOR_LETTER = 100
    ROUND_PENALTY = 0.2  # percentage
    TIME_FOR_ONE_LETTER = 250  # milliseconds
    BRAIN_LAG = 1000  # milliseconds
    MINIMAL_SCORED_POINTS = 20

    def __init__(self):
        self._points_sum = 0
        self._last_scored_points = 0

    def correct_answer(self, time, round_no, translation):
        word_length = len(translation)
        elapsed_time = round(time * 1000)

        if elapsed_time < self.BRAIN_LAG:
            elapsed_time = self.BRAIN_LAG

        elapsed_time_for_letter = (elapsed_time - self.BRAIN_LAG) / word_length
        print(elapsed_time_for_letter)

        points_correct_answer = int(
            self.MAX_POINTS_FOR_LETTER
            * (self.TIME_FOR_ONE_LETTER - elapsed_time_for_letter)
            / self.TIME_FOR_ONE_LETTER
            * word_length
        )
        if points_correct_answer < self.MINIMAL_SCORED_POINTS:
            points_correct_answer = self.MINIMAL_SCORED_POINTS
        self._last_scored_points = int(
            points_correct_answer * (1 - (round_no - 1) * self.ROUND_PENALTY)
        )
        self._points_sum += self._last_scored_points

    def last_scored_points(self):
        return f"{self._last_scored_points}"

    def points_info(self):
        return f" Collected points: {self._points_sum}"

    def points_summary(self):
        return f"Your score: {self._points_sum}"
