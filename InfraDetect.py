import numpy as np
import cv2
import imutils
from imutils import contours
from skimage import measure


def detect(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    thresh = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=1)
    thresh = cv2.dilate(thresh, None, iterations=4)

    labels = measure.label(thresh, connectivity=1, background=0)
    mask = np.zeros(thresh.shape, dtype="uint8")
    # loop over the unique components
    for label in np.unique(labels):
        # if this is the background label, ignore it
        if label == 0:
            continue
        labelMask = np.zeros(thresh.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)
        if 5 < numPixels < 350:
            mask = cv2.add(mask, labelMask)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    num_detected = len(cnts)
    if num_detected == 0:
        # str_no_detected = "Detected Marker nums is 0"
        # cv2.putText(image_rgb, str_no_detected, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color=(0, 0, 255))
        return image_rgb, None
    else:
        joints_2d = []
        cnts = contours.sort_contours(cnts)[0]
        # loop over the contours
        for (i, c) in enumerate(cnts):
            # (x, y, w, h) = cv2.boundingRect(c)
            ((cX, cY), radius) = cv2.minEnclosingCircle(c)

            # str_detected = "Detected Marker nums is {}".format(num_detected)
            # cv2.putText(image_rgb, str_detected, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color=(0, 0, 255))

            # str_show = "Coordinate is (" + str(int(cX)) + ", " + str(int(cY)) + ")"
            # cv2.putText(image_rgb, str_show, (20, (i + 2) * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color=(0, 0, 255))

            cv2.circle(image_rgb, (int(cX), int(cY)), int(radius), (0, 0, 255), -1)

            coord_array = np.array([int(cX), int(cY)])
            joints_2d.append(coord_array)
        return image_rgb, joints_2d
