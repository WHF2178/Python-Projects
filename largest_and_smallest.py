
#largest
def lar(ar,n):
    l=ar[0]
    for i in range(1,n):
        if l<ar[i]:
            l=ar[i]
    return l
ar=[]
n=int(input("enter lenght of array"))
for i in range(0,n):
    e=int(input())
    ar.append(e)
print(ar)
ans=lar(ar,n)
print("largest is :",ans)

#smallest
def lar(ar,n):
    l=ar[0]
    for i in range(1,n):
        if l>ar[i]:
            l=ar[i]
    return l
ar=[]
n=int(input("enter lenght of array"))
for i in range(0,n):
    e=int(input())
    ar.append(e)
print(ar)
ans=lar(ar,n)
print("smallest is :",ans)
