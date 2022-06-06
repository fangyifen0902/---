a=input("請輸入A的好友:")
b=input("請輸入B的好友:")
c=a.split(" ")
d=b.split(" ")
e=0
for i in range(len(c)):
    for j in range(len(d)):
        if c[i]==d[j]:
            e+=1
print(e)