# -*- coding: utf-8 -*-

# #####################################
# @Author: Feyiz135
# @Time: 2017-05-09
# #####################################

import filecmp
import os


def remove_file(dir, base_dir):
    """比对标准目录下的文件/子目录并删除多余的文件/子目录"""
    obj = filecmp.dircmp(dir, base_dir)
    if obj.right_only:
        print("It needs these files:")
        for right in obj.right_only:
            print(right)
    for file in obj.left_only:
        path = dir + '/' + file
        _remove(path)


def _remove(path):
    """删除文件或者目录"""
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        sub = os.listdir(path)
        for file in sub:
            path_sub = path + '/' + file
            _remove(path_sub)
        os.rmdir(path)

if __name__ == "__main__":
    remove_file("G:/SVN/FJ1.0.4.20170508.B", "G:/SVN/FJ1.0.3.20170427.B")
