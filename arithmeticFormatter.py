def arithmetic_arranger(dat, solve=False):
	if len(dat) > 5: return("Error: Too many problems.")
	data = []
	for each in dat:
		values = each.split()
		try:
			maxlen = max(len(values[0]),len(values[2]))
			if maxlen>4: return("Error: Numbers cannot be more than four digits.")
			if values[1] not in {"+","-"}: return("Error: Operator must be '+' or '-'.")
			else: data.append(tuple(values+[str(eval(each))]+[maxlen]))
		except:
			return("Error: Numbers must only contain digits.")

	v1  = "    ".join(a.rjust(l+2)         for a,s,b,an,l in data)
	v2  = "    ".join(s+b.rjust(l+1)       for a,s,b,an,l in data)
	das = "    ".join(("-"*(l+2)).ljust(l) for a,s,b,an,l in data)
	ans = "    ".join(an.rjust(l+2)        for a,s,b,an,l in data)
	solution = (v1+'\n'+v2+'\n'+das) if solve == False else (v1+'\n'+v2+'\n'+das+'\n'+ans)
	return(solution)

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))