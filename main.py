import machine, neopixel
import math
import time

np = neopixel.NeoPixel(machine.Pin(6), 1)


# to calculate duty cycle based on human perception
def perceived_brightness(level, max_duty):
    """
    Maps a level (0 to 1) to a logarithmic brightness scale (0 to max_duty).
    """
    return int(math.exp(level * math.log(max_duty)))


def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

brightStep = 8
brightMax  = 255

def setBright(b):
    logB = int(math.exp((b/brightMax) * math.log(brightMax)))
    print(b, logB)
    np[0] = (0, 0, logB)
    np.write()
    time.sleep_ms(60)

while True:
    # XXX currently give double zero and double brightMax
    for i in range(brightStep-1, brightMax+1, brightStep):  # Count up
        setBright(i)
        time.sleep_ms(60)

    for i in range(brightMax, -1, -brightStep):  # Count down
        setBright(i)
        time.sleep_ms(60)
