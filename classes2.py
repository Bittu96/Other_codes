import math 
from math import sqrt


class AdvancedArithmetic(object):
	print('AA instance created')
	
	def divisorSum(n):
		raise NotImplementedError


class Calculator(AdvancedArithmetic):
	print('Calculator istance created')
	
	def divisorSum(self, n):
		self.n = int(sqrt(n))+1
		self.summ = 0 
		for i in range(1,self.n): 
			if n%i==0: self.summ+=(( i+(n//i) , i) [ i==(n//i) ])
			print(i,n//i)
		print(self.summ)



my_calculator = Calculator()
my_calculator.divisorSum(16)

# list(map(my_calculator.divisorSum, [2,5,8]))