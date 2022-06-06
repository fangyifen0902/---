a=str(input("輸入一組四位數字為:"))
b=(int(a[0])+7)%10
c=(int(a[1])+7)%10
d=(int(a[2])+7)%10
e=(int(a[3])+7)%10
c,e =e,c
b,d =d,b
print(str(b)+str(c)+str(d)+str(e))