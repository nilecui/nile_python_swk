#!/bin/env python
#coding:utf-8

import os,sys,re
import re,time

class PyAnsy:
    author = 'dream.people'

    def Now(self):
        return "%04d/%02d/%02d %02d:%02d" % time.localtime()[:5]

    def GetFile(self,filename):
        _lines = []
        if filename == '':
            while True:
                _line = sys.stdin.readline()
                if _line == '':
                    break
                _lines.append(_line)
        else:
            _lines = open(filename,"r").readlines()

        return _lines

    def ClassComment(self):
        line = self.GetFile('')[0]
        if line == '':
            return

        g = re.match("^( *)class  *([^(:]*).*",line)
        if g == None:
            print line
            return

        blank,classname = g.groups()
        blank += "    "
        comment = blank + '"""\n'
        comment += blank + '@author     :    %s\n' % self.author
        comment += blank + 'comment     :    \n'
        comment += blank + 'create date :    %s\n' % self.Now()
        comment += blank + '-----------------------------------------\n'
        comment += blank + 'modify date :    \n'
        comment += blank + '@author     :    \n'
        comment += blank + 'reason      :    \n'
        comment += blank + '"""'

        print line.rstrip()
        print comment

    def FuncComment(self):
        line = self.GetFile('')[0]
        if line == '':
            return

        g = re.match("^( *)def  *([^(]*)\(([^)]*)\).*",line)
        if g == None:
            print line
            return

        blank,fname,params = g.groups()
        params = params.split(",")
        blank += "    "
        comment = blank + '"""\n'
        comment += blank + '@author     :    %s\n' % self.author
        comment += blank + 'comment     :    \n'
        comment += blank + 'parameter   :    \n'
        for param in params:
            comment += blank + '    %s - \n' % param
        comment += blank + 'return value:    \n'
        comment += blank + 'create date :    %s\n' % self.Now()
        comment += blank + '-----------------------------------------\n'
        comment += blank + 'modify date :    \n'
        comment += blank + '@author     :    \n'
        comment += blank + 'reason      :    \n'
        comment += blank + '"""'

        print line.rstrip()
        print comment


ansy = PyAnsy()
if len(sys.argv) < 2:
    print """命令行: pyTool option [filename]
    选项:
        -func 添加函数备注
"""

    sys.exit(-1)

flag = sys.argv[1]

if len(sys.argv) != 3:
    filename = ''
else:
    filename = sys.argv[2]

if flag == '-func':
    ansy.FuncComment()
elif flag == '-class':
    ansy.ClassComment()
else:
    sys.exit(-1)
