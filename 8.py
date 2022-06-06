a=(input("輸入第一行正整數為:"))
b=(input("第二行中數列中的數字為:"))
c=b.split(" ")
d=[]
f=[]
if a in b :
        for i in range(len(c)):
                d.append(c[i])
        for j in range(len(d)):
                if d[j] in b :
                        e=d.count(d[j])
                        f.append(e)
        if min(f)==max(f):
                print("每個數字剛好只出現1次")
        else:
                for i in range(len(d)):
                        if max(f)==f[i]:
                                ans=d[i]
                print("最大出現次數為:",ans)
                print("出現次數:",max(f))