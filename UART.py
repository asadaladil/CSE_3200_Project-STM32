import serial
# import time
# import random


def UART(number):
    sl = serial.Serial('COM5', 115200, timeout=1)
    # while True:
    # number=random.randint(0,9)
    # print(number)
    byte_value=str(number).encode()
    sl.write(byte_value)
    # print('done')
    # return number
    # time.sleep(2)


# UART(8)
# Python (PC) → USB Adapter (COM5) → UART (115200) → STM32 → 7-Segment Display.
