def celsius_to_fahrenheit(celsius):
    """ given a celsius value return the conversion"""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def f_to_c(f):
    """given a fahrenheit value return the converted value"""
    # fahrenheit = celsius * 9/5 + 32
    # celsius = (f + 32) * 5/9
    return (f + 32) * 5/9

celsius = 25

fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")

celsius = f_to_c(fahrenheit)
print(f"{fahrenheit} fahrenheit to Celsius is {celsius}")