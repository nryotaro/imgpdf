# -*- coding: utf-8 -*-
from mangapdf.main import _list_img_files, _get_ext


def test_get_ext():
    assert _get_ext('fa.txt') == '.txt'


def test_list_img_files():
    rootdir = 'tests/test_list_dir'
    
    assert _list_img_files(rootdir) == [f'{rootdir}/a.bmp',
                                        f'{rootdir}/a.jpg',
                                        f'{rootdir}/a.png']
