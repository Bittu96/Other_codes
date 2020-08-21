def fill(i,j):
	n,k=3,1
	ms = [[0,0,0],[0,0,0],[0,0,0]]
	while k<10:
		if i>=n: i=0
		if i<=-1: i=n-1
		if j>=n: j=0
		if j<=-1: j=n-1
		if ms[i][j]!=0: i+=1;j-=2
		else: ms[i][j]=k;i-=1;j+=1;k+=1
	return ms
#print([fill(i,j) for i in range(3) for j in range(3)])


'''
n = 98
s = '7 12 13 19 17 7 3 18 9 18 13 12 3 13 7 9 18 9 18 9 13 18 13 13 18 18 17 17 13 3 12 13 19 17 19 12 18 13 7 3 3 12 7 13 7 3 17 9 13 13 13 12 18 18 9 7 19 17 13 18 19 9 18 18 18 19 17 7 12 3 13 19 12 3 9 17 13 19 12 18 13 18 18 18 17 13 3 18 19 7 12 9 18 3 13 13 9 7'
s = list(map(int,s.split()))
print(([(s[i],s[i-1]) for i in range(1,n) if abs(s[i]-s[i-1])<=1]))  
'''

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def calculate(self, scores, firstname, lastname):
    	print(scores)
    	self.score = 10 


    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here


line = 'Heraldo Memelli 8135627'.split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = 2 # not needed for Python
scores = list( map(int, '100 80'.split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())