#!/usr/bin/env python3
import argparse
import random
import time
from collections import Counter


class StreakCounter:
    def __init__(self):
        self._streak_count = 0

    def wrong_answer(self):
        self._streak_count = 0

    def correct_answer(self):
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


class TimeCounter:
    def __init__(self):
        self.program_start_time = time.time()
        self.start_time = 0
        self.elapsed_time = 0
        self.counted_times = []

    def start(self):
        self.start_time = time.time()

    def end(self):
        self.elapsed_time = time.time() - self.start_time
        self.counted_times.append(self.elapsed_time)
        return self.elapsed_time

    def info(self):
        return f"{self.elapsed_time:.2f}s"

    def game_stats(self):
        return (
            f'Time Stats:\n'
            f'Average time for correct answer: {sum(self.counted_times) / len(self.counted_times):.2f}s\n'
            f'Quickest correct answer: {min(self.counted_times):.2f}s\n'
            f'Longest correct answer: {max(self.counted_times):.2f}s\n'
            f'It took you {time.time() - self.program_start_time:.2f}s to get all the answers'
        )


class PointsCounter:
    MAX_POINT_AMOUNT = 10

    def __init__(self):
        self.points_sum = 0

    def correct_answer(self, time, round):
        self.points_sum += time + round
        pass

    def info(self):
        return f'{self.points_sum}'

    def points_summary(self):
        pass


class ItalianTutor:
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


def parse_arguments():
    parser = argparse.ArgumentParser(description="Give some words.")
    parser.add_argument("file", type=str)
    parser.add_argument(
        "--shuffle", "-s", action="store_true", help="Shuffle output"
    )
    parser.add_argument(
        "--start", "-st", default=0, dest="START_VALUE", type=int
    )
    parser.add_argument("--amount", "-a", default=5, dest="HOW_MANY", type=int)
    parser.add_argument(
        "--pre_shuffle", "-pe", action="store_true", help="Shuffle input"
    )
    parser.add_argument(
        "--test", "-t", action="store_true", help="Print translated words"
    )
    parser.add_argument(
        "--source", action="store_true", help="only source words"
    )
    parser.add_argument(
        "--learn", "-l", action="store_true", help="Learning mode"
    )

    return parser.parse_args()


def parse_words_from_file(parsed_args):
    with open(parsed_args.file, "r") as file:
        lines = file.readlines()

    if parsed_args.pre_shuffle:
        random.shuffle(lines)

    lines = lines[
            parsed_args.START_VALUE: parsed_args.START_VALUE
                                     + parsed_args.HOW_MANY
            ]

    return {
        " ".join(line.split()[:-1]).lower(): line.split()[-1].lower()
        for line in lines
    }


def main():
    parsed_args = parse_arguments()

    parse_words_from_file(parsed_args)
    source_to_translated = parse_words_from_file(parsed_args)

    output = [
        f"{key} {value}\n".lower()
        for key, value in source_to_translated.items()
    ]

    if parsed_args.shuffle:
        random.shuffle(output)

    if parsed_args.learn:
        ItalianTutor(source_to_translated).learn()

    if parsed_args.test:
        output = source_to_translated.values()
    elif parsed_args.source:
        output = source_to_translated.keys()

    print("".join(output), end="")


if __name__ == "__main__":
    main()
