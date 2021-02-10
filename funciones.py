# def print_message():
#     print('Mensaje especial')
#     print('¡Estoy aprendiendo a usar funciones!')
#
#
# print_message()
# print_message()
# print_message()

def conversation(msg):
    print('Hola')
    print('Cómo estás')
    print('Elegiste la opción ' + msg)
    print('Adios')


option = input('Elige una opción (1, 2, 3): ')

if option == '1':
    conversation(option)
elif option == '2':
    conversation(option)
elif option == '3':
    conversation(option)
else:
    print('⚠ Elegiste una opción incorrecta')
