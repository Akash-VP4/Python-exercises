class Temperature:

    def __init__(self):
        self._celsius = 0
        self._fahrenheit = 0
        self._kelvin = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        self._fahrenheit = (value * 9 / 5) + 32
        self._kelvin = value + 273.15

    @property
    def kelvin(self):
        return self._kelvin

    @kelvin.setter
    def kelvin(self, value):
        self._celsius = value - 273.15
        self._fahrenheit = (self._celsius * 9 / 5) + 32
        self._kelvin = value

    @property
    def fahrenheit(self):
        return self._fahrenheit

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5 / 9
        self._fahrenheit = value
        self._kelvin = self._celsius + 273.15
