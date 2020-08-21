from collections import Counter

string = 'abba'
n = len(string)


def anagrampairs(string, count=0):
	dic = Counter(string)
	
	for i in range(2,n):
		for j in range(0,n-i+1):
			dic[''.join(sorted(string[j:j+i]))]+=1
			# print(frozenset(string[j:j+i]))
	print(dic)

	for k,v in dic.items():
		count += v*(v-1)//2
	print(count)

anagrampairs(string)