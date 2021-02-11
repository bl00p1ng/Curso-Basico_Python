def run():
    LIMIT = 1000
    i = 0
    power_2 = 2**i

    while power_2 < LIMIT:
        print('2 elevado a ' + str(i) + ' es igual a: ' + str(power_2))
        i += 1
        power_2 = 2**i


if __name__ == '__main__':
    run()
