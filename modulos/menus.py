import os
def menuss():
    os.system('cls')
    opciones = ['1','2','3','4','5','6','7','8']
    titulo = """
    --------------------------
    +       MENU CAMPUS      +
    --------------------------
    """
    print(titulo)
    opcioness = '1. Regitrar candidato\n2. Registro prueba de ingreso\n3. Registrar ruta \n4. Registrar trainer\n5. Gestor de matricula\n6. Registrar notas filtro \n7. Reportes\n8. Salir'
    print(opcioness)
    op = input('selecciona una opciones : ')
    if op not in opciones:
        print('Ingresaste una opcion invalida')
        os.system('pause')
        menuss()
    else:
        return op
    

def menumatriculas():
    os.system('cls')
    opciones = ['1','2','3','4']
    tituloo = """
    ***********************
    +   MENU MATRICULAS   +
    ***********************
    """
    print(tituloo)
    opciness = '1. Crear Grupo\n2. Añadir estudiantes aprobados (Automatico)\n3. Añadir estudiantes aprobados ( Manual )\n4. Regresar'
    print(opciness)
    ops = input('Seleccione una opciones : ')
    if ops not in opciones:
        print('Ingresaste una opciones invalida')
        os.system('pause')
        menumatriculas()
    else:
        return ops
    
def menureportes():
    os.system('cls')
    opciones = ['1','2','3','4','5','6','7']
    titulo = """
    ///////////////////////
    *    MENU REPORTES   *
    //////////////////////
    """
    print(titulo)
    opcioness = '1. Listar los campers que se encuentren en estado de inscrito.\n2. Listar los campers que aprobaron el examen inicial.\n3. Listar los entrenadores que se encuentran trabajando con campuslands.\n4. Listar los estudiantes que cuentan con bajo rendimiento.\n5. Listar los campers y entrenador que se encuentren asociados a una ruta de entrenamiento.\n6. Mostrar cuantos campers perdieron y aprobaron cada uno de los modulos\n7. regresar'
    print(opcioness)
    op = input('Selecciona una opcion : ')
    if op not in opciones:
        print('Ingresaste una opcion no valida')
        os.system('pause')
        menureportes()
    else:
        return op
    
    