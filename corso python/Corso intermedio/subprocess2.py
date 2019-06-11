import subprocess
import os
print(os.listdir())
os.chdir('corso python\\Corso intermedio\\')
'''
su IDLE non verrà visualizzato nulla poiché
non erediterà lo standard output
'''
subprocess.run(['python','ifname.py'])
#questo si tramite comando stdout=subprocess.PIPE
subprocess.run(['python','ifname.py'],stdout=subprocess.PIPE)

