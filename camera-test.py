import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Camera", gray)
    if cv2.waitKey(1) == ord('q'):#ord('q') returns the ASCII code of the "q" key
        break


cap.release()
cv2.destroyAllWindows()
