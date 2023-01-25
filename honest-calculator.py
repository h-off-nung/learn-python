# Messages
msgs = ["Enter an equation. The pattern is 'a + b'.",
       "Do you even know what numbers are? Stay focused!",
       "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
       "Yeah... division by zero. Smart move...",
       "Do you want to store the result? (y / n):",
       "Do you want to continue calculations? (y / n):",
       " ... lazy",
       " ... very lazy",
       " ... very, very lazy",
       "You are",
       "Are you sure? It is only one digit! (y / n)",
       "Don't be silly! It's just one number! Add to the memory? (y / n)",
       "Last chance! Do you really want to embarrass yourself? (y / n)"]
# Variables
result = 0.0
memory = 0.0
answer = ""
x, oper, y = 0.0, 0.0, 0.0


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msgs[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msgs[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "-" or v3 == "+"):
        msg = msg + msgs[8]
    if msg != "":
        msg = msgs[9] + msg
        print(msg)


def enter():
    global x
    global y
    global oper
    while True:
        print(msgs[0])
        calc = input()
        calc = calc.split()
        x, oper, y = calc[0], calc[1], calc[2]
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msgs[1])
            continue
        if oper != "+" and oper != "-" and oper != "*" and oper != "/":
            print(msgs[2])
            continue
        return x, oper, y


def operation(oper):
    global result
    match oper:
        case "+":
            result = x + y
        case "-":
            result = x - y
        case "*":
            result = x * y
        case "/":
            if y == 0:
                print(msgs[3])
                result = - 0.0
                # continue
            else:
                result = x / y
    print(result)
    return result

def save():
    global memory
    global result
    while True:
        print(msgs[4])
        answer = input()
        if answer == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(msgs[msg_index])
                    answer = input()
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        memory = result
                        break
                    if answer != "n":
                        continue
                    break
            else:
                memory = result
                break
        if answer == "n":
            break
        else:
            break


def goo():
    while True:
        global answer
        print(msgs[5])
        answer = input()
        if answer == "y":
            return answer
            break
        if answer != "n":
            continue
        return answer
        break


while True:
    enter()
    check(x, y, oper)
    operation(oper)
    if result != 0.0:
        save()
        goo()
        if answer == "y":
            continue
        break
