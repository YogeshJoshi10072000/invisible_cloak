import cv2

cap=cv2.VideoCapture(0)
background=cv2.imread("./image.jpg")
while(cap.isOpened()==True):

    k,frame=cap.read()
    if(k==True):
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        cv2.imshow("",hsv)
        if(cv2.waitKey(5)==ord('q')):
            break


cap.release()
cv2.destroyAllWindows()