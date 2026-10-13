
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = 0
    
    return celsius + 273.15


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = 0
    
    return (celsius * 9/5) + 32


def convertFahrenheitToCelsius(fahrenheit):

    return (fahrenheit - 32) * 5/9

def convertFahrenheitToKelvin(fahrenheit):

    return (fahrenheit + 459.67) * 5/9

def convertKelvinToCelsius(kelvin):

    return kelvin - 273.15

def convertKelvinToFahrenheit(kelvin):

    return kelvin * 9/5 - 459.67
