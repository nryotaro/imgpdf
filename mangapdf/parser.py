# -*- coding: utf-8 -*-
import argparse as ap


def build_parser() -> ap.ArgumentParser:
    parser = ap.ArgumentParser('mangapdf')
    parser.add_argument('picuture', metavar='PIC_DIR',
                        help='directory which includes pictures')
    return parser
