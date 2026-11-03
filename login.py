# Student Login Form

print("----- Student Login Form -----")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "student" and password == "12345":
    print("Login Successful!")
    print("Welcome", username)
else:
    print("Invalid Username or Password")