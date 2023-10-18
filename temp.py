def celsius_to_fahrenheit(celsius):
    """ given a celsius value return the conversion"""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

celsius = 25
# fahrenheit = celsius * 9/5 + 32
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")