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
        print(Fore.YELLOW + "--------------------------------------------------------------------------------------------") 
        print(Fore.YELLOW + art.text2art("Downloader", font="smslant"))
        print(Fore.YELLOW + "--------------------------------------------------------------------------------------------") 
        print(Fore.CYAN + "\nCreado por: " + Fore.RESET + "Juan Camilo Hernandez Saavedra")
        print(Fore.GREEN + "GitHub: " + Fore.RESET + "juaca2009")
        print(Fore.MAGENTA + "Repositorio: " + Fore.RESET + "https://github.com/juaca2009/youtubeMusicDownloader")
        

    def probarConexion(self):
        if not self.__gestor.probarConexion:
            print(Fore.RED + "[INFO]: " + Fore.RESET + "No se pude establecer una conexion")
            self.setSalir(True)
        else: 
            print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Conexion establecida con " + self.__gestor.getUrlYoutube())

    def solicitiarRutaDescarga(self):
        boolt = False
        while boolt == False:
            print(Fore.BLUE + "\n[INFO]: " + Fore.RESET + "La ubicacion de descarga actual es: " + self.__sistema.get_directorioScript())
            ruta = input("Ingrese la ruta de descarga (Deje el espacio vacio para descargar en la ubicacion actual): ")
            if ruta == "":
                boolt = True
                print(Fore.BLUE + "\n[INFO]: " + Fore.RESET + "La ubicacion de descarga actual es: " + self.__sistema.get_directorioScript())
            else:
                if self.__sistema.directorioExiste(ruta):
                    self.__sistema.set_directorioDescarga(ruta)
                    boolt = True
                    print(Fore.BLUE + "\n[INFO]: " + Fore.RESET + "La ubicacion de descarga actual es: " + self.__sistema.get_directorioDescarga())
                else:
                    print(Fore.RED + "\n[ERROR]: " + Fore.RESET + "El directorio no existe, vuelva a intentarlo")

    def menuPrincipal(self):
        while self.getSalir() == False:
            print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Escriba exit para salir")
            url = input("Ingrese la url de la cancion o playlist (para varias canciones ingrese las urls separadas por comas): ")
            if url != "exit":
                opt = self.__gestor.verificarUrl(url)
                if opt == 1:
                    res = input("Desea descargar la playlist entera? (y/n): ")
                    if res == "y":
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar la playlist")
                        self.__gestor.descargarCancion(url, True)
                    elif res == "n":
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar la cancion")
                        self.__gestor.descargarCancion(url)
                    else:
                        print(Fore.RED + "[ERROR]: " + Fore.RESET + "Respuesta invalida")
                elif opt == 2:
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar la playlist")
                    self.__gestor.descargarCancion(url, True)
                elif opt == 3:
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar la cancion")
                    self.__gestor.descargarCancion(url)
                elif opt == 4:
                    urlList = url.split(",")
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar las canciones")
                    self.__gestor.descargarCanciones(urlList)
                else:
                    print(Fore.RED + "[ERROR]: " + Fore.RESET + "Formato de url incorrecto")
                print("\n")
                self.probarConexion()
            else:
                self.setSalir(True)
                self.__sistema.limpiarPantalla()
