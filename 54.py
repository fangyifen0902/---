m=75
a=float(input("請輸入路程公里數(km):"))
b=(a-1.5)*1000%250
c=(a-1.5)*1000//250
if a<1.5:
    print("所需車資為:",int(m))
elif a>1.5 and b==0:
    print("所需車資為:",int(m+(c*5)))
elif a>1.5 and b<250 :
    print("所需車資為:",int(m+5+(c*5)))
elif a>1.5 and b>=250:
    print("所需車資為:",int(m+(c*5)))
