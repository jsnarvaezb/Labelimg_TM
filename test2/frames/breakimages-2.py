import cv2
import sys

print(sys.argv[1])
vidcap = cv2.VideoCapture(sys.argv[1])
success,image = vidcap.read()
count = 0

while success:
    success,image = vidcap.read()
    if count % 10 == 0:
        cv2.imwrite("test2-%d.jpg" % count, image)     # save frame as JPEG file

    print('Read a new frame: ', success)
    count += 1
