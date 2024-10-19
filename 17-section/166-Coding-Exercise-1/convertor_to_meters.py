def convert_feet_inches_to_meters(feet, inches):
    ''' convert feet and inches to meters '''
    # feet = float(feet)
    # inches = float(inches)
    # meters = feet * 0.3048 + inches * 0.0254
    # return float(meters)
    return feet * 0.3048 + inches * 0.0254

if __name__ == "__main__":
    meters = convert_feet_inches_to_meters(6, 45)
    print(meters)