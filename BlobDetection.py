import imutils
import cv2

colorLower = (94, 75, 136)
colorUpper = (119, 255, 255)

def __transform_frame(frame):
    # resize the frame, inverted ("vertical flip" w/ 180degrees),
    # blur it, and convert it to the HSV color space
    frame = imutils.resize(frame, width=600)
    #frame = imutils.rotate(frame, angle=180)
    # frame = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    return hsv_frame


def __create_mask(frame, debug):
    mask = cv2.inRange(frame, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    if debug:
        #cv2.imshow("Mask", mask)
        pass

    return mask


def __extract_center(cnts):
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        circle = cv2.minEnclosingCircle(c)
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])
        return (x, y), circle

    return None


def find_center_of_blop(image, debug=False):
    hsv_frame = __transform_frame(image)
    mask = __create_mask(hsv_frame, debug)

    # find contours in the mask and initialize the current
    # (x, y) center of the ball
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)[-2]

    detected = __extract_center(cnts)

    return detected