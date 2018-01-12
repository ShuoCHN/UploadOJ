import urllib.request,requests


url="https://weibo.com/u/5201691099/home"
cookie_weibo ="SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFkAsl10l1fTJM2uq.6-j3g5JpX5KMhUgL.Fo-Eeh2c1K271K.2dJLoIEBLxK.LB.BL1K5LxK-LBonL1hzLxKnLBo-LBo-LxKMLBK2L1K-t; SCF=ArsiecUGtbZMnw6ioxqGmVjL9yMmqocGQo4OYmIeEKUotqUZSupo3N3ZE8a7doNQGVxhC81iD1FcOLBoBKAdYyY.; SUHB=079jfnFn88-4Rn; ALF=1544969702; un=18204623356; wvr=6; wb_timefeed_5201691099=1; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; SUB=_2A253MVozDeRhGeNM61MX-S_MwjWIHXVUR8z7rDV8PUNbmtAKLVbVkW9NTliJsxo90ctMiQZp3QCH5FWdLpojdKn0; SSOLoginState=1513433702; TC-V5-G0=b8dff68fa0e04b3c8f0ba710d783479a; TC-Page-G0=b1761408ab251c6e55d3a11f8415fc72"

cookies = {}

for each in cookie_weibo.split(";"):
    key,value = each.split("=",1)
    cookies[key]=value

#print(cookies)

b = requests.get(url, cookies=cookies)

a =b.content.decode("utf8")
print(a)
