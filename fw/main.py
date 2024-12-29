# flake8: noqa: E221
#
# Ramp the brightness of a NeoPixel blue LED up and down logarithmically, resulting
# a linear ramp in perceived brightness.
# Should result in a surging effect.

import machine
import neopixel
import math
import time

# Configuration Constants
rampSteps  = 40  # Number of steps as ramp rises and falls
rampStepMs = 30  # Time in milliseconds between steps
neoPin     = 20   # Pin for NeoPixel

# Manifest Constants
ledMax = 255    # Max brightness value for LED

# Derived Constants
brightStep = 1/rampSteps    # Size of steps in linear ramp

# Ten percent fudge factor to account for accumulating floating point errors
brightFudge = brightStep/10

np = neopixel.NeoPixel(machine.Pin(neoPin), 1)

ramp = []       # Ramp of calculated brightness values

# Converting a linear brightness of 0 to a logarithmic brightness takes exp(0),
# which is 1, so the LED never goes off unless the first value is forced to 0.
ramp.append(0)

# Increasing brightness ramp
linBright = brightStep
while linBright <= 1+brightFudge:
    logBright = int(math.exp(linBright * math.log(ledMax)))
    ramp.append(logBright)
    linBright += brightStep

# Decreasing brightness ramp
linBright = 1
while linBright >= brightStep+brightFudge:
    linBright -= brightStep
    logBright = int(math.exp(linBright * math.log(ledMax)))
    ramp.append(logBright)

assert len(ramp) == 2*rampSteps, \
       "Expecting ramp length of " + str(2*rampSteps) + \
       ", got " + str(len(ramp))
print(ramp)

while True:
    for brightness in ramp:
        np[0] = (0, 0, brightness) # Set NeoPixel blue LED to calculated brightness
        np.write()
        time.sleep_ms(rampStepMs)
