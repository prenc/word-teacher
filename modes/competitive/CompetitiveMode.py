import random
from collections import Counter

from modes.competitive.counters.PointsCounter import PointsCounter
from modes.competitive.counters.StreakCounter import StreakCounter
from modes.competitive.counters.TimeCounter import TimeCounter


class CompeteMode:
    def __init__(self, words_pairs):
        self.words = list(words_pairs.items())
        self.round_num = 0
        self.words_count = len(self.words)
        self.progress = 0
        self.percentage = 0
        self.hardest_words = []
        self.sc = StreakCounter()
        self.tc = TimeCounter()
        self.pc = PointsCounter()

    def learn(self):
        print("Begin learning by providing a translation to subsequent words.")
        while len(self.words):
            self.do_round()
        exit()

    def do_round(self):
        random.shuffle(self.words)
        self.round_num += 1
        mistaken_words = []
        for source, translation in self.words:
            self.get_and_evaluate_answer(mistaken_words, source, translation)
        self.evaluate_progress(mistaken_words)
        self.print_finish_round_message()
        self.words = mistaken_words

    def get_and_evaluate_answer(self, mistaken_words, source, translation):
        self.tc.start()
        answer = input(f"{translation}: ").lower().strip()
        if (
                answer == source.translate(str.maketrans("àìòéèù", "aioeeu"))
                or source == answer
        ):
            self.tc.end()
            self.sc.correct_answer()
            print(self.sc.strike_info() + " " + self.tc.info())
        else:
            mistaken_words.append((source, translation))
            self.hardest_words.append((source, translation))
            self.sc.wrong_answer()
            print(f"Nope, correct is {source}")

    def evaluate_progress(self, mistaken_words):
        self.progress = self.percentage
        self.percentage = round(
            (1 - len(mistaken_words) / self.words_count) * 100
        )
        self.progress = self.percentage - self.progress

    def print_finish_round_message(self):
        if self.percentage != 100:
            print(
                f"You guessed {self.percentage}%(+{self.progress}) words. "
                f"Let's proceed to round {self.round_num + 1}!"
            )
        else:
            print(self.get_ending_message(self.hardest_words), end='')

    def get_ending_message(self, hardest_words):
        counted_mistakes = dict(Counter(hardest_words))
        most_common_mistakes = []
        for words, count in counted_mistakes.items():
            if count > 1:
                most_common_mistakes.append(
                    f"{words[0]} - {words[1]}  Mistaken {count} times."
                )
        most_common_mistakes = "\n".join(most_common_mistakes)
        if most_common_mistakes:
            revise_words = (
                f"\nThere are words that you should revise:\n"
                f"{most_common_mistakes}"
            )
        else:
            revise_words = ""
        return (
            f"That's the end. It took you {self.round_num} rounds to translate "
            f"{self.words_count} words. You can do better :P"
            f"{revise_words}"
            f"\n{self.tc.game_stats()}"
        )
