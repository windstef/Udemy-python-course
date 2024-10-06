def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return float(meters)    # decoupling output (simplify the function)
