import os
def creargrupo(campus):
    os.system('cls')
    nombre = input('ingrese el nombre del grupo : ')
    if nombre in campus['matricula']:
        print('Ingresaste un nombre que ya se encuentra registrado')
        return
    os.system('cls')
    for key,value in campus['trainers'].items():
        print(f'id:{key} nombre:{value['nombre']}')
    trainer = input('ingrese el id del trainer que quieres asiganar al grupo : ')
    os.system('cls')
    for key in campus['rutas']:
        print(key)
    ruta = input('ingrese la ruta del grupo : ')
    os.system('cls')
    for key in campus['areas']:
        print(key)
    area = input('Ingrese el Area del grupo : ')
    os.system('cls')
    horario = input('ingrese la hora de inicio de la clase : ')
    horario1 = input('ingrese la hora de finalizacion de la clase : ')
    hora, minutos = horario.split(":")
    horaEntero = int(hora)
    minutoEntero = int(minutos)
    hora1, minutos1 = horario1.split(":")
    horaEntero1 = int(hora1)
    minutoEntero1 = int(minutos1)
    os.system('cls')
    for keys,value in campus['matricula'].items():
        if ((horaEntero >= campus['matricula'][keys]['horarioin'][0]) and (area == campus['matricula'][keys]['area']) and (horaEntero1 <= campus['matricula'][keys]['horariofin'][0])):
            print('Ya existe un grupo registrado en ese horario y en la misma area de entrenamiento')
            os.system('pause')
            return
    else:
        pass
    fechain = input('Ingrese la fecha de inicializacion dd/mm/aa : ')
    fechafin = input('Ingrese la fecha de finalizacion dd/mm/aa : ')


    grupo = {
        
        'nombre':nombre,
        'trainer':campus['trainers'][trainer],
        'ruta':ruta,
        'area':area,
        'horarioin':[horaEntero,minutoEntero],
        'horariofin':[horaEntero1,minutoEntero1],
        'fechain':fechain,
        'fechafin':fechafin,
        'alumnos':{},
        'totalalumnos':0
        
    }
    
    
    campus['matricula'].update({nombre:grupo})
    
    
    
    
    