n=int(input("請輸入n:"))
k=int(input("請輸入k:"))
b=0
if k>1:
    a=n//k
    if a>=k:
        b=a//k
print("Peter可以抽",n+a+b,"支紙菸")