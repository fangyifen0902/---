M=int(input("請輸入階層值M:"))
a=1
i=1
while(a<M):
    i=i+1
    a=a*i
print("超過M為",M,"的最小階層N值為:",i)