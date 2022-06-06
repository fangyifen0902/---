M=int(input("小明身上有幾元:"))
N=int(input("飲料有幾種:"))
ans=0
if M>=0 and M<=100:
    if N>=1 and N<=30:
        for i in range(N):
            p=int(input(""))
            if p>=10 and p<=50:
                if M>=p:
                    ans+=1
                else:
                    ans+=0
        print(ans)