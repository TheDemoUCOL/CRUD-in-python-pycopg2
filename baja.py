import time

def baja(id, name, price, lot):
    new_id = int(input("Ingrese el id del producto a eliminar: "))
    if new_id not in id:
            print("El id no existe!")
    else:
        pos=int(id.index(new_id))
        if input(f"Estas seguro que quieres eliminar {name[pos]}? (s/n)").lower() == "s":
            del id[pos]
            del name[pos]
            del price[pos]
            del lot[pos]
            print("Producto eliminado!")
            time.sleep(3)
            
        else:
            print("El producto no fue eliminado!")
            
    return id, name, price, lot