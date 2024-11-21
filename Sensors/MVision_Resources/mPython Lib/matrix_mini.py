from pyb import UART
from pyb import LED
from pyb import Pin

uart = UART(3, 115200)
pin0 = Pin('P4', Pin.IN, Pin.PULL_NONE)
is_enabled = False
green_led = LED(2)
green_led.on()

def enable_if_start_received():
    global is_enabled
    if uart.any() >= 5:
        start_signal = uart.read(5)
        if start_signal == b'start':
            is_enabled = True
            green_led.off()
            uart1 = UART(3, 115200)

def send_data(send_buffer):
    global is_enabled

    # 首次检查是否收到 'start' 指令
    if not is_enabled:
        enable_if_start_received()
        return

    length = len(send_buffer)
    if length > 20:
        raise Exception("Too much data, number of data should not exceed 20.")
    uart.writechar(0xaa)
    uart.writechar(length)
    check = 0xaa ^ length
    for n in send_buffer:
        if n < 0 or n > 65535:
            raise Exception("Value range error, value should be between 0 and 65535.")
        n = round(n)
        uart.writechar(n & 0xff)
        uart.writechar((n >> 8) & 0xff)
        check = check ^ (n & 0xff)
        check = check ^ ((n >> 8) & 0xff)
    uart.writechar(check)
