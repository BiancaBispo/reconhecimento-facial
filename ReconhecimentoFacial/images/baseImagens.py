import numpy as np
import cv2
import os

'''
Código fonte original disponível em: https://github.com/lucaslattari/UniversoDiscreto/tree/master/OpencVLOG/OpenCVLOG%2011.2

A modificação feita no código fonte será diferenciado/representada da
seguinte forma abaixo:
#------------------------------------------------------------------------------#
                          ALTERAÇÕES FEITAS
#------------------------------------------------------------------------------#
'''

def carregaNomesASeremLidos(txt):
#-------------------------------------------------------------------------------#
    listaNomeUsuarios = []
#-------------------------------------------------------------------------------#
    pFile = open(txt, "r")
    for line in pFile:
        listaNomeUsuarios.append(line.rstrip())
    return listaNomeUsuarios

    
def criaPastaComNomes(listaNomes):
    for nome in listaNomes:
        try:
            print("criou " + nome)
            os.mkdir(nome)
        except OSError:
            print("Não foi possível criar o diretório ou o mesmo já existe. \n")

def salvaFacesDetectadas(nome):
    #Para carregar o classificador haar:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#------------------------------------------------------------------------------#
    #cap = cv2.VideoCapture(nome + ".mp4") #O original inicia atráves do video
    cap = cv2.VideoCapture(0) #O zero vai executar através da Webcam
#------------------------------------------------------------------------------#    
    counterFrames = 0;
    while(counterFrames < 1000): #quando chegar ao milésimo frame, para 
        print(counterFrames)
        # Carrega o frame de video
        ret, img = cap.read()

        #frame não pode ser obtido? então sair
        if(ret == False):
            cap.release()
            return

        #O reconhecimento não funciona com cores, então tem que converter para ter tons de cinza
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Em cada pessoa tem um retângulo em varias escalas da imagem, sempre marcando onde tem faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #se nenhuma face for achada, continue
        if not np.any(faces):
            continue

        #achou uma face? recorte ela
        for (x, y, w, h) in faces:
            rostoImg = img[y:y+h, x:x+w]
            cv2.imshow("roi_gray", rostoImg)
            
        #imagens muito pequenas são desconsideradas
        larg, alt, _ = rostoImg.shape
        if(larg * alt <= 20 * 20):
            continue

        #salva imagem na pasta
        rostoImg = cv2.resize(rostoImg, (255, 255))
        cv2.imwrite(nome + "/" + str(counterFrames)+".png", rostoImg)
        counterFrames += 1
            
    cap.release()


#função principal da aplicação
#------------------------------------------------------------------------------#
def main():
#-------------------------------------------------------------------------------#
    listaNomeUsuarios = carregaNomesASeremLidos("input.txt")
    criaPastaComNomes(listaNomeUsuarios)
#-------------------------------------------------------------------------------#
    for nome in listaNomeUsuarios:
        print("Analisando: " + nome)
        salvaFacesDetectadas(nome)


if __name__ == "__main__":
    main()
