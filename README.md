# APS


Instrução sobre o programa => 


1. Para executar o programa deve-se iniciar arquivo basImagens.py que ativará a câmera de captura da WebCam. Ele se encontra dentro da pasta Images, mas antes de executa-lo é necessário ir no arquivo em formato de txt, o input.txt e escrever seu nome nele e salvar. Só após isso que se executa a baseImages.py, que tirará fotos e armazenará em uma pasta/diretório de mesmo nome.

2. Após isso é necessário treinar o sistema através da sua base de imagens feita anteriormente, executando o treina.py que está fora do arquivo images. Ele analisará todas as suas fotos, registrando suas características para que possa identifica-lo no arquivo chamado “trainner.xml”.  ATENÇÃO, ao tirar as fotos evite uma iluminação muito baixa, pois irá interferir na sua identificação, então se atente a esse detalhe. 

3. E por último, execute o faces.py que abrirá a WebCam e identificará o rosto com um contorno azul. Se for identificado (de acordo com as informações retiradas e salvas no trainner.xml) informará seu nome, o mesmo que está na pasta.
