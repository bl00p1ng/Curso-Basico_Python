def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    inverse_word = word[::-1]

    if word == inverse_word:
        return True
    else:
        return False


def run():
    word = input('📝 Escribe una palabra: ')
    is_palindrome = palindrome(word)
    if is_palindrome:
        print('✅ Es palíndromo')
    else:
        print('❌ No es palíndromo')


if __name__ == '__main__':
    run()
