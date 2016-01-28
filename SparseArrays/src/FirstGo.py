'''
Created on 28 Jan 2016

@author: chris
'''


counts = {}

for _ in input():
    strIn = raw_input().strip()
    try:
        counts[strIn] += 1
    except KeyError:
        counts[strIn] = 1
        
for _ in input():
    strComp = raw_input().strip()
    print counts(strComp)
