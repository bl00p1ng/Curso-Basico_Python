import random


def run():
    random_number = random.randint(1, 100)
    user_number = int(input('Elige un número del 1 - 100: '))

    while user_number != random_number:
        if user_number < random_number:
            print('⚠ Busca un número más grande')
        else:
            print('⚠ Busca un número más pequeño')
        user_number = int(input('Elige otro número: '))

    print('🏆 Ganaste!')


if __name__ == '__main__':
    run()
