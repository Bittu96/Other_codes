'''
Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
Structure is like below:
|  |
|_|
We can trap 2 units of water in the middle gap.



Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. Each test case contains an integer N denoting the size of the array, followed by N space separated numbers to be stored in array.

Output:
Output the total unit of water trapped in between the blocks.

Constraints:
1 <= T <= 100
3 <= N <= 107
0 <= Ai <= 108

Example:
Input:
2
4
7 4 0 9
3
6 9 9

Output:
10
0

Explanation:
Testcase 1: Water trapped by block of height 4 is 3 units, block of height 0 is 7 units. So, total unit of water trapped is 10 units.
'''


#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
import time
start_time = time.time()
#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL

s = '8 8 2 4 5 5 1'
s = '7 4 0 9'
s = '1 1 5 2 7 6 1 4 2 3'

s = list(map(int,s.split()))
n = len(s)

lmax = [s[0]]
rmax = [s[-1]]
for i in range(1,n):
	lmax.append(max(lmax[-1], s[i]))
	rmax.append(max(rmax[-1], s[-i-1]))
print(lmax,rmax)
rmax=rmax[::-1]
tw=0
for i in range(n):
	# lmax = max(s[:i+1])
	# rmax = max(s[i:])
	# print(s[:i+1],s[i:])
	wb = min(lmax[i],rmax[i])
	w = wb - s[i]
	tw+=w
print(tw)


# for i in range(1,n):
#     if s[i]>a[-1]: a.append(s[i])
#     else: a.append(a[-1])
#     if s[-i-1]>b[-1]: b.append(s[-i-1])
#     else: b.append(b[-1])
# print(a,b)
# print(sum([-s[i]+min(a[i],b[::-1][i]) for i in range(n) ]))


#TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
print("--- %ls seconds ---" % (time.time() - start_time))
#LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
