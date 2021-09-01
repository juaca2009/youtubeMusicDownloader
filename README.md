# youtubeMusicDownloader
Script que extrae el audio de los videos de youtube por medio de la libreria Youtube-dl,
y convirte el audio descargado en formato wav.
Posteriormente, recorta un frame de 30 segundos de las canciones descargas y las canciones que no esten recortadas que se encuentren
en el directorio seleccionado para la descarga.

## Prerequisitos
#### FFMPEG:
Libreria encargada de realizar las conversiones entre formatos de audio.
```
sudo apt install ffmpeg
```

#### Librerias Python:
Las siguientes son las librerias necesarias para poder ejecutar el script conrrectamente:

* art==5.2
* colorama==0.4.4
* requests==2.26.0
* youtube-dl==2021.6.6
* pydub==0.25.1

Instale las librerias ejecutando el siguiente comando:
```
pip install -r requirements.txt
```
## Ejecucion del Script
Ejecute el fichero main.py para iniciar el script, debe poseer conexion a internet de lo contrario, 
el script no permitira descargar canciones.
```                                                                                                              
python main.py                                                                                                          
```  
