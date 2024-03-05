import os
def registrarpruebas(campus:dict):
    os.system('cls')
    id = input('Ingrese el id del estudiante al cual le quieres registrar la nota de las pruebas : ')
    if id not in campus['campers']:
        print('ingresaste una id no valida')
        os.system('pause')
        return
    else:
        pruebateorica = int(input('Ingrese la nota teorica : '))
        pruebapractica = int(input('Ingrese la prueba pratica : '))
        notafinal = (pruebapractica + pruebateorica) / 2

    if notafinal >= 60:
        campus['campers'][id]['estado'] = 'aprobado'
        campus['campers'][id].update({'Grupo':''}) 
    else:
        del campus['campers'][id]
