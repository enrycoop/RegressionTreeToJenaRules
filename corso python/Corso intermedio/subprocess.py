import os
import subprocess

os.chdir("C:\\Users\\enric\\Desktop\\") #cambio directory di lavoro
os.listdir() #listare tutte le cartelle

#questo comando non dipenderà dal sistema operativo
subprocess.run(["vlc","Interlude.mp3"])

"""
cosi sto dicendo che la stringa la deve interpretare come se fosse la shell.
Ma così facendo dipenderà dal sistema operativo.
Attenzione perchè il comando shell=True può causare falle di sicurezza.
"""
subprocess.run('dir',shell=True) 




