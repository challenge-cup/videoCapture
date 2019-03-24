import cv2
import numpy as np
import sys
import os

videoN = sys.argv[1]
os.makedirs('cap{}'.format(videoN))
cap = cv2.VideoCapture(0)
sz = (640,480)
fps=30
# fourcc = cv2.cv.FOURCC(*'MJPG')
fourcc = cv2.cv.FOURCC(*'XVID')
videoWrite = cv2.VideoWriter('output{}.avi'.format(videoN),fourcc,fps,sz)

# videoWrite=cv2.VideoWriter('output.mp4',fourcc,fps,sz)
# videoWrite.open('./output.avi',-1,fps,sz,True)
i=0
while(1):
    ret,frame = cap.read()
    videoWrite.write(frame)
    cv2.imshow("capture",frame)
    cv2.imwrite("./cap{}/cap{}.jpg".format(videoN,str(i)),frame)
    i=i+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print i    
videoWrite.release()
cap.release()
cv2.destroyAllWindows()
