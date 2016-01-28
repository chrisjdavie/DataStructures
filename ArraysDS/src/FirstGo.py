'''
Sovling the hackerrank Arrays-DS puzzle.

https://www.hackerrank.com/challenges/arrays-ds

Print the reverse of an array in Python

Created on 28 Jan 2016

@author: chris
'''

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

for a in arr[::-1]: print a,