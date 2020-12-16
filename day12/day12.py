directions_raw = open('puzzle_input.txt', 'r').read().split('\n')
directions_test = """F10
N3
F7
R90
F11""".split('\n')

def simulate_directions(directions):
    current_direction = 90
    n = 0 #North
    e = 0 #East
    s = 0 #South
    w = 0 #West

    for d in directions:
        direction = d[:1]
        amount = int(d[1:])
        # print(f"{direction}{amount}: {current_direction} -- North: {n}, East: {e}, South: {s}, West: {w}")
        if(direction == 'F'):
            if(current_direction == 0 or current_direction == 360):
                if(s != 0):
                    if(s > amount):
                        s = s - amount
                    else:
                        n += amount - s
                        s = 0
                else:
                    n += amount
            elif(current_direction == 90):
                if(w != 0):
                    if(w > amount):
                        w = w - amount
                    else:
                        e += amount - w
                        w = 0
                else:
                    e += amount
            elif(current_direction == 180):
                if(n != 0):
                    if(n > amount):
                        n = n - amount
                    else:
                        s += amount - n
                        n = 0
                else:
                    s += amount
            elif(current_direction == 270):
                if(e != 0):
                    if(e > amount):
                        e = e - amount
                    else:
                        w += amount - e
                        e = 0
                else:
                    w += amount
        elif(direction == 'N'):
            if(s != 0):
                if(s > amount):
                    s = s - amount
                else:
                    n += amount - s
                    s = 0
            else: 
                n += amount
        elif(direction == 'E'):
            if(w != 0):
                if(w > amount):
                    w = w - amount
                else:
                    e += amount - w
                    w = 0
            else: 
                e += amount
        elif(direction == 'S'):
            if(n != 0):
                if(n > amount):
                    n = n - amount
                else:
                    s += amount - n
                    n = 0
            else: 
                s += amount
        elif(direction == 'W'):
            if(e != 0):
                if(e > amount):
                    e = e - amount
                else:
                    w += amount - e
                    e = 0
            else: 
                w += amount
        elif(direction == 'R'):
            current_direction += amount 
            if(current_direction >= 360):
                current_direction = current_direction - 360
        elif(direction == 'L'):
            current_direction -= amount 
            if(current_direction < 0):
                current_direction = 360 + current_direction

    # print(n, e, s, w)
    return (n + s) + (e + w)

p1_answer_test = simulate_directions(directions_test)
p1_answer = simulate_directions(directions_raw)

print(f"Part 1 Test -- Expected: 25, Got: {p1_answer_test}")
print(f"Part 1 -- {p1_answer}") 