#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import requests
import bs4
import json
import MainUtil

# 相对路径，也是需要将此路径存入数据库
resources_file_path = '/resources/movie/cinemaNameList.ini'
scratch_url = 'http://theater.mtime.com/China_Beijing/'


# scratch data with define url
def scratch_latest_movies(scratch_url, old_movies):
    data = requests.get(scratch_url).text
    soup = bs4.BeautifulSoup(data, "html.parser")
    new_movies = []
    new_movies_json = json.loads(
        soup.find('script', text=re.compile("var hotplaySvList")).text.split("=")[1].replace(";", ""))
    coming_movies_data = soup.find_all('li', class_='i_wantmovie')
    # 上映的电影
    for movie in new_movies_json:
        move_name = movie['Title']
        if move_name not in old_movies:
            new_movies.append(movie['Title'])
    # 即将上映的电影
    for coming_movie in coming_movies_data:
        coming_movie_name = coming_movie.h3.a.text
        if coming_movie_name not in old_movies and coming_movie_name not in new_movies:
            new_movies.append(coming_movie_name)
    return new_movies


if __name__ == '__main__':
    MainUtil.main(resources_file_path, scratch_url, scratch_latest_movies)
