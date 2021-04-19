from random import randint

equation = ''
n = 6
sign = lambda x: '-' if x<0 else '+'

def term(c,p):
    s = f"{sign(c)} " if p!=n-1 else '-' if c<0 else ''
    print(c)
    c = '' if (abs(c)==1 and p!=0) else abs(c)
    x = 'x' if p>0 else ''
    p = f"^{p}" if p>1 else ''
    return f"{s}{c}{x}{p} "


for p in range(n-1,-1,-1):
    c = randint(-n,n)
    if c != 0:
        equation += term(c,p)

print(equation)
