import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import urllib.request
import urllib.parse

values={'q':'Mahabalipuram history'}

data=urllib.parse.urlencode(values)
url='https://www.google.com/search?'+data


headers={}
headers['User-Agent']="Mozilla/5.0 (X11; Linux i686)"

req=urllib.request.Request(url,headers=headers)
resp=urllib.request.urlopen(req)
resp_data=resp.read()

fhand= open("sample.txt",'w')
l1=[]
soup = BeautifulSoup(resp_data, 'html.parser')
lst=soup.find_all("a")
st=re.compile("http.*")
for urlinfetchedata in lst:
    url1=urlinfetchedata.get('href')
    lofurl=re.findall(st,url1)
    for i in lofurl:
        l1.append(i)
#print(l1)
for u in l1:
    if(u.find("webcache")!=-1):
        continue
    if (u.find("google") != -1):
        continue
    if (u.find("blogger") != -1):
        continue
    if (u.find("youtube") != -1):
        continue
    t=u.find("&")
    fhand.write(u[:t]+"\n")




