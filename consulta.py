from main import name, id, price, lot

def one(id, name, price, lot):
    ok=0
    while ok==0:
        try: #validación de ID
            id_new = int(input("Ingrese el id del producto: "))
        except ValueError:
            print("Ingrese un número!")
            ok=+1
            break
        if id_new not in id:
            print("El id no existe!")
            ok=+1            
            break
        else:
            print("El producto es: ", name[id.index(id_new)])
            print("El precio es: ", price[id.index(id_new)])
            print("La cantidad es: ", lot[id.index(id_new)])
            ok=+1
            break

def all(id, name, price, lot):
    print(f"{'ID':^12}{'Nombre':^12}{'Precio':^12}{'Cantidad':^12}")
    print("-"*48)
    for i in range(len(id)):
        print(f"{id[i]:^10} | {name[i]:^10} | {price[i]:^10} | {lot[i]:^10}") 
        print("-"*48)