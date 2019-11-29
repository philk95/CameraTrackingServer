from picar.SunFounder_PCA9685 import Servo
import picar
import time

picar.setup()
pan_servo = Servo.Servo(1)
tilt_servo = Servo.Servo(2)

pan_servo.offset = 10
tilt_servo.offset = 0

def write_pan(angle):
    print("Pan write: ", angle)
    pan_servo.write(angle)

    time.sleep(1)

def write_tilt(angle):
    print("Tilt write: ", angle)
    tilt_servo.write(angle)

    time.sleep(1)

def reset():
    write_tilt(90)
    write_pan(90)

reset()
for a in [0, 45, 90, 135, 180]:
    write_pan(a)

reset()
for a in [0, 45, 90, 135, 180]: #45 does nothing?!
    write_tilt(a)

reset()