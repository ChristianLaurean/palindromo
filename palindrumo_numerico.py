def palindrome(number):
    upside_down_number = number[::-1]
    if  number == upside_down_number:
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