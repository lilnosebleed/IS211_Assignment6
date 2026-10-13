class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

   ## if converting a unit to itself, return the same value
    if fromUnit == toUnit:
        return float(value)

    distances = ('meters', 'miles', 'yards')
    temperatures = ('kelvin', 'celsius', 'fahrenheit')

   ## checking for incompatible units
    if (fromUnit in distances and toUnit in temperatures) or (fromUnit in temperatures and toUnit in distances):
        raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit}")

   ## distance conversion
    if fromUnit in distances and toUnit in distances:
        ## convert whatever the fromUnit is, into meters
        if fromUnit == 'miles':
            meters = value * 1609.344
        elif fromUnit == 'yards':
            meters = value * 0.9144
        else:
            meters = value  # It's already in meters

        ## converting those meter into the toUnit
        if toUnit == 'miles':
            return float(meters / 1609.344)
        elif toUnit == 'yards':
            return float(meters / 0.9144)
        else:
            return float(meters)

    ## temp conversions
    elif fromUnit in temperatures and toUnit in temperatures:
        ## converting whatever the fromUnit is into kelvin
        if fromUnit == 'celsius':
            kelvin = value + 273.15
        elif fromUnit == 'fahrenheit':
            kelvin = (value + 459.67) * 5 / 9
        else:
            kelvin = value  # It's already in Kelvin

        ## converting the Kelvin into the toUnit
        if toUnit == 'celsius':
            return float(kelvin - 273.15)
        elif toUnit == 'fahrenheit':
            return float(kelvin * 9 / 5 - 459.67)
        else:
            return float(kelvin)

    else:
        ## a check to see if there any units not inthe list
        raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit}")
