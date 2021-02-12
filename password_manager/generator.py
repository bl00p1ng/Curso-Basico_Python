import random
import string


def generate_password():
    characters = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
    generated_password = []

    for i in range(15):
        random_char = random.choice(characters)
        generated_password.append(random_char)

    generated_password = ''.join(generated_password)
    return generated_password


def run():
    password = generate_password()
    print('Tu nueva contraseña es: ' + str(password))


if __name__ == '__main__':
    run()
