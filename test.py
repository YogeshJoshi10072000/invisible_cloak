import cv2
cap=cv2.VideoCapture(0) #opeing camera

while(cap.isOpened()==True):
    ret,back=cap.read() #reding frames
    if(ret==True):
        cv2.imshow("image",back)  #back contains img background
        if(cv2.waitKey(5)==ord('q')):
            # saving image
            cv2.imwrite('image.jpg',back)    #saving image
            break


cap.release()
cv2.destroyAllWindows()
