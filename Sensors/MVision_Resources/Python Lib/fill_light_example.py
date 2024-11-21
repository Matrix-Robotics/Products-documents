import sensor, image, time
import fill_light


fill_light.on()
time.sleep(1)
fill_light.off()
time.sleep(1)

while(True):
    for n in range(100):
        fill_light.brightness(n)
        time.sleep(0.01)
    for n in range(100,0,-1):
        fill_light.brightness(n)
        time.sleep(0.01)


