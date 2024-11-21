# mVision-SPIKE
An example for mVision Camera connect to LEGO SPIKE Hub.

## How it works
A MicroPython library from ceeoinnovations allow mVision (OpenMV) emulate LEGO UART Protocol, and we wrote a sample program to let mVision detect objects by color and mark them with IDs on the screen (IDE view) and send the information to SPIKE Hub.

## Hardware
You can use SPIKE Ultrasonic sensor breakout board, or cut a wire to connect to SPIKE Hub, and connnect the wire as:

            mVision Pins       <------> SPIKE Pins
    Pin 1 (BLACK, GND        ) <------> Pin 3 GND
    Pin 2 (RED, VIN          ) <------> Pin 4 3V3
    Pin 3 (WHITE, Tx         ) <------> Pin 6 Rx
    Pin 4 (BLUE, Rx          ) <------> Pin 5 Tx

If we have wire or adapter can connect mVision camera and SPIKE Hub directly, we will update info here.

## Software - Camera side
Using OpenMV IDE or mVision IDE with Python mode, open "main.py" and copy the "LPF2.py" to OpenMV disk drive, then Download the program to OpenMV, connect OpenMV to SPIKE, and OpenMV IDE screen will show the object ID with square, SPIKE will receive the largest object information(You can change the code to send diffrent information to SPIKE). 

You can modify the DataToSend variable to custom the information you want to sent to SPIKE, just make sure the Max size of DataToSend variable is 8 items, and each items max value is 32767.

## Software - SPIKE Hub side
Pybricks:
```
Camera = PUPDevice(Port.F)
CamData = Camera.read(0) # CamData will got the DataToSend content from camera.
```

SPIKE App 3:
```
import device
CamData = device.data(port.F) # CamData will got the DataToSend content from camera.
```

## Reference
 - [PyBricks - LEGO Powered Up UART Protocol](https://github.com/pybricks/technical-info/blob/master/uart-protocol.md)
 - [ceeoinnovations/SPIKEPrimeBackpacks](https://github.com/ceeoinnovations/SPIKEPrimeBackpacks)
 - [EV3 Hardware Developer Kit](https://education.lego.com/en-us/support/mindstorms-ev3/developer-kits)

## Disclaimer
LEGO® is a trademark of the LEGO Group of companies which does not sponsor, authorize or endorse this software.
The LEGO Group and contributors to this repo are not liable for any loss, injury or damage arising from the use or misuse of the provided code or hardware.

