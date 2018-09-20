# MicroPython_MAX44009_driver
MicroPython driver for MAX44009 light sensor

There are specific versions for :
* BBC Micro:bit;
* low memory usage, using less RAM memory.

#### Example using Micro:bit lowmem version, rename the driver to 'max44009.py' and copy it to flash memory.
```python
import max44009
from microbit import i2c
sensor = max44009.MAX44009(i2c)
sensor.illuminance_lux()
```
