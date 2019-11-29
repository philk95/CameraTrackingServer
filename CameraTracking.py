#import picar
#from picar.SunFounder_PCA9685 import Servo
import cv2
import BlobDetection as detection
import time
from simple_pid import PID
import logging

logger = logging.getLogger(__name__)
pid_pan = PID(0.02, 0, 0, setpoint=0)
pid_tilt = PID(0.02, 0, 0, setpoint=0)

def start(front_wheels, back_wheels, pan_servo, tilt_servo):
    pan_angle = 90
    tilt_angle = 90
    pan_servo.write(pan_angle)
    tilt_servo.write(tilt_angle)

    camera = cv2.VideoCapture(0)
    (grabbed, image) = camera.read()
    y, x, rgb = image.shape

    center_image_y = int(y/2)
    center_image_x = int(x/2)

    logger.info(image.shape)
    logger.info((center_image_y, center_image_x))

    while True:
        (grabbed, image) = camera.read()

        detected = detection.find_center_of_blop(image, debug=True)

        if detected != None:
            center, circle = detected
            center_blob_x, center_blob_y = center
            logger.info("Found object with center (y|x): \t\t({}/{}|{}/{}) ".format(center_blob_x, center_image_x, center_blob_y, center_image_y))

            error_hor_dist = center_image_x - center_blob_x
            error_vert_dist = center_image_y - center_blob_y

            logger.info("Horizontal error: \t\t{}".format(error_hor_dist))
            logger.info("Vertical error: \t\t{}".format(error_vert_dist))

            pan_angle_offset = pid_pan(error_hor_dist)
            tilt_angle_offset = pid_tilt(error_vert_dist)

            logger.info("Pan angle: \t\t{}".format(pan_angle_offset))
            logger.info("Tilt angle: \t\t{}".format(tilt_angle_offset))

            pan_angle -= pan_angle_offset
            pan_servo.write(pan_angle)

            tilt_angle -= tilt_angle_offset
            tilt_servo.write(tilt_angle)

            #(x_circle, y_circle), radius = circle
            #cv2.circle(image, (int(x_circle), int(y_circle)), int(radius),
            #           (0, 255, 255), 2)
            #cv2.circle(image, center, 5, (0, 0, 255), -1)

            #time.sleep(1)

        #cv2.imshow("Frame", image)
        #cv2.waitKey(30)

        center = None
        #Not logging else case because output would be too much


#logging.basicConfig()
#logging.root.setLevel(logging.DEBUG)
#start(None, None, None, None)