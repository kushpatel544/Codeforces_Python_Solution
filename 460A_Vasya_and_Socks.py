a=input().split()
n=int(a[0])
m=int(a[1])
c=0
while(n):
    n-=1
    c+=1
    if(c%m==0):
        n+=1
print(c)