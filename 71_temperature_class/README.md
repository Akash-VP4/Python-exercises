Write a class to convert from Fahrenheit, Celsius, and Kelvins.

You'll have to use descriptors, so read the doc first.

The class should be named Temperature, it represents a temperature, in any scale (I only ask for Fahrenheit, Celsius, and Kelvins, but you can add more as needed.)

It should work like this:
 
>>> t1 = Temperature()
>>> t1.kelvin = 0
>>> t1.celsius
-273.15
>>> t1.fahrenheit
-459.67
Your class should accept a modification of the current temperature from any of the three attributes, and should give proper values when accessed by any of the three attributes:

 
>>> t0 = Temperature()
>>> t0.celsius = 50
>>> t0.kelvin
323.15
>>> t0.celsius += 1
>>> t0.kelvin
324.15
>>> t0.kelvin -= 1
>>> t0.kelvin
323.15