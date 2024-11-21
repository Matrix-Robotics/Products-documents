# mVision-Python Lib for Arduino
An example for mVision Camera connect to MCU. Include MATRIX Mini (R3, R4).

## How it works
A MicroPython library from ceeoinnovations allow mVision (OpenMV) connect to other controller via UART Protocol, and we wrote a sample program to let mVision detect objects by color and mark them with IDs on the screen (IDE view) and send the information to other controller.

## Hardware
You can use SPIKE Ultrasonic sensor breakout board, or cut a wire to connect to SPIKE Hub, and connnect the wire as:

            mVision Pins       <------> Other MCU Pins (UART)
    Pin 1 (BLACK, GND        ) <------> GND
    Pin 2 (RED, VIN          ) <------> 3V3
    Pin 3 (WHITE, Tx         ) <------> Rx
    Pin 4 (BLUE, Rx          ) <------> Tx

For MATRIX User, can using the JST cable conneect direcly.

## Software - Camera side
Using OpenMV IDE or mVision IDE with Python mode, open "main.py" and copy the "matrix_mini.py" & "fill_light.py" to OpenMV disk drive, then Download the program to OpenMV, connect OpenMV to controller, and OpenMV IDE screen will show the object ID with square, controller will receive the largest object information(You can change the code to send diffrent information to controller). 

You can modify the send_data() content to custom the information you want to sent to controller, just make sure the Max size of send_data() is 20 items, and each items max value is 65535.

## Software - Controller side

For Arduino User, using the code in "Arduino Side" folder.
For MATRIX User, using the code in "MATRIX Side" folder.
