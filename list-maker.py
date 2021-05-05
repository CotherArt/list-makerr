import json, os
from colorama import init, Fore, Style

lista = []
file = 'lista.txt'
debug_mode = False # Bandera para mostrar los mensajes debug
init(autoreset=True)
clearconsole = lambda: os.system('cls')

# adds a item to the list
def add(msg):
    lista.append(msg)

# print the message on the console if debug_mode = True
def debug(msg):
    if debug_mode:
        print(msg)

# prints the list on the console
def show(lista):
    if len(lista) == 0:
        print(Fore.RED + 'La lista esta vacia')
        return
    indice = 0

    debug(Fore.RED + 'debug mode is on')
    print(Fore.CYAN + '\t### LIST-MAKER ###')
    print(Fore.YELLOW + '_____________________________________\n')
    for item in lista:
        indice += 1
        print('|' + Fore.BLUE + f'{indice}' + Fore.RESET + f'| {item}')
    print(Fore.YELLOW + '_____________________________________')

# save the list on a file
def save():
    try:
        with open(file, 'w') as f:
            json.dump(lista, f, indent=2)
            debug(Fore.GREEN + 'Lista guardada')
    except:
        debug(Fore.RED + 'Error al guardar')

# gets the list from the file
def openfile():
    global lista
    try:
        with open(file, 'r') as f:
            lista = json.load(f)
            debug(Fore.GREEN + 'Lista abierta')
    except:
        print(Fore.RED + 'Error al abrir')

# remove an item from the list
def remove(indice):
    global lista
    lista.pop(int(indice)-1)

# clears the list
def clearlist():
    global lista
    lista.clear()

def main():
    global lista, debug_mode
    clearconsole()
    openfile()
    show(lista)

    #main loop
    while True:
        # the debug mode deactivates the clear console
        if not debug_mode: 
            clearconsole()

        show(lista)

        message = input('\n> ')

        # identifies if is a command or a new item
        if message[0] == '!':
            message.lower()
            comm = message.split(' ')

            # commands available
            if comm[0] in ['!clear', '!clr', 'cls']:
                yesno = input('The whole list will be erased. Are you sure? (yes/no)')
                yesno.lower()
                if yesno in ['yes', 'y']:
                    clearlist() 
            if comm[0] in ['!remove', '!rm']:
                remove(comm[1])
                save()
            if comm[0] == '!debug':
                debug_mode = not debug_mode
        else:
            add(message)
            save()
        



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\nacabo el programita')