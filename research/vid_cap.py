#!/usr/bin/python3

import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

while(True):
    ret, frame = cap.read()

    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    frame = cv2.resize(frame, (600, 800))

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


