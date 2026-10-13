import unittest
import conversions

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
            self.assertEqual(result, expected_fahrenheit)

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
            self.assertEqual(result, expected_kelvin)

if __name__ == '__main__':
    unittest.main()
