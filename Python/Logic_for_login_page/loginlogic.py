Username = "JohnDeer"
password = "NN2940"
A = input("Enter your unique username\n:")
B = input("Enter your password\n:")

if A == Username and B == password:
    print("login successful!")
    print("....")
    print("  /|")
    print(" / |")
    print("/__|")
    print("Welcome home %s" % Username)
else:
    print("You have entered either a wrong username or password try again!")
    exit(0)
