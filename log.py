#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'yunusekmekci'

import re

ac = open("test.log", "r")
satir = ac.readlines()
urldict = {}
urllist = []
encok = []
zaman = []
a = 0
b = 0
i = 0
end = 0
begin = 0
max2 = 0
urlTime = {}

# Toplam URL Sayısı

for i in satir:
    if re.search("GET|HEAD|POST|DELETE|PUT|OPTIONS", i):
        a = a + 1

#Farklı URL Sayısı

for i in range(len(satir)):
    if ('HTTP' in satir[i]):
        if('"GET' in satir[i]):
            begin = int(satir[i].index('"GET')+5)

        elif('"HEAD' in satir[i]):
            begin = int(satir[i].index('"HEAD')+6)

        elif('"POST' in satir[i]):
            begin = int(satir[i].index('"POST')+6)

        elif('"PUT' in satir[i]):
            begin = int(satir[i].index('"PUT')+5)

        elif('"DELETE' in satir[i]):
            begin = int(satir[i].index('"DELETE')+8)

        elif('"OPTIONS' in satir[i]):
            begin = int(satir[i].index('"OPTIONS')+9)

# En Çok Ziyaret Edilen URL

        end = int(satir[i].index(' HTTP'))
        url = satir[i][begin:end]
        urllist.append(url)
        urldict[url] = urldict.get(url, 0)+1
        row = satir[i].split(' ')
        uTime = row[-1]

        if uTime > urlTime.get(url,0):
			urlTime[url] = uTime

    else:
        begin = 0
        end = 0

    urllist.append(satir[i][begin:end])

dsurl = list(set(urllist))
mtcu = max(urlTime,key=urlTime.get)

# Yüklenme Süresi

zaman2 = []

for i in range(len(satir)):
    temp2 = satir[i]

    begin2 = int(satir[i].index('~')+2)
    end2 = (len(satir[i])-1)

    if('~' in temp2):
        zaman.append(temp2[begin2: end2])

print "\n"
print "Toplam URL Sayısı: " + str(a)
print "Farklı URL Sayısı: " + str(len(dsurl))
print "En Çok Ziyaret Edilen URL: ", max(urldict, key=urldict.get)
print "En Uzun Süreye Sahip URL: "+mtcu
print "Yüklenme Süresi: " +max(zaman)
print "\n"
