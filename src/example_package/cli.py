from dataclasses import dataclass
from . import counts
import argparse


@dataclass
class ProgArguments():
    sum: list[int]
    add_two: int


def parse_args() -> ProgArguments:
    parser = argparse.ArgumentParser(
                    prog='Example Package',
                    description='Package description... can be loaded from README.md')

    parser.add_argument('--sum', nargs="+", help='sum all integers', type=int)
    parser.add_argument('--add_two', nargs="?", help='add two to a number', type=int)

    args = parser.parse_args()
    
    if not args.sum and not args.add_two:
        parser.print_help()
        exit(1)

    return ProgArguments(**vars(args))


def main():
    args = parse_args()
    if args.sum is not None:
        print(counts.sum_all(args.sum))
    if args.add_two is not None:
        print(counts.add_two(args.add_two))
