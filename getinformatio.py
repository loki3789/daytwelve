import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
fhand=open("sample.txt",'r')

for l1 in fhand:
    html = urllib.request.urlopen(l1, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    lst1 = soup1.find_all('p')
    for i in lst1:
        print(i)
    print("=========================================================================================================")
