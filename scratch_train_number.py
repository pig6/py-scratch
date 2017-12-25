#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import bs4
import json
import MainUtil

resources_file_path = '/resources/train/trainNameList.ini'
scratch_url = 'http://www.59178.com/checi/'


def scratch_train_number(scratch_url, old_trains):
    new_trains = []
    resp = requests.get(scratch_url)
    data = resp.text.encode(resp.encoding).decode('gb2312')
    soup = bs4.BeautifulSoup(data, "html.parser")
    a_trains = soup.find('table').find_all('a')
    for train in a_trains:
        if train.text not in old_trains and train.text:
            new_trains.append(train.text)
    return new_trains


if __name__ == '__main__':
    MainUtil.main(resources_file_path, scratch_url, scratch_train_number)
