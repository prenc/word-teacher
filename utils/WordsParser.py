import random


class WordsParser:
    def parse(self, args):
        with open(args.file, "r") as file:
            lines = file.readlines()

        if args.pre_shuffle:
            random.shuffle(lines)

        lines = lines[args.START_VALUE : args.START_VALUE + args.HOW_MANY]

        source_to_translated = {
            " ".join(line.split()[:-1]).lower(): line.split()[-1].lower()
            for line in lines
        }

        return source_to_translated
