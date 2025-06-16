# install opencv 
# download haarcascade_frontalface_default.xml and haarcascade_smile.xml
import cv2 

# to read cascade files
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cascade_smile = cv2.CascadeClassifier('haarcascade_smile.xml')

# Access Camera
cap = cv2.VideoCapture(0)
# Keep showing smile
 # 1. rate the image
 # 2. convert BGR to grayscale
while True:    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # conevrt colour image to gray
    f = cascade_face.detectMultiScale(   # scale has these 4 factors
        gray,
        scaleFactor= 1.3,
        minNeighbors=5,
        minSize=(30,20),
    )                   # work on face and then smile

    # Rectangle shown on face
    for (x,y,width,height) in f:
        cv2.rectangle(img, (x,y), (x+width, y+height), (255,0,0))  # add x with width and y with height, write bg value
        # write value for gray scale 
        gray_r = gray[y:y+height, x:x+width]

     # for smile now
        s = cascade_smile.detectMultiScale(
            gray_r, scaleFactor=1.5,
            minNeighbors=10,
            minSize=(25,25),
        )

        for i in s:
            if len(s) > 1:
                cv2.putText(img, 'SMILING MAN',(x,y-30),
                            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0.255,0),
                            3,cv2.LINE_4)
            
    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff

    if k==27:
        break

cap.release()
cv2.destroyAllWindows()