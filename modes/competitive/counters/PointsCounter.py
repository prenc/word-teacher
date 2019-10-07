class PointsCounter:
    MAX_POINT_AMOUNT = 10

    def __init__(self):
        self.points_sum = 0

    def correct_answer(self, time, round_no):
        self.points_sum += time + round_no
        pass

    def info(self):
        return f"{self.points_sum}"

    def points_summary(self):
        return f"You scored {self.points_sum}"
