# -*- coding:utf-8 -*-
import os.path as p
import os


def list_files(pic_dir: str):
    os.listdir(pic_dir)
    # os.path.isfile


def run(args):

    print(list_files(args.pic_dir))
