# -*- coding: utf-8 -*-
from mangapdf.main import _list_img_files


def test_list_img_files():
    rootdir = 'tests/test_list_dir'
    
    assert _list_img_files(rootdir) == [f'{rootdir}/a.bmp',
                                        f'{rootdir}/a',
                                        f'{rootdir}/a.jpg',
                                        f'{rootdir}/a.png']
