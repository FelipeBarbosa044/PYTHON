from pygame import mixer
from pygame import mixer
from time import sleep
lim  =  '\033[m '
ver = '\033[;31m'
verd = '\033[;32m'
amare = '\033[;33m'
azul = '\033[;34m'
ros = '\033[;35m'
cian = '\033[;36m'
cinz = '\033[;37m'
inver = '\033[7;40m'
x= 3
a = input(f'{inver}Digite algo para tocar... : {lim}')
while x > 0:
    print(f'{azul}{x}{lim}')
    sleep(1)
    x   -= 1
while True:
    mixer.init()
    mixer.music.load('mydama.mp3')
    mixer.music.play()
    z = input(f'{inver}Digite algo para parar de tocar... :{lim}')
    if z.isalnum() == True:
        break