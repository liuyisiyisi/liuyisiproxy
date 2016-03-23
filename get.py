#!/usr/bin/env python
# encoding=utf-8
import requests
from bs4 import BeautifulSoup
import time


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
of = open('proxy.txt' , 'w')

for page in range(1, 100):
    url = 'http://www.xici.net.co/nn/' + str(page)
    html_doc = requests.get(url, headers=headers).content


    soup = BeautifulSoup(html_doc)
    trs = soup.find('table', id='ip_list').find_all('tr')
    for tr in trs[1:]:
        tds = tr.find_all('td')
        ip = tds[2].text.strip()
        print ip
        port = tds[3].text.strip()
        protocol = tds[6].text.strip()
        if protocol == 'HTTP':
            of.write('http://%s:%s\n' % ( ip, port) )
            print '%s:%s' % ( ip, port)
    print page

of.close()