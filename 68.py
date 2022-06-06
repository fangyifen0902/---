a=input("請輸入第一組數字:")
b=input("請輸入第二組數字:")
c=0
d=0
if (len(a)>=2 and len(a)<=6) and (len(b)>=2 and len(b)<=6):
    for i in a:
        for j in b:
            if i==j:
                if a.index(i)==b.index(j):
                    c+=1
                else:
                    d+=1
if c==4 and d==0:
    print(str(c)+"A"+str(d)+"B","全對")
else:
    print(str(c)+"A"+str(d)+"B","加油")