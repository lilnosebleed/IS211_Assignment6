import unittest
import conversions
import conversions_refactored


class ConversionsTests(unittest.TestCase):

    def test_convertCelsiusToFahrenheit(self):
        print("Testing convertCelsiusToFahrenheit.")
        test_cases = [
            (300.0, 572.0),
            (0.0, 32.0),
            (100.0, 212.0),
            (-40.0, -40.0),
            (20.0, 68.0)
        ]
        for celsius, expected_fahrenheit in test_cases:
            print(f"Checking if {celsius} C == {expected_fahrenheit} F")
            result = round(conversions.convertCelsiusToFahrenheit(celsius), 2)
            self.assertAlmostEqual(result, expected_fahrenheit)

    def test_convertCelsiusToKelvin(self):
        print("Testing convertCelsiusToKelvin.")
        test_cases = [
            (300.0, 573.15),
            (0.0, 273.15),
            (100.0, 373.15),
            (-273.15, 0.0),
            (20.0, 293.15)
        ]
        for celsius, expected_kelvin in test_cases:
            print(f"Checking if {celsius} C == {expected_kelvin} K")
            result = round(conversions.convertCelsiusToKelvin(celsius), 2)
            self.assertAlmostEqual(result, expected_kelvin)

    def test_convertFahrenheitToCelsius(self):
        print("Testing convertFahrenheitToCelsius.")
        test_cases = [
            (572.0, 300.0),
            (32.0, 0.0),
            (212.0, 100.0),
            (-40.0, -40.0),
            (68.0, 20.0)
        ]
        for fahrenheit, expected_celsius in test_cases:
            print(f"Checking if {fahrenheit} F == {expected_celsius} C")
            result = round(conversions.convertFahrenheitToCelsius(fahrenheit), 2)
            self.assertAlmostEqual(result, expected_celsius)

    def test_convertFahrenheitToKelvin(self):
        print("Testing convertFahrenheitToKelvin.")
        test_cases = [
            (572.0, 573.15),
            (32.0, 273.15),
            (212.0, 373.15),
            (-40.0, 233.15),
            (68.0, 293.15)
        ]
        for fahrenheit, expected_kelvin in test_cases:
            print(f"Checking if {fahrenheit} F == {expected_kelvin} K")
            result = round(conversions.convertFahrenheitToKelvin(fahrenheit), 2)
            self.assertAlmostEqual(result, expected_kelvin)

    def test_convertKelvinToCelsius(self):
        print("Testing convertKelvinToCelsius.")
        test_cases = [
            (573.15, 300.0),
            (273.15, 0.0),
            (373.15, 100.0),
            (0.0, -273.15),
            (293.15, 20.0)
        ]
        for kelvin, expected_celsius in test_cases:
            print(f"Checking if {kelvin} K == {expected_celsius} C")
            result = round(conversions.convertKelvinToCelsius(kelvin), 2)
            self.assertAlmostEqual(result, expected_celsius)

    def test_convertKelvinToFahrenheit(self):
        print("Testing convertKelvinToFahrenheit.")
        test_cases = [
            (573.15, 572.0),
            (273.15, 32.0),
            (373.15, 212.0),
            (0.0, -459.67),
            (293.15, 68.0)
        ]
        for kelvin, expected_fahrenheit in test_cases:
            print(f"Checking if {kelvin} K == {expected_farenheit} F")
            result = round(conversions.convertKelvinToFahrenheit(kelvin), 2)
            self.assertAlmostEqual(result, expected_fahrenheit)


class RefactoredConversionsTests(unittest.TestCase):
    
    def test_temperature_conversions(self):
        print("Testing Refactored Temperature Conversions.")
        ## checking that all temperature conversions are working
        test_cases = [
            ("celsius", "kelvin", 300.0, 573.15),
            ("fahrenheit", "celsius", 32.0, 0.0),
            ("kelvin", "fahrenheit", 273.15, 32.0)
        ]
        for from_u, to_u, val, expected in test_cases:
            result = conversions_refactored.convert(from_u, to_u, val)
            self.assertAlmostEqual(expected, result, places=2)

    def test_distance_conversions(self):
        print("Testing Refactored Distance Conversions.")
        ## checking that all distance conversions are working
        test_cases = [
            ("miles", "meters", 1.0, 1609.34),
            ("yards", "meters", 1.0, 0.9144),
            ("miles", "yards", 1.0, 1760.0)
        ]
        for from_u, to_u, val, expected in test_cases:
            result = conversions_refactored.convert(from_u, to_u, val)
            self.assertAlmostEqual(expected, result, places=2)

    def test_same_unit_conversion(self):
        print("Testing Refactored Same Unit Conversions.")
        ## checking that converting from one unit to itself returns the same value
        test_cases = [
            ("miles", "miles", 10.0),
            ("celsius", "celsius", 100.0),
            ("meters", "meters", 5.0)
        ]
        for unit, target_unit, val in test_cases:
            result = conversions_refactored.convert(unit, target_unit, val)
            self.assertEqual(val, result)

    def test_incompatible_conversions(self):
        print("Testing Refactored Incompatible Conversions.")
        ## checking that converting incompatible units raises ConversionNotPossible
        self.assertRaises(
            conversions_refactored.ConversionNotPossible, 
            conversions_refactored.convert, 
            "celsius", "meters", 100.0
        )
        self.assertRaises(
            conversions_refactored.ConversionNotPossible, 
            conversions_refactored.convert, 
            "miles", "kelvin", 100.0
        )

if __name__ == '__main__':
    unittest.main()
