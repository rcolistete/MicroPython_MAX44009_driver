"""
MicroPython driver for Maxim Integrated MAX44009 ambient light I2C sensor, low memory version, specific for BBC Micro:bit :
https://github.com/rcolistete/MicroPython_MAX44009
Version: 0.2.0 @ 2018/06/08
"""


class MAX44009:
    
    def __init__(self, i2c, address=0x4A):
        self.i2c = i2c
        self.address = address
        self.set_configuration(0x00)   # Default continous mode, automatic mode
  
    def configuration(self):
        return self._config

    def set_configuration(self, value):
        self._config = value
        self.i2c.write(self.address, bytearray([0x02, self._config]))   # Register configuration

    def illuminance_lux(self):
        self.i2c.write(self.address, bytearray([0x03]))   # Register lux high byte
        data = self.i2c.read(self.address, 2)
        exponent = (data[0] & 0xF0) >> 4
        mantissa = ((data[0] & 0x0F) << 4) | (data[1] & 0x0F)
        illuminance = (2**exponent)*mantissa*0.045
        return illuminance   # float in lux
