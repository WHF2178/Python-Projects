meronum=69
attemp=3
while(True):
    print("the number of guesses left are :",attemp)
    attemp=attemp-1

    if attemp>=0:
        print("enter the number u wanna guess?")
        g = int(input())
        if meronum>g:
            print("your number is lower")
            continue
        else:
            if meronum<g :
                print("your number is higher")
                continue
            elif meronum==g:
                print("you won")
                break
    else:
        print("you lose")
        print("thanbks for playing")
        break
print("wanna play again ? y / n ")
c=str(input())
if c=="y" or c=="Y":
    print("how many times do u wanna play ?")
    n=int(input())
    for i in range(1,n+1):
        print("remaining round is ", n)
        n=n-1
        meronum = 69
        attemp = 3
        while (True):
            print("the number of guesses left are :", attemp)
            attemp = attemp - 1

            if attemp >= 0:
                print("enter the number u wanna guess?")
                g = int(input())
                if meronum > g:
                    print("your number is lower")
                    continue
                else:
                    if meronum < g:
                        print("your number is higher")
                        continue
                    elif meronum == g:
                        print("you won")
                        print("the number of guesses left  is :", attemp)
                        break
                    break
            else:
                print("you lose")
                print("thanbks for playing")
                break
        continue

elif c=="n" or c=="N":
        print("thnks for playing")
