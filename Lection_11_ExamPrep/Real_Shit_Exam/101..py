
try:
    word = input()
    counter = 0
    counter_letter = 0
    if word == '':
        print("INVALID INPUT")
    else:
        for letter in word:

            if letter == 'q' or letter == 'u' or letter == 'x':
                counter = 2
            elif letter == 'p' or letter == 't' or letter == 'w':
                counter = 1
            elif letter == 'r' or letter == 'v' or letter == 'y':
                counter = 3
            elif letter == 's' or letter == 'z':
                counter = 4
            elif ord(letter) % 3 == 1 or letter == ' ' and ord(letter) < 112:
                counter = 1
            elif ord(letter) % 3 == 2 and ord(letter) < 112:
                counter = 2
            elif ord(letter) % 3 == 0 and ord(letter) < 112:
                counter = 3
            if letter == 'a' or letter == 'b' or letter == 'c':
                counter_letter = '2'
                print(counter_letter * counter, end='')
            elif letter == 'd' or letter == 'e' or letter == 'f':
                counter_letter = '3'
                print(counter_letter * counter, end='')
            elif letter == 'g' or letter == 'h' or letter == 'i':
                counter_letter = '4'
                print(counter_letter * counter, end='')
            elif letter == 'j' or letter == 'k' or letter == 'l':
                counter_letter = '5'
                print(counter_letter * counter, end='')
            elif letter == 'm' or letter == 'n' or letter == 'o':
                counter_letter = '6'
                print(counter_letter * counter, end='')
            elif letter == 'p' or letter == 'q' or letter == 'r' or letter == 's':
                counter_letter = '7'
                print(counter_letter * counter, end='')
            elif letter == 't' or letter == 'u' or letter == 'v':
                counter_letter = '8'
                print(counter_letter * counter, end='')
            elif letter == 'w' or letter == 'x' or letter == 'y' or letter == 'z':
                counter_letter = '9'
                print(counter_letter * counter, end='')
            elif letter == ' ':
                counter_letter = '0'
                print(counter_letter * counter, end='')
except:
    print("INVALID INPUT")
