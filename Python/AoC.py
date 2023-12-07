import sys
import argparse

def debug(*a, **kw):
    if args.debug:
        print(*a, **kw, file=sys.stderr)

parser = argparse.ArgumentParser(description="AoC solve")

parser.add_argument(
    "--debug",
    "-d",
    action=argparse.BooleanOptionalAction,
    help="debug mode: verbose printing",
)

args = parser.parse_args()


def parseInts(l, sep=' '):
    return [int(x) for x in l.split(sep)]
