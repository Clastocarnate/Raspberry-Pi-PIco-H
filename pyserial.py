import serial
import time

# Set up the serial connection (adjust the port and baud rate as necessary)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

def send_angle(angle):
    if 0 <= angle <= 180:
        ser.write(f"{angle}\n".encode())
        print(f"Sent angle: {angle}")
    else:
        print("Angle out of range. Please input an angle between 0 and 180.")

try:
    while True:
        angle = int(input("Enter the angle (0-180): "))
        send_angle(angle)
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program...")
    ser.close()
