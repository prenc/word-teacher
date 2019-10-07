class RoundCounter:
    def __init__(self):
        self.round_number = 0

    def new_round(self):
        self.round_number += 1

    def round_info(self):
        return f"Let's proceed to round {self.round_number + 1}!"

    def rounds_sumamry(self):
        return f"That's the end. It took you {self.round_number} rounds to translate "
