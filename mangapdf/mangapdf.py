# -*- coding:utf-8 -*-
import os
import tempfile


def _get_ext(filename):
    return os.path.splitext(filename)[1]


def _list_img_files(pic_dir: str):
    return [os.path.join(pic_dir, f) for f in os.listdir(pic_dir)
            if (_get_ext(f) in {'.bmp', '.jpg', '.png'})]


def _generate_pdf(src, dest):
    return NotImplemented


def _generate_pdf_files(root_dir, img_file_paths):
    # os.path.basename('/ho/hoa.pdf') >> 'hoa.pdf'
    # os.path.basename('/foo/bar') >> 'bar'
    dest_paths = [os.path.join(root_dir, os.path.basename(img_file_path))
                  for img_file_path in img_file_paths]

    for src, dest in zip(img_file_paths, dest_paths):
        _generate_pdf(src, dest)


def _concat_pdf(filename, pdf_files, dest):
    return NotImplemented


def run(args):

    img_file_paths = _list_img_files(args.pic_dir)
    #  tempfile.mkdtemp()
    #  >> '/var/folders/j0/g25lzk_x7c7dcx7vs6dxs8jh0000gq/T/tmpz57kl7ze'
    temp_dir = tempfile.mkdtemp()
    _generate_pdf_files(temp_dir, img_file_paths)

    pdf_filename = args.filename if args.filename else \
        os.path.basename(args.pic_dir)

    _concat_pdf(pdf_filename, os.listdir(temp_dir), pdf_filename)
