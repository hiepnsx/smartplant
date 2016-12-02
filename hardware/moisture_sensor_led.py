#! /usr/bin/python
from time import sleep
import spidev
import RPi.GPIO as GPIO

RED = 19
GREEN = 13
BLUE = 26

# Establish SPI device on Bus 0,Device 0
SPI = spidev.SpiDev()
SPI.open(0, 0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.output(RED, GPIO.LOW)
GPIO.output(GREEN, GPIO.LOW)
GPIO.output(BLUE, GPIO.LOW)

def toggle_led(current):
    """Toggle Led"""
    GPIO.output(RED, GPIO.HIGH if current == RED else GPIO.LOW)
    GPIO.output(GREEN, GPIO.HIGH if current == GREEN else GPIO.LOW)
    GPIO.output(BLUE, GPIO.HIGH if current == BLUE else GPIO.LOW)

def get_adc(channel):
    """Get ADC"""
    current = RED
    # Check valid channel
    if (channel > 7) or (channel < 0):
        return -1

    while True:
        # Perform SPI transaction and store returned bits in 'r'
        bits = SPI.xfer([1, (8 + channel) << 4, 0])

        # Filter data bits from retruned bits
        adc_out = ((bits[1] & 3) << 8) + bits[2]
        percent = 100 - int(round(adc_out / 10.24))

        if percent <= 20:
            current = RED
        elif percent < 60:
            current = GREEN
        else:
            current = BLUE

        toggle_led(current)
        #print out 0-1023 value and percentage
        print "ADC Output: {0:4d} Percentage: {1:3}%".format(adc_out, percent)
        sleep(10)

if __name__ == '__main__':
    get_adc(0)
