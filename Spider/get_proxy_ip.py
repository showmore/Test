#encoding=utf8  
import requests
from bs4 import BeautifulSoup  
import urllib  
import socket  
  
User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'  
header = {}  
header['User-Agent'] = User_Agent  
 

''''' 
获取所有代理IP地址 
'''  
def getProxyIp():  
    proxy = []  
    for i in range(1,5):  
        url = 'http://www.xicidaili.com/nn/'+str(i)
        req = requests.get(url,headers=header)
        soup = BeautifulSoup(req.text, "html.parser")
        ips = soup.findAll('tr') 
        for x in range(1,len(ips)):  
            ip = ips[x]  
            tds = ip.findAll("td")  
            ip_temp = tds[5].contents[0]+'://'+tds[1].contents[0]+":"+tds[2].contents[0]
            proxy.append(ip_temp)  

    return proxy

''''' 
验证获得的代理IP地址是否可用 
'''  
def validateIp(proxy):  
    url = "http://ip.chinaz.com/getip.aspx"  
    f = open("E:\\ip.txt","w")  
    socket.setdefaulttimeout(3)  
    for i in range(0,len(proxy)):  
        try:  
            ip = proxy[i].strip().split("\t")  
            proxy_host = "http://"+ip[0]+":"+ip[1]  
            proxy_temp = {"http":proxy_host}  
            res = urllib.urlopen(url,proxies=proxy_temp).read()  
            f.write(proxy[i]+'\n')  
            print(proxy[i])
        except:  
            continue  
    f.close()  
  
              
if __name__ == '__main__':  
    for i in getProxyIp():
        print(i)
     