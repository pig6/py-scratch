#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import bs4
import random
import MainUtil

resources_file_path = '/resources/train/trainStationNameList.ini'
scratch_url = 'http://www.smskb.com/train/'


def scratch_train_station(scratch_url, old_stations):
    new_stations = []
    provinces_eng = (
        "Anhui", "Beijing", "Chongqing", "Fujian", "Gansu", "Guangdong", "Guangxi", "Guizhou", "Hainan", "Hebei",
        "Heilongjiang", "Henan", "Hubei", "Hunan", "Jiangsu", "Jiangxi", "Jilin", "Liaoning", "Ningxia", "Qinghai",
        "Shandong", "Shanghai", "Shanxi", "Shanxisheng", "Sichuan", "Tianjin", "Neimenggu", "Xianggang", "Xinjiang",
        "Xizang",
        "Yunnan", "Zhejiang")
    provinces_chi = (
        "安徽", "北京", "重庆", "福建", "甘肃", "广东", "广西", "贵州", "海南", "河北",
        "黑龙江", "河南", "湖北", "湖南", "江苏", "江西", "吉林", "辽宁", "宁夏", "青海",
        "山东", "上海", "陕西", "山西", "四川", "天津", "内蒙古", "香港", "新疆", "西藏",
        "云南", "浙江")
    for i in range(0, provinces_eng.__len__(), 1):
        cur_url = scratch_url + provinces_eng[i] + ".htm"
        resp = requests.get(cur_url)
        data = resp.text.encode(resp.encoding).decode('gbk')
        soup = bs4.BeautifulSoup(data, "html.parser")
        a_stations = soup.find('left').find('table').find_all('a')
        for station in a_stations:
            if station.text not in old_stations:
                new_stations.append(provinces_chi[i] + ',' + station.text)
    return new_stations


if __name__ == '__main__':
    MainUtil.main(resources_file_path, scratch_url, scratch_train_station)
