import testData
from collections import Counter
arr = '1 2 2 4'
arr = '1 3 9 9 27 81'
# arr = '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'

# arr = testData.test2
arr = list(map(int, arr.split()))
r = 3

def countTriplets(arr, r, count=0):
	right_map, left_map = Counter(arr), Counter()
	for i in arr:
		ir, ri = i*r, i//r
		right_map[i]-=1
		if right_map[ir] and left_map[ri] and not i%r: count += left_map[ri]*right_map[ir]
		left_map[i]+=1
	return count


# 1339347780085 exp
# 8040276546818

# 2325652489 exp
# 6482935397
#dhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh

# from collections import Counter

# def countTriplets(arr, r):
#     a = Counter(arr)
#     b = Counter()
#     s = 0
#     for i in arr:
#         j = i//r
#         k = i*r
#         a[i]-=1
#         if b[j] and a[k] and not i%r:
#             s+=b[j]*a[k]
#         b[i]+=1
#     return s

print(countTriplets(arr, r))