#health management system
#3 client  saurav sahan nikal
#Total 6 files
#wap like 1 for saurav 2 for sahan 3 for nikal
#first print time and print diet

def getdate():
    import datetime
    return datetime.datetime.now()
#make function to retrive exercise or food for any client
print("this program is about fitness exercise and diet plan of me my friend sahan and nikal")
a="saurav"
b="sahan"
c="nikal"
print("1 = saurav    2 = sahan     3 = nikal")
while(True):
    print("enter name of person u wanna retrive info about exercise and diet")
    d=str(input())
    if d==a:
        print("are you sure u going to know the exercise and diet plan of saurav ? y /n ")
        c=input()
        if c=="y"or c=="Y":
            e="diet"
            f="exercise"
            print("which info do you wanna know diet or exercise ?")
            g=str(input())
            if g==e:
                print("are you sure u wnna know the info about diet of saurav? y / n")
                h=str(input())
                if h=="Y" or h=="y":
                    print("local chicken ko masuu")
                elif h=="n" or h=="N":
                    print("Bharakr tapai le saurav ko diet plan bata exit garnu bayo")
                    continue

            elif g==f:
                print("are you sure u wnna know the info about exercise plan of saurav? y / n")
                i=str(input())
                if i=="Y" or i=="y":
                    print("pushups")
                elif i=="n" or i=="N":
                    print("Bharakr tapai le saurav ko exercise plan bata exit garnu bayo")
                    continue
        elif c=="n" or c=="N":
            print("thnks")
            continue

    elif d==b:
        print("are you sure u going to know the exercise and diet plan of sahan ? y /n ")
        c = input()
        if c == "y" or c == "Y":
            e = "diet"
            f = "exercise"
            print("which info do you wanna know diet or exercise ?")
            g = str(input())
            if g == e:
                print("are you sure u wnna know the info about diet of sahan? y / n")
                h = str(input())
                if h == "Y" or h == "y":
                    print("pork ko masuu")
                elif h == "n" or h == "N":
                    print("Bharakr tapai le sahan ko diet plan bata exit garnu bayo")
                    continue

            elif g == f:
                print("are you sure u wnna know the info about exercise plan of sahan ? y / n")
                i = str(input())
                if i == "Y" or i == "y":
                    print("pullup")
                elif i == "n" or i == "N":
                    print("Bharakr tapai le sahan ko exercise plan bata exit garnu bayo")
                    continue
        elif c == "n" or c == "N":
            print("thnks")
            continue

    elif d==c:
        print("are you sure u going to know the exercise and diet plan of nikal ? y /n ")
        c = input()
        if c == "y" or c == "Y":
            e = "diet"
            f = "exercise"
            print("which info do you wanna know diet or exercise ?")
            g = str(input())
            if g == e:
                print("are you sure u wnna know the info about diet of nikal? y / n")
                h = str(input())
                if h == "Y" or h == "y":
                    print("khasi ko masuu")
                elif h == "n" or h == "N":
                    print("Bharakr tapai le nikal ko diet plan bata exit garnu bayo")
                    continue
            elif g == f:
                print("are you sure u wnna know the info about exercise plan of nikal? y / n")
                i = str(input())
                if i == "Y" or i == "y":
                    print("crosswalked")
                elif i == "n" or i == "N":
                    print("Bharakr tapai le nikal ko exercise plan bata exit garnu bayo")
                    continue
        elif c == "n" or c == "N":
            print("thnks")
            continue
