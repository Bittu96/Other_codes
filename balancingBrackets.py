from collections import defaultdict

def isBalanced(arr):
    stack=[]
    dict_ = defaultdict(lambda:None, { '[':']', '{':'}', '(':')',  })
    for each in arr:
        if stack and each == dict_[stack[-1]]:
            stack.pop()
        else:
            stack.append(each)
    return ('NO' if stack else 'YES')

string = "{{[[(())]]}}"
# print('\n',string,"-", isBalanced(string))

string = "{(([])[])[]]"
# print('\n',string,"-", isBalanced(string))

string = "{[]{()}}"
print('\n',string,"-", isBalanced(string))
  
string = "[{}{})(]"
print('\n',string,"-", isBalanced(string))
  
string = "((()"
# print('\n',string,"-",isBalanced(string))

print(type(string))