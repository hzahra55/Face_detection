# pip install opencv-python
# harrcascade_frontalface_default.xml

import cv2

# Read XML file for frontal face
cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_mouth = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
# Give Access to camera
cap = cv2.VideoCapture(0)

# Read image/video and make rectangle around face
while True :
    ret, img = cap.read()
    print(ret)  # true or false that able to read video or not
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #BGR to grayscale image
    faces = cascade_face.detectMultiScale(
        gray,
        1.3,
        5
    )
    # Rectangle has width and height
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), ( x+w, y+h ), (80,40,255), 4)

        # for mouth: focus on lower half of face 
        gray_m = gray[y+int(h/2) : y+h , x:x+w ]
        color_img_m = img[y + int(h/2): y+h, x: x+w]

        mouths = cascade_mouth.detectMultiScale(
            gray_m,1.3,5) 
        
        for (mx,my,mw,mh) in mouths:
            cv2.rectangle(color_img_m, (mx,my), (mx+mw, my+mh), (0,255,0), 4)


    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break


cap.release()
cv2.destroyAllWindows()
