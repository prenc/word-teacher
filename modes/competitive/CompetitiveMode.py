import random

from modes.competitive.counters.PointsCounter import PointsCounter
from modes.competitive.counters.RoundCounter import RoundCounter
from modes.competitive.counters.StreakCounter import StreakCounter
from modes.competitive.counters.TimeCounter import TimeCounter
from modes.competitive.features.MistakenWordsTracker import (
    MistakenWordsTracker,
)
from modes.competitive.features.RoundProgressTracker import (
    RoundProgressTracker,
)


class CompeteMode:
    def __init__(self, words_pairs):
        self.words = list(words_pairs.items())
        self.word_count = len(self.words)
        self.sc = StreakCounter()
        self.tc = TimeCounter()
        self.pc = PointsCounter()
        self.rc = RoundCounter()
        self.mwt = MistakenWordsTracker()
        self.rpt = RoundProgressTracker(self.word_count)

    def play(self):
        print("Begin learning by providing a translation to subsequent words.")
        while len(self.words):
            self._do_round()
        print(self._game_finish_message(), end="")
        exit()

    def _do_round(self):
        self.rc.new_round()
        self.mwt.new_round()

        random.shuffle(self.words)
        for source, translation in self.words:
            self._get_and_evaluate_answer(source, translation)

        self.words = self.mwt.get_words_for_the_next_round()

        self._print_finish_round_message()

    def _get_and_evaluate_answer(self, source, translation):
        self.tc.start_counting()
        answer = input(f"{translation}: ").lower().strip()
        if answer.translate(
            str.maketrans("àìòéèù", "aioeeu")
        ) == source.translate(str.maketrans("àìòéèù", "aioeeu")):
            elapsed_time = self.tc.stop_counting()
            self.pc.correct_answer(elapsed_time, self.rc.round_number, source)
            self.sc.increment_streak()
            message = (
                "\033[1;32m ✔ \033[0m"
                + self.sc.strike_info()
                + " "
                + self.tc.info()
                + " +"
                + self.pc.last_scored_points()
            )
        else:
            self.sc.finish_streak()
            self.mwt.add_mistake((source, translation))
            message = f"\033[1;31m ✘ \033[0m➜ {source}"
        print(message)

    def _print_finish_round_message(self):
        if len(self.words):
            print(
                self.rpt.progress_info(self.words)
                + self.rc.round_info()
                + self.pc.points_info()
            )

    def _game_finish_message(self):
        return (
            self.rc.rounds_sumamry()
            + f"{self.word_count} words. You can do better :P\n"
            + self.mwt.most_often_mistaken_words()
            + self.tc.time_stats()
            + self.pc.points_summary()
        )
