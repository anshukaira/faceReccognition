import cv2

#cascade classifier ---classifier name provided
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the input image
img = cv2.imread('/home/kaira/codes/cp/pypro/1/9.jpeg')

    #convert to gray scale as classifier gonna work with gray scale imgs
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #detect faces
    #args--grayscale img, scale factor- how much img size is reduced at each img scale, min neighbors- soecifying how many neighbor rectangle should have to retain it
faces = face_cascade.detectMultiScale(gray, 2.1, 4)

    #iterate over all the faces and darw a recatngle
for (x, y , w ,h) in faces:
        #drawing a rectangle
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

       
            
    # Display the output
cv2.imshow('img', img)
cv2.waitKey(5000)
cv2.destroyAllWindows
#cap.release()
