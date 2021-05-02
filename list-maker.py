import json
from colorama import init, Fore

lista = []
file = 'lista.txt'
debug_flag = False # Bandera para mostrar los mensajes debug
init(autoreset=True)

def add(msg):
    lista.append(msg)
    save()

def debug(msg):
    if debug_flag:
        print(msg)

def show(lista): # Muestra la lista en la consola
    if len(lista) == 0:
        print(Fore.RED + 'La lista esta vacia')
        return
    indice = 0
    for item in lista:
        indice += 1
        print('|{}| {}'.format(indice, item))

def save():
    try:
        with open(file, 'w') as f:
            json.dump(lista, f, indent=2)
            debug(Fore.GREEN + 'Lista guardada')
    except:
        debug(Fore.RED + 'Error al guardar')
    
def openfile():
    global lista
    try:
        with open(file, 'r') as f:
            lista = json.load(f)
            debug(Fore.GREEN + 'Lista abierta')
    except:
        print(Fore.RED + 'Error al abrir')

def remove(indice):
    global lista
    lista.pop(indice-1)

def clearlist():
    global lista
    lista.clear()

def main():
    global lista
    openfile()
    print(Fore.CYAN + '\t### LIST-MAKER ###')
    while True:
        comando = input('> ')
        if comando == 'show':
            show(lista)
        else:
            add(comando)



if __name__ == '__main__':
    main()