try:
    x = 0
    y = 0
    coordinate_fn = input()
    with open(coordinate_fn, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            items = line.split(' ')
            direction, step_len = items
            step_len = float(step_len)
            if direction == 'right':
                x += step_len
            elif direction == 'left':
                x -= step_len
            elif direction == 'up':
                y += step_len
            elif direction == 'down':
                y -= step_len
    print("X {:.2f}".format(x))
    print("Y {:.2f}".format(y))
except:
    print("INVALID INPUT")

