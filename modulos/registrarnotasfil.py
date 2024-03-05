import os
def notasregistrar(campus:dict):
    os.system('cls')
    id = input('Ingrese el id del estudiante al cual le desea registrar las notas del filtro : ')
    if id not in campus['campers']:
        print('Ingresaste una id no registrada : ')
        os.system('pause')
        return
    else:
        pass
    notateorica = int(input('Ingrese la nota teorica : '))
    notapractica = int(input('Ingrese la nota practica : '))
    notatrabajos = int(input('Ingres la nota total de los quices y trabajos : '))
    notatotal = (notapractica * 0.60)+(notateorica*0.30)+(notatrabajos*0.10)
    campus['campers'][id].update({'Notamodulo':notatotal})