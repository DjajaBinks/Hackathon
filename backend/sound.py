#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import json

sound_pin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sound_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:

    counter = 0
    refresh_ratio = 1

    while True:
        counter += 1

        if (GPIO.input(sound_pin) == GPIO.LOW):
            data = {
                    "x": counter,
                    "y": 1,
            }
            with open("soundData.json", "w") as write_file:
                json.dump(data, write_file)
            time.sleep(refresh_ratio)
        if (GPIO.input(sound_pin) == GPIO.HIGH):
            data = {
                    "x": counter,
                    "y": 2,
            }
            with open("soundData.json", "w") as write_file:
                json.dump(data, write_file)
            time.sleep(refresh_ratio)
        else:
            data = {
                    "x": counter,
                    "y": 0,
            }
        time.sleep(refresh_ratio)
        with open("soundData.json", "w") as write_file:
            json.dump(data, write_file)
except KeyboardInterrupt:
    GPIO.cleanup()
