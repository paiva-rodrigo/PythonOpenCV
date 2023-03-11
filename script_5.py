import cv2

webcamera = cv2.VideoCapture(0)
calssificadorVideo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    camera,frame = webcamera.read()

    cinza = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    detetc = calssificadorVideo.detectMultiScale(cinza)
    for (x,y,l,a) in detetc:
        cv2.rectangle(frame,(x,y),(x+l,y+a),(255,0,255),2)
        print((x+l)/2,'  ',(y+a)/2)
    cv2.imshow("Imagem webCam",frame)
    if cv2.waitKey(1)== ord('f'):   break
    
webcamera.release()
cv2.destroyAllWindows()

