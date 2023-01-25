def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input("3: "))
    rem5 = int(input("5: "))
    rem7 = int(input("7: "))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input("Give me a number: "))
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("What is the best programming language?")
    print("1. Java")
    print("2. C#")
    print("3. Python")
    print("4. PHP")
    i = 0
    while i != 1:
        if int(input()) == 3:
            i = 1
        else:
            print("No, of course not!")
    print('Well done! :D')
    print()


def question():
    stop = 0
    while stop != 1:
        print()
        print("Do you want something else?")
        print("1. Christmas tree!")
        print("2. Are you AI?")
        print("3. Calculate the derivative.")
        print("4. Nope")
        print()
        i = int(input())
        match i:
            case 1:
                print("Ok, let's started!")
                # Set the number of rows for the tree
                num_rows = int(input("Give me the number of rows for the tree:"))
                # Use a for loop to print each row of the tree
                for i in range(num_rows):
                    # Calculate the number of spaces to print before the asterisks
                    num_spaces = num_rows - i - 1
                    # Print the spaces
                    print(" " * num_spaces, end="")
                    # Calculate the number of asterisks to print
                    num_asterisks = 2 * i + 1
                    # Print the asterisks
                    print("*" * num_asterisks)
                # Print the base of the tree
                print(" " * (num_rows - 1) + "*")
            case 2:
                print("Well, I am a human-generated chatbot. Beep.")
            case 3:
                print("Wow, a math freak!")
                print("Fine. Please, use the pattern ax^n + bx^m + c")
                a, n = int(input("a: ")), int(input("n: "))
                b, m, c = int(input("b: ")), int(input("m: ")), int(input("c: "))
                print("f'(x)= ", a * n, "x^", n - 1, " + ", b * m, "x^", m - 1, sep="")
                print("I did it, yeah!")
            case 4:
                print("Serious?")
                print("1. Yep")
                print("2. No, it was a mistake.")
                if int(input()) == 1:
                    stop = 1
                    print("Got it!")
                    print()


def end():
    print('Have a nice day!')


greet('Hoffy', '2023')  # change it as you need
remind_name()
guess_age()
count()
test()
question()
end()
