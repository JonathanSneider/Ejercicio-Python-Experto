import os
def camperins(campus:dict):
    for key,value in campus['campers'].items():
        if campus['campers'][key]['estado'] == 'Inscrito':
            print(f'id : {key} - nombre : {campus['campers'][key]['nombre']}')
            
            
def camperapro(campus:dict):
    for key,value in campus['campers'].items():
        if campus['campers'][key]['estado'] == 'aprobado':
            print(f"id : {key} - nombre : {campus['campers'][key]['nombre']}")

def trainers(campus:dict):
    for key, value in campus['trainers'].items():
        print(f"id : {key} - nombre : {campus['trainers'][key]['nombre']}")
        
def estudiantesbajo(campus:dict):
    print('Campers con bajo rendimiento')
    for key,value in campus['campers'].items():
        if campus['campers'][key]['Notamodulo'] < 60:
            print(f"id : {key} - 'nombre : {campus['campers'][key]['nombre']}")


def traineryestudiantes(campus:dict):
    os.system('cls')
    for key,value in campus['matricula'].items():
        print(key)
    grupo = input('Ingrese el nombre del grupo el cual deseas listar : ')
    if grupo not in campus['matricula']:
        print('Ingresaste un nombre no registrado')
        os.system('pause')
        return
    else:
        pass
    for key,value in campus['matricula'][grupo].items():
        if key == 'trainer':
            print('---Tranier---')
            print(f"id : {key} - nombre : {campus['matricula'][grupo]['trainer']['nombre']}")
        
    print('---Estudiantes---') 
    for key,value in campus['matricula'][grupo].items():
        if key == 'alumnos':   
            for keys,values in campus['matricula'][grupo][key].items():
                print(f" id : {keys} - nombre : {values['nombre']}")  
                
def camperaproper(campus:dict):
    totalaprobados = 0
    totalperdidos = 0
    for key,value in campus['matricula'].items():
        print(key)
    grupo = input('Ingrese el nombre del grupo el cual deseas listar : ')
    if grupo not in campus['matricula']:
        print('Ingresaste un nombre no registrado')
        os.system('pause')
        return
    else:
        pass
    for key,value in campus['matricula'][grupo].items():
        if key == 'alumnos':  
            for keys,values in campus['matricula'][grupo][key].items():
                if values['Notamodulo'] >= 60:
                    totalaprobados += 1
    for key,value in campus['matricula'][grupo].items():
        if key == 'alumnos':  
            for keys,values in campus['matricula'][grupo][key].items():
                if values['Notamodulo'] <= 60:
                    totalperdidos += 1
                else:
                    pass
    print('---Estudiantes Aprobados---') 
    print(f"un total de : {totalaprobados}")
    print('---Estudiantes Desaprobados ---') 
    print(f" total de desaprobados : {totalperdidos}")