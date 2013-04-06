# -*- coding: utf-8 -*-
__author__ = 'luchanghong'
import time,random,logging
import MySQLdb
log = logging.getLogger(__name__)

class MySQLCurd(object):
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def fetchone(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchone()
        except MySQLdb.Error, e:
            log.debug(e)

    def fetchall(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except MySQLdb.Error, e:
            log.debug(e)

    def numRows(self, sql):
        try:
            return self.cur.execute(sql)
        except MySQLdb.Error, e:
            log.debug(e)

    # info is a dict : key is field
    def insert(self, info, table):
        fields = values = ''
        sql = 'insert into `%s`' % table
        for item in info.items():
            field = '`%s`' % item[0]
            value = u'\'%s\'' % item[1]
            fields = ','.join([fields, field])
            values = ','.join([values, value])
        sql = "%s (%s) values (%s)" % (sql, fields[1:], values[1:])
        self.execute(sql)

    def update(self, info, where, table):
        sql = 'update `%s` set ' % table
        update = list()
        for item in info.items():
            field = '`%s`' % item[0]
            value = u'\'%s\'' % item[1]
            update.append('%s = %s' % (field, value))
        sql += ','.join(update) + where
        self.execute(sql)

    def execute(self, sql):
        try:
            self.cur.execute(sql)
        except MySQLdb.Error, e:
            log.debug(e)
        finally:
            self.conn.commit()

    def executemany(self, sql, info):
        try:
            self.cur.executemany(sql, info)
        except MySQLdb.Error, e:
            log.debug(e)
        finally:
            self.conn.commit()
