def palindromo(numero):
    numero_al_revez = numero[::-1]
    if  numero == numero_al_revez:
        return True
    else:
        return False


def run():
    numero = (input('Escribe un numero: '))
    if palindromo(numero) == True:
        print('Es palindromo')
    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()