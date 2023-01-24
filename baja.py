import time
import psycopg2

DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASS = 'pass'
DB_HOST = 'localhost'
DB_PORT = '5432'

def baja():
    
    conn=psycopg2.connect(dbname=DB_NAME, user=DB_NAME, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    
    try:
        new_id = int(input("Ingrese el id del la materia a eliminar: "))
    except ValueError:
        print("Ingrese un número!")
        
    cur.execute("SELECT * FROM Materia WHERE materiaid="+str(new_id))
    if cur.rowcount == 0:
            print("El id no existe!")
    else:
        cur.execute("SELECT * FROM Materia WHERE materiaid="+str(new_id))
        res= cur.fetchone()
        
        if input(f"Estas seguro que quieres eliminar {res[1]}? (s/n)").lower() == "s":
            try: 
                cur.execute("DELETE FROM Materia WHERE materiaid="+str(new_id))
                conn.commit()
                print("Producto eliminado!")
                time.sleep(3)
            except psycopg2.Error as e:
                print("Error al eliminar el producto!")
                print(e)
                conn.rollback()
                time.sleep(3)
        else:
            print("El producto no fue eliminado!")