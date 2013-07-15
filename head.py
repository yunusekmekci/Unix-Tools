# -*- coding: utf-8 -*-

__author__ = 'yunusekmekci'

import sys
from sys import argv

if(len(sys.argv) == 2):
    ad = sys.argv[1]
    sayi = 10

elif(len(sys.argv) == 4):
    ad = sys.argv[3]
    sayi = 100

ac = open(ad)
satir = ac.readlines()

for i in range(sayi):
    print(satir[i])