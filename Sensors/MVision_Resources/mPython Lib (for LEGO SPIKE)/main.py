import sensor, image, time
import gc,utime
import micropython
import LPF2
from machine import Pin
from pyb import LED
micropython.alloc_emergency_exception_buf(200)

# Target Setting
ball_threshold   = (39, 59, 41, 61, 32, 81) # Middle L, A, B values.

##Camera Define
sensor.reset()
sensor.set_vflip(True)
sensor.set_hmirror(True)
sensor.set_pixformat(sensor.RGB565) # Format: RGB565.
sensor.set_framesize(sensor.QVGA) # Size: QVGA (240x320)
sensor.set_auto_gain(True) # Close auto gain (must be turned off for color tracking)
sensor.set_auto_whitebal(True) # Close white balance (must be turned off for color tracking)
clock = time.clock() # Create a clock object to track the FPS.

##LUMP Define
modes = [LPF2.mode('OpenMV-ALL',size = 8, type = LPF2.DATA16, format = '3.0'),]
DataToSend = [0, 0, 0, 0, 0, 0, 0, 0] #X, Y, W, H, ID, state, 0, 0
max_idx = -1
lpf2 = LPF2.Prime_LPF2(3, 'P4', 'P5', modes, 62, timer = 4, freq =10)
lpf2.initialize()

##Main Task
while(True):
    #If LEGO Brick not connect
    if not lpf2.connected:
        LED(1).on() # Turn on Red LED
        LED(2).off() # Turn on Green LED
        LED(3).off() # Turn off Blue LED
        lpf2.sendTimer.deinit()
        utime.sleep_ms(50)
        lpf2.initialize()
    else:
        LED(1).off() # Turn off Red LED
        clock.tick() # Track elapsed milliseconds between snapshots().
        img = sensor.snapshot() # Take a snapshot
        blobs = img.find_blobs([ball_threshold], area_threshold=100) # Find Blobs

        #If blobs found, draw all
        if blobs:
            LED(2).on() # Turn on Green LED
            LED(3).off() # Turn off Blue LED
            max_size=0
            i = 0
            for b in blobs:
                #Draw all blobs with ID
                img.draw_string(b.x()-6, b.y()+3, str(i)) # Draw ID
                img.draw_rectangle(b[0:4]) #Draw a rectangle
                #Find largest blob
                if b.area() > max_size:
                    max_blob = b
                    max_size = b.area()
                    max_idx = i
                i += 1
            img.draw_string(1, 1, "X:" + str(max_blob.cx()) + ", Y:" + str(max_blob.cy()) + ", ID:" + str(max_idx) + ", FPS:" + str(clock.fps())) # Draw Max Blob Info
            DataToSend = [max_blob.cx(), max_blob.cy(), max_blob.w(), max_blob.h(), max_idx, 1, 0, 0]
        #If no blobs found
        else:
            LED(2).off() # Turn off Green LED
            LED(3).on() # Turn on Blue LED
            max_idx = -1
            DataToSend = [0, 0, 0, 0, 0, 7, 0, 0]

        #Send Data to LEGO Brick
        mode=lpf2.current_mode
        if mode==0:
             lpf2.load_payload('Int16',DataToSend)

        #print(clock.fps())
