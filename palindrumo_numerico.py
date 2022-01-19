def palindrome(num):
    upside_down_number = num[::-1]
    if  num == upside_down_number:
        return True
    else:
        return False


def run():
    num = (input('Write a numero: '))
    if palindrome(num) == True:
        print('Is palindrome')
    else:
        print("It's not palindrome")


if __name__ == '__main__':
    run()