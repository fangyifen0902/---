c=[]
s=str(input("請輸入英文句子:"))
a=s.split(" ")
for i in range(len(a)):
    c.append(a[i])
c.reverse()   
print(c)