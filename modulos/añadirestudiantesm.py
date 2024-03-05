import os
capacidad = 0
def añadirestudiantesm(campus:dict):
    os.system('cls')
    for key in campus['matricula']:
        print(key)
    grupo = input('Ingresa el nombre del grupo al cual le quieres añadir estudiantes : ')
    if grupo not in campus['matricula']:
        print('Ingresaste un grupo no registrado')
        os.system('pause')
        return
    estudiante = input('Ingrese el id del estudiante al cual quieres agregar : ')
    if estudiante not in campus['campers']:
        print('Ingresaste una id no registrada')
        os.system('pause')
        return
    else:
        campus['matricula'][grupo]['alumnos'].update({estudiante:campus['campers'][estudiante]})
        campus['campers'][estudiante].update({'grupo':grupo})
        campus['matricula'][grupo]['totalalumnos'] += 1
        if campus['matricula'][grupo]['area'] == 'apolo':
            capacidad = 33
        elif campus['matricula'][grupo]['area'] == 'sputnik':
            capacidad = 36
        elif campus['matricula'][grupo]['area'] == 'artemis':
            capacidad = 35
        if campus['matricula'][grupo]['totalalumnos'] == capacidad:
            print('La grupo ya se encuentra lleno')
            os.system('cls')
            return
            
        