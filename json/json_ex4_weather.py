#!/usr/bin/python
#-*- coding:utf-8 -*-

import sys
import codecs

class Weather(object):
    def __init__(self,data):
        data=data['weatherinfo']
        self.city=data['city']
        self.id=data['cityid']
        self.date=' '.join([data['date_y'],data['week']])
        self.week=data['week'];
        t1= ''.join([data['temp1'],data['weather1']])
        t2= ''.join([data['temp2'],data['weather2']])
        t3= ''.join([data['temp3'],data['weather3']])
        t4= ''.join([data['temp4'],data['weather4']])
        t5= ''.join([data['temp5'],data['weather5']])
        t6= ''.join([data['temp6'],data['weather6']])

        self.weather=[t1,t2,t3,t4,t5,t6]
        self.suggest=data['index_d']
        self.original=data
    def report(self):
        weekstr=[u'星期一',u'星期二',u'星期三',u'星期四',u'星期五',u'星期六']
        max=len(weekstr)
        print "max=",max,
        if self.week in weekstr:
            print "true->星期---"
            #找出元素的位置
            w_index=weekstr.index(self.week)
            print "w_index=",w_index,
        #days=[u'今天',u'明天',u'后天',u'大后天']
        print ' '
        print self.city,self.date
        print '-'*26
        print max-w_index
        for i in range(max-w_index):
            #print days[i] + u': '+self.weather[i]
            print weekstr[i] + u': '+self.weather[i]
        print '-'*26
        print self.suggest
def get_cityid(city=None):
    import urllib2
    if city==None:
        id_url="http://61.4.185.48:81/g/"
        id_data=urllib2.urlopen(id_url)
        city_rid=id_data.readline().split(';')[1].split('=')[1]
    else:
        idfile=open('city_allid.txt','r')
        for line in idfile:
            line = line.decode('gbk').encode('utf-8')
            print line
            if city in line:
                city_id=line.split('=')[0]
                break
            else:
                city_id=None
        if city_id==None:
            raise ValueError('City Name Incorrect!')

        #判断city_id中是否有换行符
        if '\r\n' in city_id:
            print "true"
            #city_rid=city_id.replace('\r\n','')
            city_rid=city_id.rstrip();
            print "city_rid=",city_rid
        else:
            city_rid=city_id
    return city_rid

def get_weather(city_id):
    import json
    import urllib2
    ids=str(city_id)
    print ids
    base_url='http://m.weather.com.cn/data/'
    city_url=base_url+ids+'.html'
    print city_url
    try:
        print "data_return,ready..."
        data_return=urllib2.urlopen(city_url)
        print "data_return=",data_return
    except urllib2.URLError:
        raise ValueError('City id not correct!')
    weather_data=[i for i in data_return]
    #print weather_data
    data=json.loads(weather_data[0])
    #print data
    output=Weather(data)
    return output


def Report(city="Local"):
    if city=="Local":
        city_id=get_cityid()
        weather_data=get_weather(city_id)
        weather_data.report()
    else:
        print "city=",city,
        #city=city.decode('gbk').encode('utf-8')
        print "encode city=",city
        city_id=get_cityid(city)
        weather_data=get_weather(city_id)
        weather_data.report()

if __name__=="__main__":
    if len(sys.argv) ==1:
        print "len==1"
        import time
        Report()
        time.sleep(5)
        sys.exit(0)
    else:
        print "len!=1"
        print sys.argv[1:]
        for city in sys.argv[1:]:
            Report(city)
