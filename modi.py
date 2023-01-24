import psycopg2
from operator import index

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'pass'
DB_HOST = 'localhost'
DB_PORT = '5432'

def modi():
    conn=psycopg2.connect(dbname=DB_NAME, user=DB_NAME, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    ok=0
    while ok==0:
        try:  # validación de ID
            new_id = int(input("Ingrese el id de la materia: "))
        except ValueError:
            print("Ingrese un número!")
            ok=+1
            break

        cur.execute("SELECT * FROM Materia WHERE materiaid="+str(new_id))
        row=cur.fetchone()
        if cur.rowcount == 0:
            print("El id no existe!")
        else:
            print(f"La materia es: {row[1]}")
            print(f"la cantidad de temas es: {row[2]}")
            print(f"el maestro es: {row[3]}")
            print(f"el grupo es: {row[4]}")

                #ingreso de nombre
            name_new = input("Ingrese el nombre de la materia: ")        
                #validación de temas
            try:
                theme_new = int(input("Ingrese la cantidad de temas a llevar: "))
            except ValueError:
                print("Ingrese un número!")
                ok+=1
                break
            
            if theme_new < 0:
                print("Ingrese un número positivo!")
                ok+=1
                break
            
            #validación de mestro
            teacher_new = input("Ingrese el maestro: ")


            #validación de grupo
            grup_new = input("A que grupo pertenece?: ")
            cur.execute("SELECT * FROM Materia WHERE grup=%s", (grup_new,))
            if cur.rowcount == 0:
                print("El grupo no existe!")
                ok = +1
                break
            
            if ok==0:
                try:
                    cur.execute("UPDATE Materia SET nam='"+name_new+"', notopics="+str(theme_new)+", teacher='"+teacher_new+"', grup='"+grup_new+"' WHERE materiaid="+str(new_id))
                    conn.commit()
                    print("El producto fue modificado!")
                    conn.close()
                    break
                except psycopg2.Error as e:
                    print(f"No se pudo modificar  Error: {e}")
            else:
                print("El producto no fue modificado!")