# 128
# Bonus Example
# decoupling functions

# following:
# 119 Bonus Example
# decoupling output

feet_inches = input("Enter feet inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    # return feet, inches     # returns 2 values in tuple
    return {"feet": feet, "inches": inches}     # return dictionary {key, value}

# how to access, returned as dictionary
# parse("4 12")["feet"]
# 4.0
# parse("4 12")["inches"]
# 12.0


def convert(feet, inches):
    # parts = feet_inches.split(" ")
    # feet = float(parts[0])
    # inches = float(parts[1])
    # parts = parse(feet_inches)
    # feet = parts["feet"]
    # inches = parts["inches"]

    meters = feet * 0.3048 + inches * 0.0254
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"
    return float(meters)    # decoupling output (simplify the function)


parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")