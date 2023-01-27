def check():
    global game
    result = 0
    # Search for horizontal line
    if "XXX" == game[:3] or "XXX" == game[3:6] or "XXX" == game[6:9]:
        result += 1
    # Search for vertical line
    if "XXX" == game[::3] or "XXX" == game[1::3] or "XXX" == game[2::3]:
        result += 1
    # Search for diagonal line:
    if "XXX" == game[::4] or "XXX" == game[2:7:2]:
        result += 1
    # The same but with O
    if "OOO" == game[:3] or "OOO" == game[3:6] or "OOO" == game[6:9]:
        result += 2
    if "OOO" == game[::3] or "OOO" == game[1::3] or "OOO" == game[2::3]:
        result += 2
    if "OOO" == game[::4] or "OOO" == game[2:7:2]:
        result += 2
    # who wins
    if result == 0 and " " not in game:
        print("Draw")
        return False
    if result == 1:
        print("X wins")
        return False
    if result == 2:
        print("O wins")
        return False
    return True


def coordinates(move):
    global game
    global letter
    global x
    # translate input to the matrix index
    match move:
        case 11:
            x = 0
        case 12:
            x = 1
        case 13:
            x = 2
        case 21:
            x = 3
        case 22:
            x = 4
        case 23:
            x = 5
        case 31:
            x = 6
        case 32:
            x = 7
        case 33:
            x = 8
    # update game output with the last move
    if game[x] == " ":
        game = game[:x] + letter + game[x + 1:]
        print("---------")
        print("|", game[0], game[1], game[2], "|", sep=" ")
        print("|", game[3], game[4], game[5], "|", sep=" ")
        print("|", game[6], game[7], game[8], "|", sep=" ")
        print("---------")
    else:
        print("This cell is occupied! Choose another one!")
    # give move to other player
    if letter == "X":
        letter = "O"
    else:
        letter = "X"


def play():
    global move
    global x
    move = input()
    x = move.replace(" ", "")
    try:
        move = int(x)
    except ValueError:
        print("You should enter numbers!")
    else:
        if 1 <= move % 10 <= 3 and 1 <= move // 10 <= 3:
            coordinates(move)
        else:
            print("Coordinates should be from 1 to 3!")


letter = "X"
x = 0
game = "         "
print("---------")
print("|", game[0], game[1], game[2], "|", sep=" ")
print("|", game[3], game[4], game[5], "|", sep=" ")
print("|", game[6], game[7], game[8], "|", sep=" ")
print("---------")

while check() == True:
    play()
