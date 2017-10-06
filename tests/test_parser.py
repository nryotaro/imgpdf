# -*- coding: utf-8 -*-
from mangapdf.parser import build_parser


def test_build_parser():
    parser = build_parser()

    d = 'd'
    parsed = parser.parse_args([d])

    assert parsed.pic_dir == d
    assert not parsed.filename
    
