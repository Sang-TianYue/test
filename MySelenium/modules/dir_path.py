# coding:utf-8

from os import path
def dir_path():
    file_path = path.dirname(__file__)
    return path.dirname(file_path)

