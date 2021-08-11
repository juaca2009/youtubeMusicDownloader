from sistemaOperativo import SistemaOperativo
from gestorDescarga import gestorDescargas
#import subprocess

a = gestorDescargas()
print(a.probarConexion())
a.descargarCancion("https://www.youtube.com/watch?v=GhciBgYbA74&list=PLhxNyMmTLzoxuruCiW1gcYfLKVpY8OkQs", True)
