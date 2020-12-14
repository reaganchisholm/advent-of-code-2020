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
        if(direction == 'F'):
            if(current_direction == 0 or current_direction == 360):
                if(s != 0):
                    new_amount = amount - s
                    s = 0
                    n += new_amount
                else:
                    n += amount
            elif(current_direction == 90):
                if(w != 0):
                    new_amount = amount - w
                    w = 0
                    e += new_amount
                else:
                    e += amount
            elif(current_direction == 180):
                if(n != 0):
                    new_amount = amount - n
                    n = 0
                    s += new_amount
                else:
                    s += amount
            elif(current_direction == 270):
                if(e != 0):
                    new_amount = amount - e
                    e = 0
                    w += new_amount
                else:
                    w += amount
        elif(direction == 'N'):
            if(s != 0):
                new_amount = amount - s
                s = 0
                n += new_amount
            else: 
                n += amount
        elif(direction == 'E'):
            if(w != 0):
                new_amount = amount - w
                w = 0
                e += new_amount
            else: 
                e += amount
        elif(direction == 'S'):
            if(n != 0):
                new_amount = amount - n
                n = 0
                s += new_amount
            else: 
                s += amount
        elif(direction == 'W'):
            if(e != 0):
                new_amount = amount - e
                e = 0
                w += new_amount
            else: 
                w += amount
        elif(direction == 'R'):
            current_direction += amount 
        elif(direction == 'L'):
            current_direction -= amount 
        
    return (n + s) + (e + w)

p1_answer_test = simulate_directions(directions_test)
p1_answer = simulate_directions(directions_raw)

print(f"Part 1 Test -- Expected: 25, Got: {p1_answer_test}")
print(f"Part 1: {p1_answer}") #-277

# I think we need to check for L/R that fully turn around so it doesn't become a negative degrees
