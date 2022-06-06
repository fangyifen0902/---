dict={}
a=int(input("請輸入筆數n:"))
p=int(input("處理方式(1)(2)"))
if p==2:
    for i in range(a):
        b=input("請輸入獎牌名稱及數量:")
        c=b.split(" ")
        dict[c[0]]=int(c[1])
        item1=list(dict.items())
    for key,value in item1:
        print("%s牌得到%d面"%(key,value))
else:
    for i in range(a):
        a=input("請輸入獎牌名稱及數量(金 4):")
        b=a.split(" ")
        print("%s牌得到%s面"%(b[0],b[1]))