def fuction1():
    list1 = ["s", "w", "g"]
    import random

    s = 1
    f = 11
    c = 0
    h = 0
    print("s:snake w: water g:gun : chance 10 time")

    while s < f:
        s += 1
        _input = input()
        _randomChoice = random.choice(list1)
        if _input == _randomChoice:
            c = h
            print("draw")
        elif _input == 's' and _randomChoice == 'w':
            h = h + 1
            print("human win")
        elif _input == 's' and _randomChoice == 'g':
            c = c + 1
            print("computer win")
        elif _input == 'g' and _randomChoice == 'w':
            c = c + 1
            print("computer win")
        elif _input == 'g' and _randomChoice == 's':
            h = h + 1
            print("human win")
        elif _input == 'w' and _randomChoice == 'g':
            h = h + 1
            print("human win")
        elif _input == 'w' and _randomChoice == 's':
            c = c + 1
            print("computer win")
        else:
            print("you\'r are wrong")
        print(f - s, "chance left")
    if c == h:
        print("match draw")
    elif c < h:
        print("human win", f"you\'r point {h}")
    else:
        print("computer win", f"computer point is {c}")
fuction1()
