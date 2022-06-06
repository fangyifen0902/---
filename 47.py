dict={}
a=int(input("請輸入筆數n:"))
for i in range(0,a):
    b=(input("請輸入獎牌名稱及數量:"))
    c=b.split(" ")
    dict[c[0]]=int(c[1])
    item1=list(dict.items())
for key,value in item1:
    print("%s牌得到%d面"%(key,value))