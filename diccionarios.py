def run():
    my_dic = {
        'key1': 1,
        'key2': 2,
        'key3': 3
    }

    print(my_dic['key1'])
    print(my_dic['key2'])
    print(my_dic['key3'])

    countries_population = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424
    }

    # print(countries_population['Colombia'])

    # RECORRER LAS KEYS DE UN DICCIONARIO
    for country in countries_population.keys():
        print(country)

    # RECORRER LOS VALORES DE UN DICCIONARIO
    for country in countries_population.values():
        print(country)

    # RECORRER KEYS Y VALUES DE UN DICCIONARIO
    for country, population in countries_population.items():
        print(country + ' tiene ' + str(population) + ' habitantes')


if __name__ == '__main__':
    run()
