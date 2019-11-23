import numpy as np
import cv2
import pickle
import os

'''
Código fonte disponível em: https://github.com/codingforentrepreneurs/OpenCV-Python-Series/blob/master/src/faces.py

    A modificação feita no código fonte será diferenciado/representada da
seguinte forma abaixo:
#------------------------------------------------------------------------------#
                           ALTERAÇÕES FEITAS
#------------------------------------------------------------------------------#
'''


#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

#------------------------------------------------------------------------------#
#Carrega o classificador de um arquivo:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#------------------------------------------------------------------------------#
recognizer = cv2.face.LBPHFaceRecognizer_create()

#Vai ler o arquivo xml que contém as informações de cada pessoa cadastrada (possibilitando a identificação)
recognizer.read("trainner.xml")

#Informar o  nome da pessoa armazenado no "labels.pickle"
labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("Alan.mp4")

while(True):
    #Carrega o frame de video
    ret, frame = cap.read()
    #O reconhecimento não funciona com cores, então tem que converter para ter tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Em cada pessoa tem um retângulo em varias escalas da imagem, sempre marcando onde tem faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    #para cada face detectada
    for (x, y, w, h) in faces:
        #Desenha um retângulo (imagem, posição inicial, final, cor)
        #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)    
        #print(x, y, w, h)
        roi_gray = gray[y:y+h, x:x+w] #(ycord-start, ycord-end)
        roi_color = frame[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)
        if conf >= 45 and conf <= 85:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = labels[id_]
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

#------------------------------------------------------------------------------#
        #img_item = " .png"
#------------------------------------------------------------------------------#
        #cv2.imwrite(img_item, roi_gray)
    
        color = (255, 0, 0)
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x,y), (end_cord_x, end_cord_y), color, stroke)

        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #para cada OLHOS detectados
        #for (ex, ey, ew, eh) in eyes:
         #   cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0),2)
          #  print("Olhos")
        #subitems = smile_cascade.detectMultiScale(roi_gray)
        #para cada sorriso detectados
        #for (ex, ey, ew, eh) in subitems:
            #cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0),2)
        
    cv2.imshow("frame",frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
