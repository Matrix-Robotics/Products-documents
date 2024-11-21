from pyb import Pin, Timer

tim = Timer(4, freq=80000)
light_pin = tim.channel(1, Timer.PWM, pin=Pin("P7"), pulse_width_percent=10)

light_brightness = 30

def on():
    global light_brightness
    light_pin.pulse_width(light_brightness)

def off():
    light_pin.pulse_width(0)

def brightness(n):
    global light_brightness
    if n < 0:
        n = 0
    elif n > 100:
        n = 100
    light_brightness = round(n *0.4)
    light_pin.pulse_width(light_brightness)

