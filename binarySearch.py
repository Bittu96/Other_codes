# def binarySearch(arr,l,r, value):
# 	if r<1 or r<l: return -1
# 	else:
# 		mid = (l+r)//2
# 		if arr[mid]==value:
# 			return mid
# 		elif arr[mid]>value:
# 			return binarySearch(arr, l, mid-1, value)
# 		else:
# 			return binarySearch(arr, mid+1, r, value)

def binarySearch(arr, value):
	arr = sorted(arr)
	print(arr)
	low = 0
	high = len(arr)-1

	while low<=high:
		mid = (low+high)//2
		if arr[mid]==value:
			return mid
		elif arr[mid]>value:
			high = mid-1
		else:
			low = mid+1
	return -1

money = 5
# arr = '2 2 4 3'
arr = '1 4 5 3 2'
arr = list(map(int,arr.split()))


# arr = list(map(int,arr.split()))
# n = len(arr)
# ind = binarySearch(arr,money)
# print(money if ind!=-1 else -1)

# for i in range(n):
# 	search = binarySearch(arr, money-arr[i])
# 	if search != -1:
# 		print(i+1,arr.index(money-arr[i]+1))
# 		break

# for i in range(n):
# 	search = binarySearch(arr, 0, n-1, money-arr[i])
# 	if search != -1:
# 		print(i+1,search+1)
# 		break

