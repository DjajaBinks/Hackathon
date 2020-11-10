#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import json

# sound_pin wird definiert
sound_pin = 18
# GPIO mode wird auf GPIO.BOARD gesetzt
GPIO.setmode(GPIO.BOARD)
# sound_pin wird als Eingang festgelegt
GPIO.setup(sound_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        # ueberpruefe ob ein Geraeusch erkannt wird
        if (GPIO.input(sound_pin) == GPIO.LOW):
            data = {
                "sound": {
                    "volume": 1
                }
            }
            with open("example.json", "w") as write_file:
                json.dump(data, write_file)
            time.sleep(0.5)
        if (GPIO.input(sound_pin) == GPIO.HIGH):
            data = {
                "sound": {
                    "volume": 1
                }
            }
            with open("example.json", "w") as write_file:
                json.dump(data, write_file)
            time.sleep(0.5)
        else:
            data = {
                "sound": {
                    "volume": 1
                }
            }
        time.sleep(0.5)
        with open("example.json", "w") as write_file:
            json.dump(data, write_file)
except KeyboardInterrupt:
    GPIO.cleanup()
