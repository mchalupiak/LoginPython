print("Welcome to MiOS")
yesValues = ["y", "yes", "true", "t"]
on = True
def yn(val):
    return val.lower() in yesValues
while on:
    account = input("Do you have an account? (y/n): ")
    if yn(account):
        print("Please login: ")
        user = input("Enter your username: ")
        userpassFile = open("usersInfo", "r")
        userInfo = [userpassFile.read().splitlines()]
        userInfoList = userInfo[0]
        try:
            userInfoList.index(user)
        except:
            print("Username is incorrect")
            continue
        while on:
            password = input("Enter your password: ")
            passIndex = userInfoList.index(user) + 1
            if password == userInfoList[passIndex]:
                print("Logged In!")
                break
            else:
                print("Incorrect password")
                continue
            break
        break
    elif not yn(account):
        create = input("Would you like to create an account? ")
        if yn(create):
            while on:
                createdUserName = input("What will your username be? ")
                userpassFile = open("usersInfo", "r")
                userInfo = [userpassFile.read().splitlines()]
                userInfoList = userInfo[0]
                if createdUserName in userInfoList:
                    print("Username is already taken")
                    continue
                userpassFile.close
                userpassFile = open("usersInfo", "a+")
                userpassFile.write("\n" + createdUserName)
                createdPassword = input("What will your password be? ")
                userpassFile.write("\n" + createdPassword)
                userpassFile.close
                break
        elif not yn(create):
            continue
