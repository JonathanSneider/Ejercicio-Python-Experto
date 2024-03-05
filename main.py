import json
import modulos.camperModule as camp
import modulos.rutasModule as rut
import modulos.menus as mn
import modulos.registropruebas as rgp
import os
import modulos.registrotrainer as rgt
import modulos.creargrupo as crg
import modulos.estudiantesgrupo as esta
import modulos.añadirestudiantesm as añe
import modulos.registrarnotasfil as rgn
import modulos.reportes as rp
campus = {
    'campers':{},
    'rutas':{
        'java':{
            'fundamentos':{},
            'web':{},
            'lengformal':{},
            'bd':{},
            'backend':{}
        },
        'nodejs':{
            'fundamentos':{},
            'web':{},
            'lengformal':{},
            'bd':{},
            'backend':{}
        },
        'netcore':{
            'fundamentos':{},
            'web':{},
            'lengformal':{},
            'bd':{},
            'backend':{}
        }
    },
    'areas':{
        'apolo':{
            'nombre':'Apolo',
            'capacidad':33
        },
        'artemis':{
            'nombre':'Artemis',
            'capacidad':35
        },
        'sputnik':{
            'nombre':'Sputnik',
            'capacidad':36
        }
    },
    'trainers':{},
    'matricula':{}
}
if __name__ == "__main__":
    isrun = True
    while isrun:
        op = mn.menuss()
        if op == '1':
            os.system('cls')
            isrun1 = True
            while isrun1:
                camp.AddCamper(campus.get('campers'))
                isrun1 = bool(input('Si desea registrar a otro estudiante presiona S(si) o ENTER(no) : '))
        if op == '2':
            isrun2 = True
            while isrun2:
                rgp.registrarpruebas(campus)
                isrun2 = bool(input('Si desea registrar las pruebas dde otro estudiante presione S(si) o N(no) : '))
        if op == '3':
            os.system('cls')
            isrun3 = True
            while isrun3:
                os.system('cls')
                for key in campus['rutas']:
                    print(key)
                print('-----------')
                rutaD = input('Ingrese la Ruta : ').lower()
                if rutaD not in campus['rutas']:
                    print('Ingresaste una opciones no valida')
                    os.system('pause')
                    continue
                else:
                    pass
                os.system('cls')
                for key in campus['rutas'][rutaD]:
                    print(key)
                print('-----------')
                eje = input('Ingrese el eje tematico : ').lower()
                if eje not in campus['rutas'][rutaD]:
                    print('Ingresaste una opciones no valida')
                    os.system('pause')
                    continue

                rut.AddRuta(campus.get('rutas').get(rutaD).get(eje))
                isrun3 = bool(input('Si desea agregar otra ruta presiona S(si) o ENTER(no) : '))

        if op == '4':
            isrun4 = True
            while isrun4:
                rgt.registrotrainer(campus)
                isrun4 = bool(input('Si desea agregar otro trainer presiona S(si) o ENTER(no) : '))
        if op == '5':
            isrun5 = True
            while isrun5:
                ops = mn.menumatriculas()
                if ops == '1':
                    isrun11 = True
                    while isrun11:
                        crg.creargrupo(campus)
                        isrun11 = bool(input('Si desea crear otro grupo presione S(si) o ENTER(no) : '))
                if ops == '2':
                    isrun22 = True
                    while isrun22:
                        esta.añadirestudiante(campus)
                        isrun22 = bool(input('Si desea añadir los estudiantes a otro grupo presines S(si) o ENTER(no) : '))
                if ops == '3':
                    isrun33 = True
                    while isrun33:
                        añe.añadirestudiantesm(campus)
                        isrun33 = bool(input('Si desea agregar otro estudiante presiona S(si) o N(no)'))
                if ops == '4':
                    isrun5 = False
                
        if op == '6':
            isrun6 = True
            while isrun6:
                rgn.notasregistrar(campus)
                isrun6 = bool(input('Si desea registrar la nota de otro estudiante presiona S(si) o ENTER(no) : '))
        if op == '7':
            isrun7 = True
            while isrun7:
                op = mn.menureportes()
                if op == '1':
                    isrun111 = True
                    while isrun111:
                        os.system('cls')
                        rp.camperins(campus)
                        os.system('pause')
                        isrun111 = False
                if op == '2':
                    isrun222 = True
                    while isrun222:
                        os.system('cls')
                        rp.camperapro(campus)
                        os.system('pause')
                        isrun222 = False
                if op == '3':
                    isrun333 = True
                    while isrun333:
                        os.system('cls')
                        rp.trainers(campus)
                        os.system('pause')
                        isrun333 = False
                if op == '4':
                    isrun444 = True
                    while isrun444:
                        os.system('cls')
                        rp.estudiantesbajo(campus)
                        os.system('pause')
                        isrun444 = False
                if op == '5':
                    isrun555 = True
                    while isrun555:
                        os.system('cls')
                        rp.traineryestudiantes(campus)
                        os.system('pause')
                        isrun555 = False
                if op == '6':
                    isrun666 = True
                    while isrun666:
                        os.system('cls')
                        rp.camperaproper(campus)
                        os.system('pause')
                        isrun666 = False
                if op == '7':
                    isrun7 = False
        if op == '8':
            isrun = False
            print(json.dumps(campus, indent=4))


