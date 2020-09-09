# string = 'asasd'
#7 

string = 'abcbaba'
#10 

# string = 'aaaa'
#10

def substrCount(s, count=0):
	for i in range(len(s)):
		for j in range(i,len(s)):
			# print(s[i],s[j],s[i:j+1])
			# print(s[i:j],s[j],s[j+1:j+1+(j-i)])
			# print('-------------')
			if s[i]==s[j]:
				count+=1
			else:
				print('-------------')
				if s[i:j]==s[j+1:j+1+(j-i)]:
					count+=1
				else:
					pass
				break
			# else:
			# 	try:
			# 		s[j+1+(j-i)-1]
			# 		print('-------------')


			# 		if s[i:j]==s[j+1:j+1+(j-i)]:
			# 			count+=1
			# 	except:
			# 		pass
			# 	break
	return count

print(substrCount(string))

