'''
Solving the hackerrank puzzle 2D Arrays - DS

https://www.hackerrank.com/challenges/2d-array

Using a generator to produce an iterable that makes
array indicies. First for me in anger.

----------------------

You are given a 2D array with dimensions 6*6. An hourglass in an array is defined as a portion shaped like this:

a b c
  d
e f g
For example, if we create an hourglass using the number 1 within an array full of zeros, it may look like this:

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
Actually, there are many hourglasses in the array above. The three topmost hourglasses are the following:

1 1 1     1 1 0     1 0 0
  1         0         0
1 1 1     1 1 0     1 0 0
The sum of an hourglass is the sum of all the numbers within it. The sum for the hourglasses above are 7, 4, and 2, respectively.

In this problem, you have to print the largest sum among all the hourglasses in the array.

Note: If you have already solved the problem "Java 2D array" in the data structures chapter of the Java domain, you may skip this challenge.

Input Format

There will be exactly 6 lines of input, each containing 6 integers separated by spaces. Each integer will be between -9 and 9, inclusively.

Output Format

Print the answer to this problem on a single line.

----------------------

Created on 28 Jan 2016

@author: chris
'''
import copy

def genInds():
    
    baseInds = []
    for j in [0,2]:
        for i in range(3):
            baseInds.append([j,i])
    baseInds.append([1,1])
    
    for j in range(4):
        for i in range(4):
            opInds = copy.deepcopy(baseInds)
            for k in range(len(opInds)):
                opInds[k][0] += j
                opInds[k][1] += i
            yield opInds

arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

hrSums = []
for inds in genInds():
    hrSum = 0
    for j, i in inds:
        hrSum += arr[j][i]    
    hrSums.append(hrSum)
print max(hrSums)
