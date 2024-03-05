import os
def añadirestudiante(campus:dict):
    os.system('cls')
    for key in campus['matricula']:
        print(key)
    grupo = input('Ingresa el nombre del grupo al cual le quieres añadir estudiantes : ')
    if grupo not in campus['matricula']:
        print('Ingresaste un grupo no registrado')
        os.system('pause')
        return
    for key,value in campus['campers'].items():
        campus['matricula'][grupo]['alumnos'].update({key:value})
        campus['matricula'][grupo]['totalalumnos'] += 1
        campus['campers'][key].update({'grupo':grupo})
        if campus['matricula'][grupo]['totalalumnos'] == campus['areas'][campus['matricula'][grupo]['area']]:
            break
        