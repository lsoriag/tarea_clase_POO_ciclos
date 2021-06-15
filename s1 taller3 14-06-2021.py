#Luis Fernando Soria Guaranga
#Ingeniería en Software

#ejemplo ciclo for

class For:
    def __init__(self):
        pass

    def usoFor(self):
        nombre="Luis"
        datos=["Daniel",50,True]
        numeros=(2,5.6,4,1)
        docente={"nombre":"Erick","final":70,"fac":"faci"}
        listaNotas=[(30,40),[20,40],(50,40)]
        listaAlumnos=[{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        
        #for i in range(5):
        #    print("i={}".format(i))
        
        #for i in range(2,10):
        #    print("i={}".format(i))

        #for i in range(4,10,2):
        #    print("i={}".format(i),end=" ")

        #for i in range(12,3,-3):
        #    print("i={}".format(i),end=" ")

        #longitud=len(datos)
        #print(datos[0])
        #print(datos[1])
        #print(datos[2])
        #j=0
        #while j < longitud:
        #    print("while", datos[j])
        #    j=j+1

        #for i in range(longitud-1):
        #    print(datos[i])

        #for i,datos in enumerate(datos):
        #   print("for",i,datos)

        #for dato in numeros:
        #    print(datos)

        #for dato in ["H","o","l","a","que","tal"]:
        #   print (datos)

        print("\nDiccionario de notas")
        #for clave,valor in docente.items():
        #    print(clave,":",valor,end=" ")

        for alumno in listaAlumnos.items():
            for clave,valor in alumno.items():
                print(clave, ":" ,valor,end=" ")

bucle1=For()
bucle1.usoFor()
