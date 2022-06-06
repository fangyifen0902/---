total=0
a=input("請輸入五張牌:")
b=a.split(" ")
for i in range(len(b)):
    if b[i]=="A":
        b[i]=1
    elif b[i]=="J":
        b[i]=11
    elif a[i]=="Q":
        b[i]=12
    elif b[i]=="K":
        b[i]=13
    total=total+int(b[i])
print(total)
