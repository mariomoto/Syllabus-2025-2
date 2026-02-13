import os
import entities
import utils.pretty_print as pp

from os import path
from entities import Item, Usuario

def cargar_items() -> list:
    filepath = os.path.join(os.getcwd(), "utils", "items.dcc")
    file = open(filepath, "r", encoding="utf-8")
    items = []
    for line in file:
        nombre, puntos, precio = line.strip().split(",")
        items.append(Item(nombre, int(puntos), int(precio)))
    file.close()
    return items

def crear_usuario(tiene_suscripcion: bool) -> Usuario:
    usuario = Usuario(tiene_suscripcion)
    pp.print_usuario(usuario)
    return usuario

if __name__ == "__main__":
    usuario = crear_usuario(True)
    items = cargar_items()
    pp.print_items(items)
    for item in items:
        usuario.agregar_item(item)
    pp.print_canasta(usuario)
    usuario.comprar()
    pp.print_usuario(usuario)