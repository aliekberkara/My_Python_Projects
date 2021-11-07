print("------------ User Login ------------")

username = 'michael65'
password = '3773146ali'
login = 3

while True:
    username1 = input("Enter Your Username:")
    password1 = input("Enter Your Password:")
    if username != username1 and password == password1:
        print("Incorrect Login!!!\nUsername Incorrect!!!")
        login -= 1
    elif username == username1 and password != password1:
        print("Incorrect Login!!!\nPassword Incorrect!!!")
        login -= 1
    elif username != username1 and password != password1:
        print("Incorrect Login!!!\nUsername and Password Incorrect!!!")
        login -= 1
    else:
        print("Successful Login!!!\nLogged in!!!")
        break
    if login == 0:
        print("Too Many Trials Made!!!")
        break
