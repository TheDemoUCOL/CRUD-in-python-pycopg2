
from operator import index

def modi(id, name, price, lot):
    ok=0
    new_id = int(input("Ingrese el id del producto a modificar: "))
    pos=int(id.index(new_id))
    while ok==0:
        if new_id not in id:
            print("El id no existe!")
            ok=+1
        else:
            print("El producto es: ", name[pos])
            print("El precio es: ", price[pos])
            print("La cantidad es: ", lot[pos])
            #ingreso de nombre
            name_new = input("Ingrese el nombre del producto: ")        
            #validación de precio
            try:
                price_new = float(input("Ingrese el precio del producto: "))
            except ValueError:
                print("Ingrese un número!")
                ok+=1
                break
        
            if price_new < 0:
                print("Ingrese un número positivo!")
                ok+=1
                break
        
            #validación de lote
            try:
                lot_new = int(input("Ingrese la cantidad del producto: "))
            except ValueError:
                print("Ingrese un número!")
                ok=+1
                break
            if lot_new <= 0:
                print("Ingrese un número positivo!")
                ok=+1
                break
    
            if ok==0:
                name[pos]=name_new
                price[pos]=price_new
                lot[pos]=lot_new
                print("Producto modificado!")
                ok=+1
                break
            else:
                print("El producto no fue modificado!")

    return id, name, price, lot