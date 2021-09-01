import platform, os 
import subprocess

class SistemaOperativo():
    def __init__(self):
        self.__so = platform.system()                
        self.__directorioScript = os.getcwd()
        self.__directorioDescarga = os.getcwd()

    def get_so(self):
        return self.__so

    def set_so(self, _so):
        self.__so = _so

    def get_directorioScript(self):
        return self.__directorioScript

    def set_directorioScript(self, _dirScrp):
        if self.directorioExiste(_dirScrp):
            self.__directorioScript = _dirScrp

    def get_directorioDescarga(self):
        return self.__directorioDescarga

    def set_directorioDescarga(self, _dirDes):
        if self.directorioExiste(_dirDes):
            self.__directorioDescarga = _dirDes

    def directorioExiste(self, _dir):
        return os.path.exists(_dir)
    
    def moverDirDescarga(self):
        os.chdir(self.__directorioDescarga)

    def moverDirScript(self):
        os.chdir(self.__directorioScript)

    def limpiarPantalla(self):
        if self.__so == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    def eliminarCancion(self, _NombreCancion):
        subprocess.call(["rm", _NombreCancion])

if __name__ == "__main__":
    a = SistemaOperativo()
    print(a.get_directorioScript())
