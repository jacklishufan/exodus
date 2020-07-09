import requests
from pyquery import PyQuery as pq
from html import unescape
from rest_api.utils import *
import re
import hashlib

WATCH = '5df33d56a53e8812d783328d4704ac0e89bd6ab9cfef1fd2d2cba0f5b84b13a7'

def get_html(url):
    return unescape(requests.get(url).content.decode('utf-8'))

def update():
    html_root = unescape(requests.get('https://www.mofa.go.jp/p_pd/ipr/page7e_900126.html').content.decode('utf-8'))
    doc = pq(html_root)
    host = 'https://www.mofa.go.jp'
    url = host + doc('h2:contains(COVID-19)').find('a').attr.href
    data = get_html(url)
    return pq(data)('#contents').text()


def get_countries(d):
    continent = ['Asia', 'Oceania', 'North America', 'Middle East', 'Europe', 'Africa','Latin America and the Caribbean']
    countries = [x for x in
                 re.compile('denied to enter Japan.*countries or regions\.([^(\(2))]*)\(2\)').findall(d)[0].split('\n')
                 if x and x not in continent]
    tgt = []
    for i in [x.split(',') for x in countries]:
        for j in i:
            tgt.append(j.strip())
    return tgt

def main():
    data = update()
    hash = hashlib.sha256('898oaFs09f'.encode('utf8'))
    hash.update(data.encode('utf-8'))
    hid = hash.hexdigest()
    if hid == WATCH:
        print("NO CHANGE")
        return
    countries = get_countries(data)
    country_codes = []
    ignored = ['Kosovo']
    for i in countries:
        if i not in ignored:
            country_codes.append(get_country_code(i))
    for code in country_codes:
        if 'NOT FOUND' in code:
            print(code)

main()
