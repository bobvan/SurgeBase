from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)  # GPIO2 is usually the onboard LED

while True:
    led.value(1)  # Turn LED ON
    sleep(0.5)    # Wait for 500 ms
    led.value(0)  # Turn LED OFF
    sleep(0.5)    # Wait for 500 ms
