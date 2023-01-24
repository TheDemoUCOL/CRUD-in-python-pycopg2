import psycopg2

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'pass'
DB_HOST = 'localhost'
DB_PORT = '5432'

def one():
    conn=psycopg2.connect(dbname=DB_NAME, user=DB_NAME, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    ok=0
    while ok==0:
        try: #validación de ID
            new_id = int(input("Ingrese el id de la materia: "))
        except ValueError:
            print("Ingrese un número!")
            ok=+1
            break
        
        cur.execute("SELECT * FROM Materia WHERE materiaid="+str(new_id))
        if cur.rowcount == 0:
                print("El id no existe!")
        else:
            cur.execute("SELECT * FROM Materia WHERE materiaid="+str(new_id))
            res = cur.fetchone()
            print(f"La materia es: {res[1]}")
            print(f"la cantidad de temas es: {res[2]}")
            print(f"el maestro es: {res[3]}")
            print(f"el grupo es: {res[4]}")
            ok=+1
            conn.close()
            break

def all():
    conn=psycopg2.connect(dbname=DB_NAME, user=DB_NAME, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur=conn.cursor()
    cur.execute("SELECT * FROM Materia")
    print(f"{'ID':^12}{'Nombre':^12}{'Temas':^12}{'Maestro':^12}{'Grupo':^12}")
    print("-"*62)
    for row in cur.fetchall():
        print(f"{row[0]:^10} | {row[1]:^10} | {row[2]:^10} | {row[3]:^10} | {row[4]:^10}")
        print("-"*62)
    conn.close()
