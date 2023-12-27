# coding:utf-8


import os
import time

from .error import NotPathError, FormatError, NotFileError

def timestamp_to_string(timestamp):
    time_obj = time.localtime(timestamp)
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time_obj)
    return time_str
def check_file(file_path):
    if not os.path.exists(file_path):
        raise NotPathError('not found %s' % file_path)

    if not file_path.endswith('.json'):
        raise FormatError('not a JSON file')

    if not os.path.isfile(file_path):
        raise NotFileError('%s is not a file' % file_path)
