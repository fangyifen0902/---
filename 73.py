a=input("請輸入時間1(時:分:秒):")
b=int(input("請輸入時間2(秒):"))
c=a.split(":")
f=b//60//60
g=(b-(f*60*60))//60
h=(b-(f*60*60))%60
for i in range(len(c)):
    if i==0:
        d=int(c[i])*60*60
        i+=1
    if i==1:
        e=int(c[i])*60
        i+=1
    if i==2:
        print("時間1(",a,")格式轉換為",d+e+int(c[i]))
        print("時間2(",b,"秒)=",str(f)+":"+str(g)+":"+str(h))
        break
        