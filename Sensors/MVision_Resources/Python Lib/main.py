import sensor, image, time  # Import image sensor and time modules
from matrix_mini import send_data  # Import the send_data function from the matrix_mini module

# Initialize the sensor
sensor.reset()  # Reset the sensor
sensor.set_pixformat(sensor.RGB565)  # Set the pixel format to RGB565
sensor.set_framesize(sensor.QVGA)  # Set the image resolution to QVGA (320x240)
sensor.skip_frames(time=2000)  # Wait for 2 seconds to stabilize the sensor

# Set image flipping
sensor.set_vflip(True)  # Vertically flip the image
sensor.set_hmirror(True)  # Horizontally mirror the image

# Define color threshold range (HSV), suitable for detecting the target color
threshold = (0, 0, 0, 0, 0, 0)  # Hue, Saturation, and Value range

clock = time.clock()  # Create a clock to calculate frames per second (FPS) of image processing

while True:
    clock.tick()  # Start timing
    img = sensor.snapshot()  # Capture an image

    print(clock.fps())  # Output the current FPS

    # Find blobs (color regions) in the image that match the threshold
    blobs = img.find_blobs([threshold], pixels_threshold=200, area_threshold=200)
    if blobs:  # If blobs are found
        # Find the largest blob by area
        max_blob = max(blobs, key=lambda b: b[2] * b[3])

        img.draw_rectangle(max_blob.rect())  # Draw a rectangle around the largest blob

        # Calculate the center coordinates of the blob
        x_center = max_blob.cx()
        y_center = max_blob.cy()

        # Calculate the blob's area and round it to an integer
        blob_area = round(max_blob.area() / 2)

        # Send the center coordinates and area to an external system
        send_data([x_center, y_center, blob_area])

        # Mark the center point and coordinates text on the image
        img.draw_cross(x_center, y_center)  # Draw a cross at the center
        img.draw_string(0, 0, str(x_center) + ", " + str(y_center))  # Display the coordinates
