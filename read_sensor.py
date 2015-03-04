#!/usr/bin/env python
 
# From https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading
# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!
 
import RPi.GPIO as GPIO, time, os      
import datetime
import pytz
from sys import stdout
 
DEBUG = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
def RCtime (RCpin):
    reading = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, GPIO.LOW)
    time.sleep(0.1)
 
    GPIO.setup(RCpin, GPIO.IN)
    # This takes about 1 millisecond per loop cycle
    while (GPIO.input(RCpin) == GPIO.LOW):
            reading += 1
    return reading
 
def bars(x, scale=0.01):
    return "#" * int(scale * x)
    
   
def to_unix_timestamp(ts):
    """
    Get the unix timestamp (seconds from Unix epoch) 
    from a datetime object
    """
    start = datetime.datetime(year=1970, month=1, day=1)
    diff = ts - start
    return diff.total_seconds()


if __name__ == "__main__":
    
    while True:                                     
         reading = RCtime(18)
         n = datetime.datetime.now()
         timestamp = to_unix_timestamp(n)
         print "{},{}".format(timestamp, reading)
         stdout.flush()

