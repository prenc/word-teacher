#!/usr/bin/env python3

import random

from modes.competitive.CompetitiveMode import CompeteMode
from utils.ArgumentParser import ArgumentParser
from utils.WordsParser import WordsParser


def main():
    parsed_args = ArgumentParser().parse()
    source_to_translated = WordsParser().parse(parsed_args)

    output = [
        f"{key} {value}\n".lower()
        for key, value in source_to_translated.items()
    ]

    if parsed_args.shuffle:
        random.shuffle(output)

    if parsed_args.learn:
        CompeteMode(source_to_translated).learn()


if __name__ == "__main__":
    main()
