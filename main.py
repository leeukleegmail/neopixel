import time
import machine, neopixel

np = neopixel.NeoPixel(machine.Pin(4), 12)


def demo(np):

    n = np.n
    time_left = 50

    while time_left > 0:
    # cycle
        for i in range(4 * n):

            for j in range(n):
                np[j] = (0, 0, 0)
            # Modulus
            np[i % n] = (255, 0, 0)
            np.write()
            time.sleep_ms(time_left)
            time_left = time_left - 1

    for i in range(n):
        np[i] = (255, 0, 0)
    np.write()

    time.sleep_ms(4000)


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


demo(np)