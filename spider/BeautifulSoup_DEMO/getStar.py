#!/usr/bin/env python
#-*- coding: utf8 -*-

from urllib2 import urlopen,URLError
from bs4 import BeautifulSoup
#from BeautifulSoup import BeautifulSoup
from mysql.common import MySQLCurd
import MySQLdb
# print ord('A')
# print ord('Z')
baseUrl = 'http://data.ent.sina.com.cn/star/index.html?&tpl=0&dpc=1'
#baseUrl = 'http://www.mingxing.com/zimu/'

def main():
    allStarDict = dict()
    print "Start..."

    for x in range(97, 123, 1):
        nameList = list()

        letter = chr(x)
        searchUrl = '%s%s' % ( baseUrl, letter )

        try:
            print "Get %s name-index stars..." % letter

            hd = urlopen(searchUrl, timeout = 60)
            content = hd.read()
            # turn gb2312 code to unicode
            # content = content.decode('gb2312')

            contentSoup = BeautifulSoup(content)
            print contentSoup
            nameListSoup = contentSoup.find("div",{"class":"main"})
            print "nameListSoup--->",nameListSoup


            #nameListSoup = contentSoup.find('div',{'class': 'oldnum'}).findAll('li')

            if len(nameListSoup) > 0:
                for star in nameListSoup:
                    starInfo = star.find('a')
                    starName = starInfo.string
                    starHref = starInfo['href']
                    nameList.append([starName, starHref])

                allStarDict[letter] = nameList
            print "Get %s name-index stars successfully, and the count is %d.\n" % (letter, len(nameList))

        except URLError, e:
            print e
            print "Get %s name-index stars failed.\n" % letter
            continue

    allStarList = list()
    for item in allStarDict.items():
        allStarList += item[1]

    print "There are %d stars we have got." % len(allStarList)
    print "---Endding---"
    return allStarDict, allStarList

if __name__ == '__main__':
    starData = main()

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
    for item in starData[0].items():
        index = item[0]
        for x in item[1]:
            insertData.append((x[0], x[1], index))

    sql = '''INSERT INTO `kk_star`(`name`, `href`, `index`) VALUES (%s, %s, %s)'''
    m.executemany(sql, insertData)
