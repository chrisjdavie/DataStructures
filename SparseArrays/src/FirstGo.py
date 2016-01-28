'''
Created on 28 Jan 2016

@author: chris
'''


counts = {}

for _ in range(input()):
    strIn = raw_input().strip()
    try:
        counts[strIn] += 1
    except KeyError:
        counts[strIn] = 1
        
for _ in range(input()):
    strComp = raw_input().strip()
    try:
        print counts[strComp]
    except KeyError:
        print 0
