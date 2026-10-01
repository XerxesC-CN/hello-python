"""A tiny Python 3.13 starter program."""

import sys


def main() -> None:
    version = sys.version_info
    print(f"Hello from Python {version.major}.{version.minor}!")


if __name__ == "__main__":
    main()
