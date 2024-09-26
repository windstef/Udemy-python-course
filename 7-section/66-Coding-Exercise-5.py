# Coding Exercise 5
# Please code this exercise in your computer IDE. For this exercise, download the members.txt file attached to the resources. Then, create a program that:
#
# 1. prompts the user to enter a new member.
#
# 2. adds that member to members.txt at the end of the existing members. For example, the user here has entered the member Solomon Right.
#
#
# In the above example, Solomon Right will be added to members.txt updating the content of the file to:
#
# John Smith
#
# Sen Lakmi
#
# Sono Octonot
#
# Solomon Right


new_member = input("Enter a new member: ")

file = open("files/members.txt", "r")
members = file.readlines()
file.close()

members.append(f"{new_member}\n")
# members.append(new_member + "\n")

file = open("files/members.txt", "w")
file.writelines(members)

file.close()


########################3

# Solution
# https://pythonhow.com/coding/d6c3/


# file = open("members.txt", 'r')
# existing_members = file.readlines()
# file.close()
#
# existing_members.append(member + "\n")
#
# file = open("members.txt", 'w')
# existing_members = file.writelines(existing_members)
# file.close()
