def is_prime(number):
    count = 0

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            count += 1
    if number == 1:
        return False
    if count == 0:
        return True
    else:
        return False


def run():
    number = int(input('Escribe un número: '))

    if is_prime(number):
        print('✅ Es primo')
    else:
        print('❌ No es primo')


if __name__ == '__main__':
    run()
