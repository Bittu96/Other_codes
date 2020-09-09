a = '1 2 3'
a = list(map(int,a.split()))
n = len(a)
swaps = 0
for i in range(n-1):
	for j in range(i+1,n):
		if a[i]>a[j]:
			temp = a[i]; a[i]=a[j]; a[j]=temp; swaps+=1;print(a[i],a[j])
print(a)
print(swaps)