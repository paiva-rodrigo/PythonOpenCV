import cv2

carregaAlgoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
imagem = cv2.imread('imagem3.png')
imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
#deixe de usar o minNeighbors abaixo
faces = carregaAlgoritmo.detectMultiScale(imagem_cinza,scaleFactor=1.2,minSize=(40,40))
print(faces)
for (x,y,l,a) in faces:
    #argumentos são imagem,start point,endpoint, cor do rect e largura do seu fio
    cv2.rectangle(imagem,(x,y),(x+l,y+a),(255,0,255),2)
cv2.imshow("FACES",imagem)

cv2.waitKey()


