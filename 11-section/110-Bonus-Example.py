# 110
# Bonus Example

# In this session we'll be creating a function which gets some numbers
# from a text file (files/data.txt) and returns the average of those numbers.

# def get_average():
#     with open("files/data.txt", "r") as file:
#         data = file.readlines()     # gives as list of strings
#         # ['temperatures\n', '5\n', '7\n', '12\n', '10']
#     values = data[1:]   # slicing (exclude the 1st line, temperatures)
#     values = [float(i) for i in values]     # list comprehension
#
#     average_local = sum(values) / len(values)
#     return average_local
#
# average = get_average()
# print(average)


################
# Bug-Fixing Exercise 1

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    print(f"maximum celcius: {maximum}")
    return maximum


celsius_max = get_maximum()
fahrenheit = celsius_max * 1.8 + 32

print(f"maximum fahrenheit {fahrenheit}")