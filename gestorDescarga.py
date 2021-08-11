import requests, youtube_dl, subprocess

class gestorDescargas():
    def __init__(self):
        self.__urlYoutube = "https://www.youtube.com/"
        self.__verificadores = ["list=", "watch"]

    def getUrlYoutube(self):
        return self.__urlYoutube

    def probarConexion(self):
        response = requests.get(self.__urlYoutube)
        if response.status_code == 200:
            return True
        else:
            return False
    
    def descargarCancion(self, _url, esPlaylist = False):
        if not esPlaylist:
            subprocess.call(["youtube-dl", "--no-playlist", "--extract-audio", "--audio-format", "wav", _url])
        else:
            subprocess.call(["youtube-dl", "--yes-playlist", "--extract-audio", "--audio-format", "wav", _url])

    def descargarCanciones(self, _listaUrls):
        for i in _listaUrls:
            subprocess.call(["youtube-dl", "--extract-audio", "--audio-format", "wav", i.strip()])



