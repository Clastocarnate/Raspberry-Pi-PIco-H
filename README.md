# **Robotic Arm Project using Raspberry Pi Pico and Thonny**

## **Overview**

This project involves a robotic arm controlled by a Raspberry Pi Pico, utilizing a webcam for face tracking. The arm’s movements are controlled through Python scripts running on both the Pico (`Pico.py`) and the host computer (`Arm.py`). Communication between the two is handled via the PySerial library.

## **Project Structure**

- **Pico.py**: Script running on the Raspberry Pi Pico, responsible for interpreting commands received via serial communication and controlling the servo motor.
  
- **Arm.py**: Script running on the host computer, which processes the webcam feed to track faces and calculates the required angles to move the robotic arm.

## **Requirements**

### **Hardware**
- Raspberry Pi Pico
- Servo Motor connected to GPIO 16
- Webcam
- USB Cable (for power and communication)

### **Software**
- **Thonny IDE**: To upload and run `Pico.py` on the Raspberry Pi Pico.
- **Python 3.x**: Required for running the `Arm.py` script on your host computer.
- **PySerial**: For serial communication between the host computer and Raspberry Pi Pico.
- **OpenCV**: For processing webcam input.

### **Python Libraries**
- `pyserial`
- `opencv-python`

## **Installation and Setup**

1. **Install Required Python Libraries:**
   - Open a terminal or command prompt and install the required libraries:
     ```bash
     pip install pyserial opencv-python
     ```

2. **Upload `Pico.py` to Raspberry Pi Pico:**
   - Open Thonny IDE.
   - Connect the Raspberry Pi Pico to your computer via USB.
   - Open `Pico.py` in Thonny and select the Raspberry Pi Pico as the interpreter.
   - Upload the script to the Pico.

3. **Run `Arm.py` on Your Host Computer:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `Arm.py`.
   - Run the script:
     ```bash
     python Arm.py
     ```
   - Ensure the correct serial port is set in `Arm.py` (e.g., `/dev/ttyACM0`).

4. **Observe the Robotic Arm:**
   - The webcam will track faces, and the robotic arm will move based on the face’s position relative to the screen center.

5. **Ending the Program:**
   - Press `q` in the OpenCV window to stop the script and close the webcam feed.
   - Close Thonny and disconnect the Pico when done.

## **Troubleshooting**

- **Serial Connection Issues**: Ensure the correct COM port is set in `Arm.py`.
- **Movement Calibration**: If the arm’s movements are inaccurate, check the webcam’s alignment and calibration settings in `Arm.py`.
- **Pico Not Responding**: Restart the Raspberry Pi Pico and ensure `Pico.py` is correctly uploaded and running.

## **Future Enhancements**

- **Adding a Crossbow to Fire at ArUco Markers**: Integrating a crossbow attachment to automatically aim and fire at detected ArUco markers.
- **Additional Sensors**: Integrating sensors to improve the accuracy of the arm’s movements.
- **Advanced Control Algorithms**: Developing more sophisticated algorithms for smoother and more precise operations.

---

This README is formatted for GitHub and provides clear, step-by-step instructions for running your robotic arm project.
