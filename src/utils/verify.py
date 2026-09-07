from cgshop2027_pyutils.io import read_instance, read_solution
from cgshop2027_pyutils.verify import check_for_errors

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("sol", type=Path)
    args = parser.parse_args()

    errors = check_for_errors(
        read_instance(args.input),
        read_solution(args.sol),
    )

    print(f"=== got {len(errors)} errors ===", *errors, sep="\n")


if __name__ == "__main__":
    main()
