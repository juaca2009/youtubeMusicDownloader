from interfaz import interfaz 
import subprocess
from recortador import gestorRecortes
from sistemaOperativo import SistemaOperativo

YoutubeMusicDownloader = interfaz()
YoutubeMusicDownloader.mensajeInicial()
YoutubeMusicDownloader.probarConexion()
YoutubeMusicDownloader.solicitiarRutaDescarga()
YoutubeMusicDownloader.menuPrincipal()

#cancion = "Amame - El Gran Combo-0vQ8A29Ul-8.wav"
#sis = SistemaOperativo()
#sis.set_directorioDescarga("/usr/src/app/salsa")
#print(sis.get_directorioDescarga())
#sis.moverDirDescarga()

#rec = gestorRecortes(120, 150, sis.get_directorioDescarga())
#rec.setCancion(cancion)
#rec.recortarCancion()
#sis.eliminarCancion(cancion)
