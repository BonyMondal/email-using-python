n,k=map(int,input().split(" "))
a=list(map(int,input().split(" ")))
b=[]
for i in range(len(a)):
   # print(a[i])
    if a[i]//2:
        d=a[i]//2
       #   print(d)
        b.append(d)
print(sum(b))
        