#lcm
"""a=int(input("enter 1st number : ")) 
b=int(input("enter 2nd number : ")) 
if a>b: 
    g=a 
else: 
    g=b 
c=0 
t=g 
while(True): 
    if g%a==0 and g%b==0 : 
        break 
    g = g+t 
    c=c+1 
print("the lcm of two number is : ",g) 
print("the number of count is : ",c) 
 
#hcf 
a=int(input("enter 1st number : ")) 
b=int(input("enter 2nd number : ")) 
if a<b: 
    s=a 
else: 
    s=b 
for i in range(1,s+1): 
    if a%i==0 and b%i==0: 
        hcf=i 
print("hcf of two number is ,",hcf) 
"""
#hcf and lcm in single program
while(True):
    print("this is calculator to print both lcm and hcf of numbers")
    a=int(input("enter 1st number"))
    b=int(input("enter 1st number"))
    print("for hcf then press 1\nfor lcm press 2 ")
    q=int(input())
    if q==1:
        if a<b:
            s=a
        else:
            s=b
        for i in range(1,s+1):
            if a%i==0 and b%i==0 :
                hcf=i
        print("the hcf of number is : ",hcf)
    print("wanna play more y / n ? ")
    c = input()
    if c == "y" or c == "Y":
        continue
    elif c == "n" or c == "N":
        break
    elif q==2:
        if a>b :
            g=a
        else:
            g=b
        while(True):
            if g%a==0 and g%b==0 :
                break
            g=g+1
        print("the lcm of number is : ",g)
    print("wanna play more y / n ? ")
    c = input()
    if c == "y" or c == "Y":
        continue
    elif c == "n" or c == "N":
        break

    else:
        print("invalid input ")
        print("wanna play more y / n ? ")
        c=input()
        if c =="y" or c=="Y":
            continue
        elif c=="n" or c=="N":
            break
