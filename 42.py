a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=b**2-4*a*c
if d>0:
    x1=int(((-b)+d**(1/2))/(2*a))
    x2=int(((-b)-d**(1/2))/(2*a))
    print(x1)
    print(x2)
elif d==0:
    x1=(-b)/(2*a)
    print(x1)
else:
    print("無解")