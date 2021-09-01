from pydub import AudioSegment
import math
import re

class gestorRecortes():
    def __init__(self, _segundoInicio, _segundoFinal, _ruta):
        self.__cancion = None
        self.__nombreCancion = None
        self.__rutaCarpeta = _ruta
        self.__segInicio = _segundoInicio * 1000
        self.__segFinal = _segundoFinal * 1000

    def getCancion(self):
        return self.__cancion

    def getNombreCancion(self):
        return self.__nombreCancion

    def getRuta(self):
        return self.__rutaCarpeta

    def getSegInicio(self):
        return self.__segInicio/1000

    def getSegFinal(self):
        return self.__segFinal/1000
    
    def setCancion(self, _nombreC):
        self.__cancion = AudioSegment.from_wav(self.getRuta() + "/" + _nombreC)
        nombreSinWav = re.sub("\.wav", "", _nombreC)
        self.setNombreCancion(nombreSinWav)

    def setNombreCancion(self, _nombreC):
        self.__nombreCancion = _nombreC

    def setRuta(self, _ruta):
        self.__rutaCarpeta = _ruta

    def setSegInicio(self, _segInicio):
        self.__segInicio = _segInicio

    def setMinutoFinal(self, _segFinal):
        self.__segFinal = _segFinal

    def getDuracionCancion(self):
        return self.__cancion.duration_seconds

    def recortarCancion(self):
        audioRecortado = self.__cancion[self.__segInicio:self.__segFinal]
        audioRecortado.export(self.getRuta() + "/" + self.getNombreCancion() + "rec" + ".wav", format="wav")

