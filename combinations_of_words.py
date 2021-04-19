# arr = '1 2 2 4'
# arr = '0 8 9 12 17 21'
arr = '0 1 2 3 5 7 13 17 19 19'

triplets = []
arr = sorted(map(int, arr.split()))
k = 22
l,r = 0,len(arr)-1

i = 0
while l<=r and i<100:
	i+=1
	if l==r:
		l=0
		r-=1
	else:
		lval,rval = arr[l],arr[r] 
		m = k-lval-rval
		print(arr[l],m,arr[r])
		if m in arr[l:r]:
			triplets.append((arr[l],m,arr[r]))
		l+=1

print(triplets)