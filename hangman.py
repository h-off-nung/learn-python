import random

# initialisation
data = "python", "java", "swift", "javascript"
lost = 0
won = 0

print("H A N G M A N")


def menu():
    global won
    global lost
    while True:
        want = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        match want:
            case "play":
                return True
                break
            case "results":
                print("You won: {} times".format(won))
                print("You lost: {} times".format(lost))
            case "exit":
                return False
                break


def stop():
    global attempts
    global num
    global lost
    global won
    if attempts == 0:
        print()
        print("You lost!")
        lost += 1
        return False
    if num == 0:
        print("You guessed the word {}!".format(word))
        print("You survived!")
        won += 1
        return False


def check():
    global word
    global attempts
    global secret
    global found
    global num
    while True:
        print()
        print(secret)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("Please, input a single letter.")
            continue
        if guess.islower() == False or not ('a' <= guess <= "z"):
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if guess in found:
            print("You've already guessed this letter.")
            continue
        if guess in word:
            ser = word
            go1 = list(secret)
            go2 = list(ser)
            for i in range(len(go2)):
                if go2[i] == guess:
                    go1[i] = guess
                    go2[i] = "-"
                    num -= 1
                secret = ''.join(go1)
                ser = ''.join(go2)
                found += guess
            break
        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1
            found += guess
            break


while True:
    word = data[random.randint(0, len(data) - 1)]
    num = len(word)
    attempts = 8
    secret = len(word) * "-"
    found = ""
    if menu() == True:
        while True:
            if stop() == False:
                break
            check()
    else:
        break
