import psycopg2
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'pass'
DB_HOST = 'localhost'
DB_PORT = '5432'

conn=psycopg2.connect(dbname=DB_NAME, user=DB_NAME, password=DB_PASS, host=DB_HOST, port=DB_PORT)
cur = conn.cursor()

def alta():
    ok=0
    while ok==0:
        try: #validación de ID
            id_new = int(input("Ingrese el id del materia: "))
        except ValueError:
            print("Ingrese un número!")
            ok=+1
            break
        
        cur.execute("SELECT * FROM Materia WHERE materiaid=%s", (id_new,))
        if cur.rowcount != 0: 
            print("El id ya existe!")
            ok=+1            
            break

        #ingreso de nombre
        name_new = input("Ingrese el nombre de la materia: ")
        cur.execute("SELECT * FROM Materia WHERE nam=%s", (name_new,))
        if cur.rowcount != 0:
            print("La materia ya existe!")
            ok = +1
            break

        #validación de temas
        try:
            topic_new = int(input("Ingrese la cantidad de temas a tomar: "))
        except ValueError:
            print("Ingrese un número!")
            ok=+1
            break
        if topic_new < 0:
            print("Ingrese un número positivo!")
            ok=+1
            break

        #ingreso del maestro
        teacher_new =input("Quien dará la clase?: ")
        
        #comprobación de grupo
        grup_new = input("A que grupo pertenece?: ")
        cur.execute("SELECT * FROM Materia WHERE grup=%s", (grup_new,))
        if cur.rowcount == 0:
            print("El grupo no existe!")
            ok = +1
            break
            
        if ok==0:
            try:
                cur.execute("INSERT INTO Materia VALUES (" + str(id_new) + ", '" + name_new + "', '" + str(topic_new) + "', '" + teacher_new + "', '" + grup_new + "')" )
                conn.commit()
            except psycopg2.Error as e:
                print("Error al insertar datos")
                print(e)
                ok=+1
                break
            
            if ok == 0:
                print("Datos insertados correctamente")
                ok=+1                
            break
    return