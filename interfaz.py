from sistemaOperativo import SistemaOperativo
from gestorDescarga import gestorDescargas
from recortador import gestorRecortes, DURACION_DE_RECORTE 
from colorama import Fore
import art

class interfaz():
    def __init__(self):
        self.__sistema = SistemaOperativo()
        self.__gestor = gestorDescargas()
        self.__recorte = None
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
        print(Fore.YELLOW + "------------------------------------------------------------------------------------------------------------------------------------------------") 
        print(Fore.YELLOW + art.text2art("Downloader", font="smslant"))
        print(Fore.CYAN + "\nCreado por: " + Fore.RESET + "Juan Camilo Hernandez Saavedra")
        print(Fore.GREEN + "GitHub: " + Fore.RESET + "https://github.com/juaca2009")
        print(Fore.MAGENTA + "Repositorio: " + Fore.RESET + "https://github.com/juaca2009/youtubeMusicDownloader")
        print(Fore.YELLOW + "------------------------------------------------------------------------------------------------------------------------------------------------") 
        

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
            print(Fore.RED + "[ADVERTENCIA]: " + Fore.RESET + "TENGA EN CUENTA QUE TODAS LAS CANCIONES CON UNA DURACION MAYOR A LOS SEGUNDOS ESTABLECIDOS")
            print("UBICADAS EN EL DIRECTORIO QUE ELIJA, SERAN RECORTADAS UNA VEZ REALIZE UNA DESCARGA.")
            ruta = input("Ingrese la ruta de descarga (Deje el espacio vacio para descargar en la ubicacion actual): ")
            if ruta == "":
                boolt = True
                print(Fore.BLUE + "\n[INFO]: " + Fore.RESET + "La ubicacion de descarga actual es: " + self.__sistema.get_directorioScript())
            else:
                if self.__sistema.directorioExiste(ruta):
                    self.__sistema.set_directorioDescarga(ruta)
                    self.__sistema.moverDirDescarga()
                    boolt = True
                    print(Fore.BLUE + "\n[INFO]: " + Fore.RESET + "La ubicacion de descarga actual es: " + self.__sistema.get_directorioDescarga())
                else:
                    print(Fore.RED + "\n[ERROR]: " + Fore.RESET + "El directorio no existe, vuelva a intentarlo")

    def solicitarRangoRecorte(self):
        boolt = False
        while boolt == False:
            print(Fore.BLUE + "\n[INFO]: " + Fore.RESET + "Por defecto el rango de recorte se encuentra entre los segundos 120 - 150 (2min-2:30min) el rango de recorte es de 30 segundos")
            rango = input("Ingrese el rango de recorte en segundos separados por un espacio (ej: 120 150) deje el espacio vacio para valor por defecto: ")
            if rango == "":
                self.__recorte = gestorRecortes(self.__sistema.get_directorioDescarga())
                boolt = True
            else:
                if self.verificarEntradaRango(rango.split()):
                    temp = rango.split()
                    self.__recorte = gestorRecortes(self.__sistema.get_directorioDescarga(), int(temp[0]), int(temp[1]))
                    boolt = True
                    print("\n")
                else:
                    print(Fore.RED + "\n[ERROR]: " + Fore.RESET + "Rango de recorte invalido")

            
            
    def verificarEntradaRango(self, _listaRango):
        if len(_listaRango) == 2:
            if _listaRango[0].isdigit() and _listaRango[1].isdigit():
                rMin, rMax = int(_listaRango[0]), int(_listaRango[1])
                if rMin >= 0 and rMax > 0 and rMax - rMin == DURACION_DE_RECORTE:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def descargarPlaylist(self, _url):
        self.__gestor.descargarCancion(_url, True)

    def descargarCancion(self, _url):
        self.__gestor.descargarCancion(_url)

    def descargarListaUrls(self, _urlList):
        self.__gestor.descargarCanciones(_urlList)

    def menuPrincipal(self):
        while self.getSalir() == False:
            print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Escriba exit para salir")
            url = input("Ingrese la url de la cancion o playlist (para varias canciones ingrese las urls separadas por comas): ")
            if url == "exit":
                self.setSalir(True)
                self.__sistema.limpiarPantalla()
            elif url == "":
                print(Fore.RED + "[ERROR]: " + Fore.RESET + "Formato de url incorrecto")
            else:
                opt = self.__gestor.verificarUrl(url)
                if opt == 1:
                    res = input("Desea descargar la playlist entera? (y/n): ")
                    if res == "y":
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar la playlist")
                        self.descargarPlaylist(url)
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Leyendo canciones del directorio")
                        listaCanciones = self.__sistema.obtenerListaCanciones()
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Recortando Canciones...")
                        cancionesRecortadas = self.__recorte.RecortarListaCanciones(listaCanciones)
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Eliminando Copias...")
                        print(cancionesRecortadas)
                        self.__sistema.eliminarListaCanciones(cancionesRecortadas)
                    elif res == "n":
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar la cancion")
                        self.descargarCancion(url)
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Leyendo canciones del directorio")
                        listaCanciones = self.__sistema.obtenerListaCanciones()
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Recortando Canciones...")
                        cancionesRecortadas = self.__recorte.RecortarListaCanciones(listaCanciones)
                        print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Eliminando Copias...")
                        print(cancionesRecortadas)
                        self.__sistema.eliminarListaCanciones(cancionesRecortadas)
                    else:
                        print(Fore.RED + "[ERROR]: " + Fore.RESET + "Respuesta invalida")
                elif opt == 2:
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar la playlist")
                    self.descargarPlaylist(url)
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Leyendo canciones del directorio")
                    listaCanciones = self.__sistema.obtenerListaCanciones()
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Recortando Canciones...")
                    cancionesRecortadas = self.__recorte.RecortarListaCanciones(listaCanciones)
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Eliminando Copias...")
                    print(cancionesRecortadas)
                    self.__sistema.eliminarListaCanciones(cancionesRecortadas)
                elif opt == 3:
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar la cancion")
                    self.descargarCancion(url)
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Leyendo canciones del directorio")
                    listaCanciones = self.__sistema.obtenerListaCanciones()
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Recortando Canciones...")
                    cancionesRecortadas = self.__recorte.RecortarListaCanciones(listaCanciones)
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Eliminando Copias...")
                    print(cancionesRecortadas)
                    self.__sistema.eliminarListaCanciones(cancionesRecortadas)
                elif opt == 4:
                    urlList = url.split(",")
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Se va a descargar las canciones")
                    self.descargarListaUrls(urlList)
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Leyendo canciones del directorio")
                    listaCanciones = self.__sistema.obtenerListaCanciones()
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Recortando Canciones...")
                    cancionesRecortadas = self.__recorte.RecortarListaCanciones(listaCanciones)
                    print(Fore.BLUE + "[INFO]: " + Fore.RESET + "Eliminando Copias...")
                    print(cancionesRecortadas)
                    self.__sistema.eliminarListaCanciones(cancionesRecortadas)
                else:
                    print(Fore.RED + "[ERROR]: " + Fore.RESET + "Formato de url incorrecto")
                print("\n")
                print(Fore.YELLOW + "------------------------------------------------------------------------------------------------------------------------------------------------") 
                self.probarConexion()
                print(Fore.BLUE + "\n[INFO]: " + Fore.RESET + "La ubicacion de descarga actual es: " + self.__sistema.get_directorioDescarga())
