username = "JohnDeer"
password = "NN2940"
A = input("Enter your unique username\n: ")
B = input("Enter your password\n: ")
attempt = " "
attempt_count = 0
attempt_limit = 5
out_of_attempts = False

while A == username and B == password and not (out_of_attempts):
    if attempt_count < attempt_limit:
        attempt_count +=1
    else:
        out_of_attempts = True

if out_of_attempts:
    print("You have either entered a wrong username or wrong password try again")
else:
    print("Login successful!")

print("....")
print("WELCOME TO OUR WEBSITE!")
print("  / |")
print(" /  |")
print("/___|")