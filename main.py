from interfaz import interfaz 
import subprocess

YoutubeMusicDownloader = interfaz()
YoutubeMusicDownloader.mensajeInicial()
YoutubeMusicDownloader.probarConexion()
YoutubeMusicDownloader.solicitiarRutaDescarga()
YoutubeMusicDownloader.menuPrincipal()
#subprocess.call("python -m art fonts", shell=True)
