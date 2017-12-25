# -*- coding: UTF-8 -*-

import platform
from pymongo import MongoClient
from datetime import datetime, timedelta, timezone
import conf_dev
import conf_test

# configure Multi-confronment
platform_os = platform.system()
config = conf_dev
if (platform_os == 'Linux'):
    config = conf_test
# mongodb
uri = 'mongodb://' + config.user + ':' + config.pwd + '@' + config.server + ':' + config.port + '/' + config.db_name


# 将数据写入mongodb
# @author chenmc
# @param uri connect to mongodb
# @path save mongodb field
# @data save mongodb field
# @operation save mongodb field default value 'append'
# @date 2017/12/07 16:30
# 先在mongodb中插入一条自增数据 db.sequence.insert({ "_id" : "version","seq" : 1})

def insert(path, data, operation='append'):
    client = MongoClient(uri)
    resources = client.smartdb.resources
    sequence = client.smartdb.sequence
    seq = sequence.find_one({"_id": "version"})["seq"]
    sequence.update_one({"_id": "version"}, {"$inc": {"seq": 1}})
    post_data = {"_class": "com.gionee.smart.domain.entity.Resources", "version": seq, "path": path,
                 "content": data, "status": "enable", "operation": operation,
                 "createtime": datetime.now(timezone(timedelta(hours=8)))}
    resources.insert(post_data)
