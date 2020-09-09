'''
Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5.
It simply allows to test a condition in a single line replacing the multiline if-else making the code compact.
'''
# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
# (if_test_false,if_test_true)[test]
print( (b, a) [a < b] )

# Use Dictionary for selecting an item
print({True: a, False: b} [a < b])

# lamda is more efficient than above two methods
# because in lambda  we are assure that
# only one expression will be evaluated unlike in
# tuple and Dictionary
print((lambda: b, lambda: a)[a < b]())



# n = str(257)
# print(sum([int(n[i]) for i in range(len(str(n)))]))
# import math
# from math import log
# print(math.log(10))

# a = 3
# b = 60

# x = int(a**(log(b)//log(a)))
# y = int(a**(1 + log(b)//log(a)))
# # print(x,y)
# # print(b-x)
# # print( (x,y)[(x-b)>(y-b)])

# print( ('nuuu','yay') [3>5])


# a = range(90,101)
# print(89 in a)
# print(90 in a)
# print(100 in a)
# print(101 in a)

# def myfunc(*a):
#     print(*a)


# dict_vec = {'we': 3, 'y': 2, 'z': 1}

# myfunc(*dict_vec)
# print(*dict_vec)


# def fizzbuzz(num):
#     # return ( (num,'buzz')[num%5==0], ('fizz','fizzbuzz')[num%5==0] )[num%3==0]

#     # if num%5==0:
#     #     if num%3==0:
#     #         return 'fizzbuzz'
#     #     else: 
#     #         return 'buzz'
#     # else: 
#     #     if num%3==0:
#     #         return 'fizz'
#     #     else:
#     #         return num

#     # if num%5==0: return 'fizzbuzz' if num%3==0 else 'buzz'
#     # else: return 'fizz' if num%3==0 else num

#     return 'fizzbuzz' if num%5==0 if num%3==0 else 'buzz'
#     else: return 'fizz' if num%3==0 else num

# print([fizzbuzz(i) for i in range(1,16)])



# def fibonacci(num, a=0, b=1):
#     for i in range(num):
#         yield(a)
#         a,b = b, a+b
# print(list(fibonacci(10)))



# print((False, True)[4>2])

# for _ in range(int(input())):
#     n,d = map(int,input().split())
#     s = list(map(int,input().split()))
#     for i in range(0,n,d):
#       s[i:i+d] = s[i:i+d][::-1] 
#     print(*s)





# f = frozenset
# print(f('aab')==f('ba'))
# print(not 16%8)