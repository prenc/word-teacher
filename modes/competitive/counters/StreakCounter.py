class StreakCounter:
    def __init__(self):
        self._streak_count = 0

    def finish_streak(self):
        self._streak_count = 0

    def increment_streak(self):
        self._streak_count += 1

    def strike_info(self):
        if self._streak_count > 1:
            return f"({self._streak_count} in a row)"
        else:
            return ''
