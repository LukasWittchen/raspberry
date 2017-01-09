#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

LedPin = 29
bwmPin = 7


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.setup(bwmPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def blink():
    while True:
        print '...led on'
        GPIO.output(LedPin, GPIO.LOW)  # led on
        time.sleep(0.5)
        print 'led off...'
        GPIO.output(LedPin, GPIO.HIGH)  # led off
        time.sleep(0.5)

def status_bwm():
    while True:
        if GPIO.input(bwmPin):
            GPIO.output(LedPin, GPIO.LOW)
            print 'Bewegung detektiert'
        else:
            GPIO.output(LedPin, GPIO.HIGH)
        time.sleep(0.5)


def destroy():
    GPIO.output(LedPin, GPIO.HIGH)  # led off
    GPIO.cleanup()  # Release resource


if __name__ == '__main__':  # Program start from here
    setup()
    try:
        status_bwm()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
