"""
MicroPython driver for Maxim Integrated MAX44009 ambient light I2C sensor, low memory version :
https://github.com/rcolistete/MicroPython_MAX44009
Version: 0.2.0 @ 2018/06/08
"""

class MAX44009:
    
    def __init__(self, i2c, address=0x4A):
        self.i2c = i2c
        self.address = address
        self.configuration = 0x00   # Default continous mode, automatic mode

    @property
    def configuration(self):
        return self._config

    @configuration.setter
    def configuration(self, value):
        self._config = value
        self.i2c.writeto_mem(self.address, 0x02, self._config)   # Register configuration

    @property
    def illuminance_lux(self):
        data = self.i2c.readfrom_mem(self.address, 0x03, 2)   # Register lux high byte
        exponent = (data[0] & 0xF0) >> 4
        mantissa = ((data[0] & 0x0F) << 4) | (data[1] & 0x0F)
        illuminance = (2**exponent)*mantissa*0.045
        return illuminance   # float in lux
