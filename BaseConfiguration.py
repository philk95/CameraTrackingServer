import stream
import picar
from picar.SunFounder_PCA9685 import Servo
import logging

logger = logging.getLogger(__name__)


class BaseConfiguration:

    db_file = "config"

    def __init__(self):
        picar.setup()
        self.front_wheels = picar.front_wheels.Front_Wheels(debug=False, db=BaseConfiguration.db_file)
        self.back_wheels = picar.back_wheels.Back_Wheels(debug=False, db=BaseConfiguration.db_file)
        self.pan_servo = Servo.Servo(1)
        self.tilt_servo = Servo.Servo(2)
        self.ready()
        BaseConfiguration.start_stream()

    def ready(self):
        self.front_wheels.ready()
        self.back_wheels.ready()
        self.pan_servo.offset = 10
        self.tilt_servo.offset = 0
        self.pan_servo.write(90)
        self.tilt_servo.write(90)

    def cleanup(self):
        BaseConfiguration.stop_stream()
        self.back_wheels.stop()

    @staticmethod
    def start_stream():
        logger.info("Stream started: {}".format(stream.start()))

    @staticmethod
    def stop_stream():
        logger.info("Stream stopped: {}".format(stream.stop()))

    def start(self, func):
        func(self.front_wheels, self.back_wheels, self.pan_servo, self.tilt_servo)








