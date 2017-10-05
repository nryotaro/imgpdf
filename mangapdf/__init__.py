from mangapdf.main import run
from mangapdf.parser import build_parser
import sys


__all__ = ['main']


def main():
    """Entry point for the app"""
    parser = build_parser()
    parsed = parser.parse_args(sys.argv[1:])
    run(parsed)
