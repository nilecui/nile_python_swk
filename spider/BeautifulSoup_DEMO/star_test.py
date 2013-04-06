#!/usr/bin/python
#-*- coding:utf-8 -*-
#****************************************************
#         Author: nile cui - nile.cui@gmail.com
#  Last modified: 2013-04-02 15:14
#       Filename: star_test.py
#    Description:
#****************************************************

from urllib2 import urlopen,URLError,Request,build_opener
#from bs4 import BeautifulSoup
from BeautifulSoup import BeautifulSoup
from mysql.common import MySQLCurd
import MySQLdb
import chardet
baseUrl = 'http://data.ent.sina.com.cn/star/index.html'

def get_star():
    print "Start..."

    nameList = list()
    try:
        req=Request(baseUrl)
        req.add_header=("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
        req.add_header=('User-Agent','Mozilla/5.0 (Windows NT 5.1; rv:19.0) Gecko/20100101 Firefox/19.0')
        opener=build_opener()
        res=opener.open(req)
        content=res.read()
        res.close()

        contentSoup = BeautifulSoup(content)
        new_url=""

        for frame in contentSoup.findAll("iframe"):
            if "starlist.php?&dpc=1" in frame["src"]:
                new_url=frame["src"]

        star_burl="http://data.ent.sina.com.cn/star/"
        ul=star_burl+new_url
        req1=Request(ul)
        new_html=urlopen(req1).read()

        # convert gb2312 code to unicode
        unew_html = new_html.decode('gbk')

        # convert unicode code to utf-8 for insert to mysql
        utf8_html =unew_html.encode('utf-8','ignore')

        iframesoup=BeautifulSoup(utf8_html)

        nameListSoup = iframesoup.findAll('li')
        if len(nameListSoup) > 0:
            for star in nameListSoup:
                #抓取明星名字
                starInfo = star.find('a')
                starName = starInfo.string

                #抓取明星对应的url
                starHref = star_burl+starInfo['href']
                nameList.append([starName, starHref])
    except URLError, e:
        print e

    print "There are %d stars we have got." % len(nameList)
    print "---Endding---"
    return nameList

if __name__ == '__main__':
    starData = get_star()
    print type(starData)
    print type(starData[0])
    print type(starData[1])

    # connect mysql database
    conn = MySQLdb.connect(
        host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = 'cwtnqwjx',
        db = 'caiji',
        charset = 'utf8'
    )

    m = MySQLCurd(conn)
    insertData = list()
    for x in starData:
        insertData.append((x[0], x[1]))

    sql = '''INSERT INTO `kk_star`(`name`, `href`) VALUES (%s, %s)'''
    m.executemany(sql, insertData)
