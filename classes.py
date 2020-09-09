from collections import deque

class Solution:

	def __init__(self):
		self.stack = []
		self.queue = deque([])
		print('an instance is created')

	def pushCharacter(self, val):
		self.stack.append(val)

	def enqueCharacter(self, val):
		self.queue.append(val)

	def popCharacter(self):
		return self.stack.pop()

	def dequeueCharacter(self):
		return self.queue.popleft()

	def printds(self):
		print('stack', self.stack)
		print('queue',self.queue)

s = 'bittttib'
l = len(s)
obj = Solution()

for i in range(l):
	obj.pushCharacter(s[i])
	obj.enqueCharacter(s[i])

isPalindrome=True
obj.printds()

for i in range(l//2):
	if (obj.popCharacter() != obj.dequeueCharacter()): isPalindrome = False; break
	else: continue

obj.printds()

print('The word {} {} a palindrome'.format(s,'is' if isPalindrome==True else 'is not'))















'''

class Calculator:
	def __init__(self):
		print('an instance is created')
		pass

	def power(self, n, p):
		try:
			if n < 0 or p<0:
				raise Exception
			else:
				print(n**p)
		except:
			print('n and p should be non-negative')


myCalculator = Calculator()
a,b = 2,-5
myCalculator.power(a,b)















class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:{} {} \nID: {}".format(self.lastName,self.firstName, self.idNumber))

class Student(Person):
	def __init__(self, firstName, lastName, idNumber, scores):
		super().__init__(firstName, lastName, idNumber)
		#(or) person().__init__(self, firstName, lastName, idNumber)
		self.scores = list(map(int,scores.split()))
	def grade(self):
		self.Score = sum(self.scores)//len(self.scores)
		O = range(90,101)
		E = range(80,91)
		A = range(70,81)
		P = range(55,71)
		D = range(40,56)
		T = range(0,41)
		
		if self.Score in O: self.grad = 'O'
		elif self.Score in E: self.grad = 'E'
		elif self.Score in A: self.grad = 'A'
		elif self.Score in P: self.grad = 'P'
		elif self.Score in D: self.grad = 'D'
		#else self.Score in T: self.grad = 'T'
		else: self.grad = 'T'
		print("Grade: {}\n".format(self.grad))


person1 = Person('Mrudul', 'Katla', 905416)
person1.printPerson()
print('\n')

stud1 = Student('MK','Prince', 123, '100 200')
stud1.printPerson()
stud1.grade()

stud2 = Student('Sancho', 'Panza', 4847677, '41 42 43 44 45 46 48')
stud2.printPerson()
stud2.grade()


















from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super().__init__(title,author)
        self.price = price
    def display(self):
        print('Title: {} \nAuthor: {} \nPrice: {}'.format(self.title,self.author,self.price) )


new_novel=MyBook('My Autography','Me',100)
new_novel.display()

















class Employee:
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.first = first
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Mrudul', 'Katla', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())

'''