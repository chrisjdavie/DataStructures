'''
Solving the hackerrank Dynamic Array puzzle.

https://www.hackerrank.com/challenges/dynamic-array/submissions/code/16900895

The main pain for me was these types of very precise puzzles - I'm not bad
at doing it, but it rather presses me to pay attention as these things aren't
laid out in a way that's intuative to me.

----------------------

There are N sequences. All of them are initially empty, and you are given a variable lastans=0. You are given Q queries of two different types:

"1 x y" - Insert y at the end of the ((x⊕lastans) mod N)th sequence.
"2 x y" - Print the value of the (y mod size)th element of the ((x⊕lastans) mod N)th sequence. Here, size denotes the size of the related sequence. Then, assign this integer to lastans.
Note: You may assume that, for the second type of query, the related sequence will not be an empty sequence. Sequences and the elements of each sequence are indexed by zero-based numbering.

The ⊕ symbol denotes the xor operation. You can get more information about it from Wikipedia. It is defined as ^ in most of the modern programming languages.

Input Format

The first line consists of N, number of sequences, and Q, number of queries, separated by a space. The following Q lines contains one of the query types described above.

Constraints 
1<=N,Q<=105 
0<=x<=109 
0<=y<=109
Output Format

For each query of type two, print the answer on a new line.

---------------------- 

Created on 28 Jan 2016

@author: chris
'''
def fun0(x,y,ar,lastans):
    ar[(x^lastans)%N].append(y)
    return lastans
 
def fun1(x,y,ar,lastans):
    iAr = (x^lastans)%N
    lastans = ar[iAr][y%len(ar[iAr])]
    print lastans
    return lastans
 
funAr = [ fun0, fun1 ]

N, Q = map(int,raw_input().strip().split())

ar = []
for _ in range(N):
    ar.append([])
lastans = 0

for _ in range(Q):
    iFn, x, y = map(int,raw_input().strip().split())
    lastans = funAr[iFn-1](x,y,ar,lastans)
    
