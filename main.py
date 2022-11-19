# health management system
def getdate():
    import datetime
    return datetime.datetime.now()


date_obj = str(getdate())
print("enter the client name : harry,rohan,hammad")
cl = input().lower()
if cl == "harry" or cl == "rohan" or cl == "hammad":
    print("welcome", cl, end=", ")

    inp2 = input("What do you want exercise or diet?\n").lower()
    if inp2 == "exercise":
        inp3 = int(input("Type 1 to log or 2 to retrieve "))
        if inp3 == 1:
            with open("exercise.txt", "a") as f:
                print("enter the choice")
                f.write(date_obj + " " + input())
        elif inp3 == 2:
            with open("exercise.txt") as f:
                print(f.readlines())
        else:
            print("Invalid input")

    elif inp2 == "diet":
        inp3 = int(input("Type 1 to log or 2 to retrieve\n "))
        if inp3 == 1:
            with open("diet.txt", "a") as f:
                print("enter the choice")
                f.write(date_obj + " " + input())
        elif inp3 == 2:
            with open("diet.txt") as f:
                print(f.readlines())
        else:
            print("Invalid input")
    else:
        print("invalid input")
else:
    print("Error! chose the correct client")
