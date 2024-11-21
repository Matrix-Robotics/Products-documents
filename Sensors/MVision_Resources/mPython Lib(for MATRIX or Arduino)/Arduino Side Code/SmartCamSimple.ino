#include "SmartCamReader.h"  // Include the header file

unsigned int data[20];  // Array to store data received from OpenMV
unsigned int cX, cY, AREA;  // Variables to store received X, Y, and AREA values

void setup() {
  Serial.begin(115200);  // Initialize Serial communication with a baud rate of 115200
  Serial1.begin(115200); // Initialize Serial1 for data output with a baud rate of 115200
  delay(1000);
}

void loop() {
  // Use the SmartCamReader function to check and read data
  int result = SmartCamReader(data);  // Use the default timeout of 500ms

  // Handle the data or error based on the return value
  if (result > 0) {
    // Data read successfully, `result` indicates the length of the data
    cX = data[0];
    cY = data[1];
    AREA = data[2];

    // Output the received data to Serial1
    Serial1.print("X: ");
    Serial1.println(cX);
    Serial1.print("Y: ");
    Serial1.println(cY);
    Serial1.print("AREA: ");
    Serial1.println(AREA);
  } else {
    // Data read failed, output error message to Serial1
    Serial1.println("Error: Failed to read data.");
  }

  delay(100); // Add a delay to avoid excessively frequent outputs
}