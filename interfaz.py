from sistemaOperativo import SistemaOperativo
from gestorDescarga import gestorDescargas
from colorama import Fore
import art

class interfaz():
    def __init__(self):
        self.__sistema = SistemaOperativo()
        self.__gestor = gestorDescargas()
        self.__salir = False

    def getSistema(self):
        return self.__sistema

    def getGestor(self):
        return self.__gestor

    def getSalir(self):
        return self.__salir

    def setSistema(self, _sistema):
        self.__sistema = _sistema

    def setGestor(self, _gestor):
        self.__gestor = _gestor

    def setSalir(self, _salir):
        self.__salir = _salir

    def mensajeInicial(self):
        self.__sistema.limpiarPantalla() 
        print(Fore.YELLOW + art.text2art("Downloader", font="smslant"))
        print(Fore.CYAN + "\nCreado por: " + Fore.RESET + "Juan Camilo Hernandez Saavedra")
        print(Fore.GREEN + "GitHub: " + Fore.RESET + "juaca2009")
        print(Fore.MAGENTA + "Repositorio: " + Fore.RESET + "https://github.com/juaca2009/youtubeMusicDownloader")

    def probarConexion(self):
        if not self.__gestor.probarConexion:
            print(Fore.RED + "[INFO]: " + Fore.RESET + "No se pude establecer una conexion")
            self.setSalir(True)
        else: 
            print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Conexion establecida con " + self.__gestor.getUrlYoutube())

