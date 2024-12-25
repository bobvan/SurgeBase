from machine import Pin, PWM
from time import sleep
import math

# Initialize PWM on the LED pin (e.g., Pin 15)
led_pin = Pin(2)  # Replace with your LED pin number
led_pwm = PWM(led_pin)
led_pwm.freq(1000)  # Set PWM frequency to 1kHz

# Function to calculate duty cycle based on human perception
def perceived_brightness(level, max_duty):
    """
    Maps a level (0 to 1) to a logarithmic brightness scale (0 to max_duty).
    """
    return int(math.exp(level * math.log(max_duty)))

# Parameters
min_brightness = 0  # 0% brightness
max_brightness = 1  # 100% brightness
max_duty = 1023     # Maximum duty cycle for PWM (10-bit resolution)

# Loop to cycle brightness
while True:
    # Increase brightness from min to max
    for level in range(101):  # 0 to 100
        duty = perceived_brightness(level / 100, max_duty)
        led_pwm.duty_u16(duty)  # Adjust brightness
        sleep(0.02)  # Delay to see the effect

    # Decrease brightness from max to min
    for level in range(100, -1, -1):  # 100 to 0
        duty = perceived_brightness(level / 100, max_duty)
        led_pwm.duty_u16(duty)  # Adjust brightness
        sleep(0.02)  # Delay to see the effect
