import random

num = 0
choice = 0
name = ""


def strategy(num):
    lose = 0
    stop = num
    while stop > 0:
        stop -= 4
        lose = stop
        if lose == 1:
            break
    stop = 1
    match lose:
        case 1:
            return lose
        case other:
            while stop < num:
                if num - 1 == stop or num - 2 == stop or num - 3 == stop:
                    break
                stop += 4
            return stop

def number():
    global num
    while True:
        print("How many pencils would you like to use:")
        num = input()
        try:
            num = int(num)
        except ValueError:
            print("The number of pencils should be numeric")
            continue
        else:
            if num == 0:
                print("The number of pencils should be positive")
                continue
            if num < 0:
                print("The number of pencils should be numeric")
                continue
        return num
        break


def choose(num):
    global name
    while True:
        print("Who will be the first (John, Jack):")
        name = input()
        if name == "John" or name == "Jack":
            print("|" * num)
            return name
            break
        else:
            print("Choose between 'John' and 'Jack'")


def play(num, name):
    global choice
    trigger = 0
    while num > 0:
        print("{}'s turn!".format(name))
        match name:
            case "Jack":
                trigger = strategy(num)
                if trigger == 1:
                    choice = 1
                else:
                    choice = num - trigger
                if num == 3:
                    choice = 2
                if num == 4:
                    choice = 3
                print(choice)

                num -= choice
            case "John":
                choice = input()
                try:
                    choice = int(choice)
                except ValueError:
                    print("Possible values: '1', '2' or '3'")
                    continue
                else:
                    if choice > num:
                        print("Too many pencils were taken")
                        print("Possible values: '1', '2' or '3'")
                        continue
                    if choice == 1 or choice == 2 or choice == 3:
                        num -= choice
                    else:
                        print("Possible values: '1', '2' or '3'")
                        continue
        if num != 0:
            print("|" * num)
        if name == "John":
            name = "Jack"
        else:
            name = "John"
    print("{} won!".format(name))


number()
choose(num)
play(num, name)
