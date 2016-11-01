try:
    word = input()

    if word.endswith('y'):
        word = word[:-1]
        print(word + 'ies')
    elif word.endswith('o') or word.endswith('x') or word.endswith('s') or word.endswith('z') or word.endswith('ch') \
            or word.endswith('sh'):
        print(word + 'es')
    elif word.isdigit():
        print("INVALID INPUT")
    elif word == '':
        print("INVALID INPUT")
    else:
        print(word + "s")

except:
    print("INVALID INPUT")
