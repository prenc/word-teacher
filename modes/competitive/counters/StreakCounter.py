class StreakCounter:
    def __init__(self):
        self._streak_count = 0

    def finish_streak(self):
        self._streak_count = 0

    def increment_streak(self):
        self._streak_count += 1

    def strike_info(self):
        if self._streak_count < 2:
            return "Correct!"
        elif self._streak_count > 10:
            return f"Holy SHIT! ({self._streak_count} in a row)"
        elif self._streak_count > 5:
            return f"Good! ({self._streak_count} in a row)"
        else:
            return f"Correct! ({self._streak_count} in a row)"
