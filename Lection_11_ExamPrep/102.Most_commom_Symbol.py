import collections
expression = input()

if expression is None or expression == ' ':
    print("INVALID INPUT")
else:
    answer = collections.Counter(expression).most_common(1)[0]
    print(answer[0])
