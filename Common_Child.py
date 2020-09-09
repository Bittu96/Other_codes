string1 = 'OUDFRMYMAW'
string2 = 'AWHYFCCMQX'

# string1 = 'SHINCHAN'
# string2 = 'NOHARAAA'

def dp(s1,s2, _max = 0):
	s1len, s2len = len(s1), len(s2)
	dpcurr = [0]*(s1len+1)

	for i in range(s2len):
		dptemp=tuple(dpcurr)

		for j in range(s1len):
			if s2[i]==s1[j]:
				dpcurr[j]=1
				dpcurr[j]+=dptemp[j-1]
			else:
				dpcurr[j]=max(dptemp[j],dpcurr[j-1])
			# print(dptemp)
	return dpcurr[-2]

print(dp(string1, string2))