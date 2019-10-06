from collections import Counter
from typing import Tuple


class MistakenWordsTracker:
    def __init__(self):
        self.global_mistaken_words = []
        self.mistaken_words_in_round = []

    def new_round(self):
        self.global_mistaken_words.extend(self.mistaken_words_in_round)
        self.mistaken_words_in_round.clear()

    def add_mistake(self, mistaken_words: Tuple[str, str]):
        self.mistaken_words_in_round.append(mistaken_words)

    def get_words_for_the_next_round(self):
        return self.mistaken_words_in_round

    def most_often_mistaken_words(self):
        mistaken_words_by_amount = dict(Counter(self.global_mistaken_words))
        most_common_mistakes = []
        for words, count in mistaken_words_by_amount.items():
            if count > 1:
                most_common_mistakes.append(
                    f"{words[0]} - {words[1]}  has been mistaken {count} times.\n"
                )
        if most_common_mistakes:
            return (
                f"There are words that you should revise:\n"
                f"{most_common_mistakes}"
            )
        else:
            return ""
