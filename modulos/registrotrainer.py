import os
def registrotrainer(campus:dict):
    os.system('cls')
    nombre = input('Ingresa el nombre del trainer : ')
    id = input('Ingresa el id del trainer : ')
    trainer = {
        'nombre':nombre,
        'id':id,
        'grupos':{}
    }
    campus['trainers'].update({id:trainer})
    