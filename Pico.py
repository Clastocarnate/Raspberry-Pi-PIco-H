import time
from machine import Pin
from servo import Servo
import sys
import select

# Set up the servo on GPIO 16
servo_pin = Pin(16)
servo = Servo(servo_pin)  # Initialize the servo on the specified pin

def set_servo_angle(angle):
    # Set the servo to the desired angle (0-180 degrees)
    servo.write(angle)

while True:
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        angle = sys.stdin.readline().strip()
        print("hi")
        try:
            angle = int(angle)
            if 0 <= angle <= 180:
                set_servo_angle(angle)
                print(f"Set angle to {angle} degrees")
            else:
                print("Angle out of range. Please input an angle between 0 and 180.")
        except ValueError:
            print("Invalid input. Please enter a numeric angle value.")
    time.sleep(0.1)

