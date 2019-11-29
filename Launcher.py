from BaseConfiguration import BaseConfiguration
import CameraTracking
import atexit
import logging

logging.basicConfig()
logging.root.setLevel(logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    logger.info("Run main")
    base_configuration.start(CameraTracking.start)


def handle_cleanup():
    logger.info("Exiting: call cleanup")
    base_configuration.cleanup()


base_configuration = BaseConfiguration()
atexit.register(handle_cleanup)


if __name__ == '__main__':
    try:
        main()
    finally:
        handle_cleanup()
