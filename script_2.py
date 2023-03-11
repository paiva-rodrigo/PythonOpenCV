import cv2
#reconhece rostos em uma imagem
carrega = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
ima = cv2.imread('imagem1.png')
ima_cinza = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)
faces = carrega.detectMultiScale(ima_cinza)
print(faces)

for(x, y, l, a) in faces:
    cv2.rectangle(ima, (x, y), (x + l, y + a), (0, 255, 0), 2)

cv2.imshow("Caras",ima)
cv2.waitKey()

