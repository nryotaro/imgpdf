# -*- coding: utf-8 -*-
import argparse as ap


def build_parser() -> ap.ArgumentParser:
    parser = ap.ArgumentParser('mangapdf')
    parser.add_argument('pic_dir', metavar='PIC_DIR',
                        help='directory which includes pictures')
    parser.add_argument(
        'filename',
        metavar='FILENAME',
        help='the output filename',
        default=None,
        nargs='?')
    return parser
