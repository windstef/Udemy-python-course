# 196
# Code Blocks, f-string

# follows
# 153 # Create a Desktop Graphical User Interface (GUI)


######################################

#### Code Blocks ####

## While-Loops ##

# infinite loop
while True:
    password = input("Enter password: ")


# while loop with condition
while password != "pass1":
    password = input("Enter password: ")

print("Password is correct")


## For-loops ##

usernames = ["john", "sim", "spongy"]
for username in usernames:
    print(username.capitalize())


## Match-Case ##

username = input("Enter username")

match username:
    case "john":
        print("Welcome Admin")
    case "sim":
        print("Welcome User")
    case "spongy":
        print("Welcome Guest")
    case _:
        print("Invalid username")


## If-Elif-Else ##

password = "pass"
if len(password) > 3:
    print("Password is strong")
else:
    print("Password is weak")


password = "pass"
if len(password) > 3:
    print("Password is strong")
elif len(password) == 4:
    print("Password is medium")
else:
    print("Password is weak")


## f-strings ##

first_name = "naya"
last_name = "anand"
message = f"Hello {first_name.capitalize()} {last_name.capitalize()}! Have a nice day!"
