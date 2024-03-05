import os
def AddCamper(campers:dict):
    os.system('cls')
    id = input('Ingrese Id : ')
    nombre = input('Ingrese Nombre : ')
    apellido = input('Ingrese Apellido : ')
    direccion = input('Ingrese direccion : ')
    estado = 'Inscrito'
    tel = input('Ingrese Telefono : ')
    camper ={
        'id':id,
        'nombre':nombre,
        'apellido':apellido, 
        'direccion':direccion,
        'estado':estado,
        'tel':tel
    }
    campers.update({id:camper})