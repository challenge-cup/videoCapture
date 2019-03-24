import cv2
import numpy as np
import os 
DIR = './cap' 
N = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) 
print N
# N = 
for i in range(0,N-1):
    cap = cv2.imread('./cap/cap{}.jpg'.format(str(i)))
    sz = (640,480)
    fps=20
    fourcc= cv2.cv.FOURCC(*'XVID')
    videoWrite=cv2.VideoWriter('input.avi',fourcc,fps,sz)
    videoWrite.write(cap)
    cv2.imshow("capture",cap)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
videoWrite.release()
cv2.destroyAllWindows()
