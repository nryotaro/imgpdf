# -*- coding:utf-8 -*-
import os
import tempfile
import PIL.Image as Image
from PyPDF2 import PdfFileMerger
import progressbar


def _resolve_path(path):
    return os.path.expanduser(os.path.expandvars(path))


def _get_ext(filename):
    return os.path.splitext(filename)[1]


def _list_img_files(pic_dir: str):
    resolved_path = _resolve_path(pic_dir)
    return [os.path.join(resolved_path, f) for f in os.listdir(resolved_path)
            if (_get_ext(f) in {'.bmp', '.jpg', '.png'})]


def _to_pdf_path(root_dir, filepath):
    name, _ = os.path.splitext(os.path.basename(filepath))
    return os.path.join(root_dir, name + ".pdf")


def _generate_pdf(img_file_paths, dest):
    merger = PdfFileMerger()
    with open(dest, 'wb') as output_f, \
        progressbar.ProgressBar(max_value=len(img_file_paths) * 2) as bar, \
            tempfile.TemporaryDirectory() as temp_dir:
        bar_status = 0
        temp_pdf_paths = [
            _to_pdf_path(temp_dir, path) for path in img_file_paths]

        for img_path, pdf_path in zip(img_file_paths, temp_pdf_paths):
            with Image.open(img_path) as f:
                f.save(pdf_path)
                bar_status += 1
                bar.update(bar_status)

        pdf_fs = [open(f, 'rb') for f in temp_pdf_paths]
        for f in pdf_fs:
            merger.append(f)
            bar_status += 1
            bar.update(bar_status)
            merger.write(output_f)
        for f in pdf_fs:
            f.close()


def _generate_pdf_files(root_dir, img_file_paths):
    # os.path.basename('/ho/hoa.pdf') >> 'hoa.pdf'
    # os.path.basename('/foo/bar') >> 'bar'
    dest_paths = [os.path.join(root_dir, os.path.splitext(
        os.path.basename(img_file_path))[0] + ".pdf")
                  for img_file_path in img_file_paths]

    for src, dest in zip(img_file_paths, dest_paths):
        _generate_pdf(src, dest)


def _concat_pdf(filename, pdf_files, dest):
    return NotImplemented


def run(args):
    """
    TODO
         Implement unittests
    """
    img_file_paths = _list_img_files(args.pic_dir)
    #  tempfile.mkdtemp()
    #  >> '/var/folders/j0/g25lzk_x7c7dcx7vs6dxs8jh0000gq/T/tmpz57kl7ze'

    pdf_filename = args.filename if args.filename else \
        os.path.basename(args.pic_dir) + '.pdf'

    _generate_pdf(img_file_paths, _resolve_path(pdf_filename))
