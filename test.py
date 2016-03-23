#encoding=utf8
import urllib
import socket
import requests
#socket.setdefaulttimeout(3)
inFile = open('proxy.txt', 'r')
outFile = open('available.txt', 'w')
lines = inFile.readlines()
proxys = []




for i in range(0,len(lines)):
    ip = lines[i].strip("\n")
    proxy_temp = {"http":ip}
    proxys.append(proxy_temp)




headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}
url = "http://host.com"
for proxy in proxys:

    try:
        s = requests.session()
        res = requests.get(url, headers=headers, proxies=proxy, timeout=5)
        if res.status_code == 200:
            outFile.write(proxy['http'] + '\n')

    except Exception,e:
        print proxy
        print e
        continue


inFile.close()
outFile.close()
