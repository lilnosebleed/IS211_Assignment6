import unittest 
import conversions 

class testcelsiusconversions(unittest.testcase):

    def test_convertcelsiustokelvin(self):
        print("\nTest convertCeliusToKelvin.")
        test_cases = (
            (300.0, 573.15),
            (0.0, 273.15),
            (100.0, 373.15),
            (-273.15, 0.0),
            (20.0, 293.15)
        )
        for celsius, expected_kelvin in test_case:
          print(f"Cecking if {Celsisus} C == {expected_kelvin} K")
          result = round(conversions.convertcelsiustokelvin(celsius), 2)
          self.assertEqual(results, expected_kelvin)

      def test_convertcelsiustofarenheit(self):
          print("\n Testr convertcelsiustofarenheit.")
          test_cases = (
              (300.0, 572.0),
              (0.0, 32.0),
              (100.0, 212.0),
              (-40.0, -40.0),
              (20.0, 68.0)
          )
          for celsius, expected_fahrenheit in test_cases:
              print(f"Checkinf if {celsius} C == {expected_farenheit} F")
              results = round(conversions.convertcelsiustofarenheit(celsius), 2)
              self.assertEqual(result, expected_farenheit)


if __name__ = '__main__':
unittest.main()
