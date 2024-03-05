import os
def AddRuta(ejetematico:dict):
    os.system('cls')
    stack = input('Ingrese el Stack : ')
    myStack ={
        'id' : str(len(ejetematico)+1).zfill(2),
        'nombre' : stack
    }
    ejetematico.update({myStack['id']:myStack})