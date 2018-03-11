#encoding=utf8
import random
import requests

proxy_ip=[]


def validateIp(proxy_ip):
  s = requests.session()
  proxies={}
  f = open("E:\ip.txt","w")
  for i in range(len(proxy_ip)):
    proxies["http"]=proxy_ip[i]
    url ="http://www.xatrm.com"
    try:
      print(url)
      print(proxies)  
      response = s.get(url,proxies=proxies,timeout=5)
      f.write(proxy_ip[i]+'\n')
      print('-'*100)
    except:
      continue
  f.close()

if __name__ == '__main__':
  validateIp(proxy_ip)