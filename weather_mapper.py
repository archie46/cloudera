#!/usr/bin/env python

import sys

i = 0
max_we = []
max_we_date = []
min_we = []
min_we_date = []
lis = []

for i in range(33):
    ls = []
    cls = []
    emp = []
    for j in range(12):
        ls.append(0)
        cls.append(50)
        emp.append('')
    min_we.append(cls)
    max_we.append(ls)
    min_we_date.append(emp)
    max_we_date.append(emp)

tmax = 0
tmin = 0

for line in sys.stdin:
    row = line.split(',')
    month = int(row[0].split('-')[1])
    year = int(row[0].split('-')[2])
    if row[2] != '':
        tmin = float(row[2])
    else:
        tmin = 502
    if row[3] != '':
        tmax = float(row[3])
    else:
        tmax = 0
    i = year - 1990
    j = month - 1
    if tmax > max_we[i][j]:
        max_we[i][j] = tmax
        max_we_date[i][j] = row[0]
    if tmin < min_we[i][j]:
        min_we[i][j] = tmin
        min_we_date[i][j] = row[0]

for i in range(len(min_we)):
    for j in range(len(min_we[0])):
        print "{0}\t{1}".format(max_we_date[i][j], min_we_date[i][j])
