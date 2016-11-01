user_input = input()
right_brackets = 0
left_brackets = 0

right_bracket_index = user_input.find('(')
left_bracket_index = user_input.find(')')

for symbol in user_input:

    if right_bracket_index > left_bracket_index:
        print("WRONG" + " " + str(len(user_input)))
        break
    if symbol == '(':
        right_brackets += 1
    elif symbol == ')':
        left_brackets += 1

if right_brackets == left_brackets and right_bracket_index < left_bracket_index:
    print("OK {}".format(left_brackets))
else:
    print("WRONG" + " " + str(len(user_input)))
