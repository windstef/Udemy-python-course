# 137
# Bonus Example

# use 2 modules in 2 files

# following:
# 128
# Bonus Example
# decoupling functions

# 119 Bonus Example
# decoupling output

# folder.file import function_name
from bonus.parsers14 import parse
# import bonus.parsers14      # other way

from bonus.coverters14 import convert

feet_inches = input("Enter feet inches: ")

parsed = parse(feet_inches)
# parsed = bonus.parsers14.parse(feet_inches)     # other way

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")