b=[]
c=[]
a=str(input("輸入一字元為:"))
for i in range(len(a)):
    c.append(a[i])
    b.append(a[i])
b.reverse()
if b==c:
    print("Yes")
elif b!=c:
    print("NO")