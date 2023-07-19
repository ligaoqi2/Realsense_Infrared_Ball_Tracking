import cv2


def draw(image, joints_2d):
    num_detected = len(joints_2d)
    for (i, joint) in enumerate(joints_2d):
        x, y = joint[0], joint[1]

        str_detected = "Detected Marker nums is {}".format(num_detected)
        cv2.putText(image, str_detected, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color=(0, 0, 255))

        str_show = "Coordinate is (" + str(int(x)) + ", " + str(int(y)) + ")"
        cv2.putText(image, str_show, (20, (i + 2) * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color=(0, 0, 255))

        # cv2.circle(image, (int(x), int(x)), int(radius), (0, 0, 255), -1)
        cv2.circle(image, (int(x), int(x)), 10, (0, 0, 255), -1)

    return image
