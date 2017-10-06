# -*- coding: utf-8 -*-
from mangapdf.mangapdf import \
    _list_img_files, _get_ext, _generate_pdf_files, _to_pdf_path
from unittest.mock import patch, call


def test_get_ext():
    assert _get_ext('fa.txt') == '.txt'


def test_list_img_files():
    rootdir = 'tests/test_list_dir'

    assert _list_img_files(rootdir) == [f'{rootdir}/a.bmp',
                                        f'{rootdir}/a.jpg',
                                        f'{rootdir}/a.png']


@patch('mangapdf.mangapdf._generate_pdf')
def test_generate_pdf_files(m):
    _generate_pdf_files('foobar/piyo', ['bar/a.png', 'bar/b.png'])

    assert len(m.call_args_list) == 2
    assert m.call_args_list[0] == call('bar/a.png', 'foobar/piyo/a.pdf')
    assert m.call_args_list[1] == call('bar/b.png', 'foobar/piyo/b.pdf')


def test_to_pdf_path():
    assert _to_pdf_path('root_dir', 'foo/bar.png') == 'root_dir/bar.pdf'
