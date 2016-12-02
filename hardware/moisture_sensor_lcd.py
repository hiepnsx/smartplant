#! /usr/bin/python
from time import sleep
from datetime import datetime
import spidev
import RPi.GPIO as GPIO
from RPLCD import CharLCD, BacklightMode

SPI = spidev.SpiDev()
SPI.open(0, 0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LCD = CharLCD(
    pin_rs=5, pin_rw=None, pin_e=6, pins_data=[13, 19, 26, 21],
    numbering_mode=GPIO.BCM, cols=16, rows=2, dotsize=8, auto_linebreaks=True,
    pin_backlight=20, backlight_enabled=True, backlight_mode=BacklightMode.active_high
)
LCD.clear()

def get_adc(channel):
    """Get ADC"""
    # Check valid channel
    if (channel > 7) or (channel < 0):
        return -1
    custom_chars = [
        (0b10000, 0b01001, 0b10001, 0b01001, 0b00001, 0b00010, 0b01100, 0b10000),
        (0b00001, 0b10101, 0b10101, 0b00001, 0b00001, 0b00010, 0b01100, 0b10000),
        (0b01001, 0b01010, 0b01001, 0b01100, 0b01010, 0b01000, 0b01000, 0b01000)
    ]
    LCD.create_char(0, custom_chars[0])
    LCD.create_char(1, custom_chars[1])
    LCD.create_char(2, custom_chars[2])
    while True:
        # Perform SPI transaction and store returned bits in 'r'
        bits = SPI.xfer([1, (8 + channel) << 4, 0])
        # Filter data bits from retuned bits
        adc_out = ((bits[1] & 3) << 8) + bits[2]
        percent = 100 - int(round(adc_out / 10.24))
        LCD.clear()
        LCD.write_string(datetime.now().strftime('%m/%d %H:%M:%S'))
        LCD.cursor_pos = (1, 0)
        LCD.write_string(unichr(0) + unichr(1) + unichr(2) + ': ' + str(percent) + '%')
        #print "ADC Output: {0:4d} Percentage: {1:3}%".format (adcOut,percent)
        sleep(1)

if __name__ == '__main__':
    get_adc(0)
