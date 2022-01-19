def palindrome(number):
    numero_al_reves = number[::-1]
    if  number == numero_al_reves:
        return True
    else:
        return False


def run():
    number = (input('Write a numero: '))
    if palindrome(number) == True:
        print('Is palindrome')
    else:
        print("It's not palindrome")


if __name__ == '__main__':
    run()