#! /usr/bin/python
import spidev
import RPi.GPIO as GPIO
from RPLCD import CharLCD, BacklightMode
from time import sleep
from datetime import datetime

spi = spidev.SpiDev()
spi.open(0,0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
lcd = CharLCD(pin_rs=5, pin_rw=None, pin_e=6, pins_data=[13, 19, 26, 21],
              numbering_mode=GPIO.BCM,
              cols=16, rows=2, dotsize=8,
              auto_linebreaks=True,
              pin_backlight=20, backlight_enabled=True,
              backlight_mode=BacklightMode.active_high)
lcd.clear()

def getAdc(channel):
    #check valid channel
    if ((channel>7)or(channel<0)):
        return -1

    while True:
        # Perform SPI transaction and store returned bits in 'r'
        r = spi.xfer([1, (8+channel) << 4, 0])

        #Filter data bits from retruned bits
        adcOut = ((r[1]&3) << 8) + r[2]
        percent = 100 - int(round(adcOut/10.24))
        lcd.clear()
        lcd.write_string(datetime.now().strftime('%m/%d %H:%M:%S'))
        lcd.cursor_pos = (1, 0)
        lcd.write_string('Percentage: ' + str(percent) + '%')

        #print out 0-1023 value and percentage
        #print "ADC Output: {0:4d} Percentage: {1:3}%".format (adcOut,percent)
        sleep(1)

if __name__ == '__main__':
    getAdc(0)
