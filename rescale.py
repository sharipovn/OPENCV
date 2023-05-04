import cv2


cap = cv2.VideoCapture(0)

def make_1080p():
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1920)#width 3
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)#height 4

def make_720p():
    cap.set(3,1280)#width
    cap.set(4,720)#height 

def make_480p():
    cap.set(3,640)#width
    cap.set(4,480)#height     

def change_res(width,height):
    cap.set(3,width)
    cap.set(4,height)     

# make_480p()
# make_1080p()

def rescale_frame(frame,percent=75):
    scale_percent=75
    print(frame.shape)
    widht=int(frame.shape[1]*scale_percent/100)
    height=int(frame.shape[0]*scale_percent/100)
    dim=(widht,height)
    return cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
    
while True:
    ret, frame = cap.read()
    frame=rescale_frame(frame,percent=30)
    cv2.imshow("My Camera", frame)

    frame2=rescale_frame(frame,percent=500)
    cv2.imshow("Camera2", frame2)
    
    
    if cv2.waitKey(1) == ord('q'):#ord('q') returns the ASCII code of the "q" key
        break


cap.release()
cv2.destroyAllWindows()

