
from functools import wraps
"""
def funzione_decoratore(funzione):
    @wraps(funzione)
    def wrapper():
        '''wrapper significa incarto, confezione - convenzionale'''
        print('...codice da eseguie prima della funzione parametro...')
        funzione()
        print('...codice che la segue ...')
    return wrapper
"""

def caps_lock(funzione):
    @wraps(funzione)
    def wrapper(*args,**kwargs):
        return funzione(*args,**kwargs).upper() + 'dopo'

    return wrapper

class Caps_lock:
    def __init__(self, funzione):
        self.funzione = funzione
    def __call__(self,*args,**kwargs):
        return self.funzione(*args,**kwargs).upper()


def spam(funzione):
    @wraps(funzione)
    def wrapper(*args,**kwargs):
        print('SPAM!')
        return funzione(*args,**kwargs)
    return wrapper

@spam
@Caps_lock
def mia_funzione(msg):
    return msg

#mia_funzione = funzione_decoratore(mia_funzione)


#analogo


print(mia_funzione('ciao mondo'))