import argparse


class ArgumentParser:
    def __init__(self):
        self._parser = argparse.ArgumentParser(
            description="Do what you want with words."
        )

    def _add_arguments(self):
        self._parser.add_argument("file", type=str)
        self._parser.add_argument(
            "--shuffle", "-s", action="store_true", help="Shuffle output"
        )
        self._parser.add_argument(
            "--start", "-st", default=0, dest="START_VALUE", type=int
        )
        self._parser.add_argument(
            "--amount", "-a", default=5, dest="HOW_MANY", type=int
        )
        self._parser.add_argument(
            "--pre_shuffle", "-pe", action="store_true", help="Shuffle input"
        )
        self._parser.add_argument(
            "--test", "-t", action="store_true", help="Print translated words"
        )
        self._parser.add_argument(
            "--source", action="store_true", help="only source words"
        )
        self._parser.add_argument(
            "--learn", "-l", action="store_true", default=True, help="Learning mode"
        )

    def parse(self):
        return self._parser.parse_args()
