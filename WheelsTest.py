import picar
import time

picar.setup()
front_wheels = picar.front_wheels.Front_Wheels(debug=False)
back_wheels = picar.back_wheels.Back_Wheels(debug=False)

front_wheels.ready()
back_wheels.ready()

def drive_forward(speed):
    back_wheels.speed = speed
    back_wheels.forward()

    time.sleep(1)

def drive_backward(speed):
    back_wheels.speed = speed
    back_wheels.backward()

    time.sleep(1)

def stop():
    back_wheels.speed = 0
    back_wheels.stop()



drive_backward(1)
drive_backward(2)

drive_forward(2)
drive_forward(1)

stop()



