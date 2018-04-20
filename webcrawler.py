import os
import re
import requests
import urllib2
from bs4 import BeautifulSoup

def filterLivedIds(url):
    '''extract livedIds from the inital webpage    	
    '''
    html = urllib2.urlopen(url)
    liveIds = set()
    content = BeautifulSoup(html,"html.parser")
    for link in content.findAll("a",href=re.compile("^(/l/)")):
	if 'href' in link.attrs:
	    newPage = link.attrs['href']
	    liveId = re.findall("[0-9]+",newPage)
	    liveIds.add(liveId[0])
    return liveIds

def getUserIds(liveId):
    ''' get user id from live id
    '''
    html = urllib2.urlopen("http://www.huajiao.com/" + "l/" + str(liveId))
    content = BeautifulSoup(html,"html.parser")
    text = content.title.get_text()
    res = re.findall("[0-9]+",text)
    if 0 == len(res):
	return 0
    else:
	return res[0]

def getUserData(userId):
    html = urllib2.urlopen("http://www.huajiao.com/user/" + str(userId))
    bsObj = BeautifulSoup(html,"html.parser")
    data = dict()
    try:
	userInfoObj = bsObj.find("div", {"id":"userInfo"})
        data['FAvatar'] = userInfoObj.find("div", {"class": "avatar"}).img.attrs['src']
        data['FUserId'] = re.findall("[0-9]+", userId)[0]
        tmp = userInfoObj.h3.get_text('|', strip=True).split('|')
        data['FUserName'] = tmp[0]
        data['FLevel'] = tmp[1]
        tmp = userInfoObj.find("ul", {"class":"clearfix"}).get_text('|', strip=True).split('|')
        data['FFollow'] = tmp[0]
        data['FFollowed'] = tmp[2]
        data['FSupported'] = tmp[4]
        data['FExperience'] = tmp[6]
	return data
    except AttributeError:
	print(str(userId) + ": html parse error in getUserId.")
	return 0

class BoseModel(Model):
    conn = Mysql(host='127.0.0.1', unix_socket='/var/lib/mysql/mysql.sock', user='root', passwd='123456', db='wanghong', charset='utf8')

class User(BoseModel):
    tbl = "Tbl_Huajiao_User"

class Live(BoseModel):
    tbl = "Tbl_Huajiao_Live"

if __name__ == "__main__":
    website = "http://www.huajiao.com/category/1000"
    liveIds = filterLivedIds(website)
    for liveId in liveIds:
	userId =  getUserIds(liveId)
	print getUserData(userId)
