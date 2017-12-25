# -*- coding: UTF-8 -*-

import sys
from datetime import datetime
import MongoUtil
import FileUtil


def main(resources_file_path, base_url, scratch_func):
    old_data = FileUtil.read(resources_file_path)
    new_data = scratch_func(base_url, old_data)
    if new_data:
        date_new_data = "//" + datetime.now().strftime('%Y-%m-%d') + "\n" + "\n".join(new_data) + "\n"
        FileUtil.append(resources_file_path, date_new_data)
        MongoUtil.insert(resources_file_path, date_new_data)
    else:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '----', getattr(scratch_func, '__name__'), ": nothing to update ")
