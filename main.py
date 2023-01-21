id=[]
name=[]
price=[]
lot=[]

from curses.ascii import isalpha
import time
import alta as a
import modi as m
import baja as b
import consulta as c
import os


def next():
  if input("Desea continuar? (s/n)").lower() == "s":
    return False
  else:
    return True

if __name__ == '__main__':
  

  
  while True:
    print("Seleccione una opción:")
    print("""
        1) Dar de alta un artículo.
        2) Modificar un artículo
        3) Eliminar un artículo
        4) Consultar las existencias
        5) Inventario total.""")

    option = input("Opción: ") 
    if option.isnumeric():
      option = int(option)
      if option == 1:
        a.alta()
        if next():
          break
      elif option == 2:
        m.modi()
        if next():
          break
      elif option == 3:
        b.baja()
        if next():
          break
      elif option == 4:
        c.one()
        if next():
          break
      elif option == 5:
        c.all()
        if next():
          break
      else:
        os.system("clear")
        print("Ingrese una opción valida!")
        time.sleep(3)
    else:
        os.system("clear")
        print("Ingrese una opción valida!")
        time.sleep(3)

    os.system("clear")
    