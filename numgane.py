import random

def main():
    ranges = int(input("Set a range Number: "))
    lives = 3  
    numer = randomers(ranges)

    print(numer)
    while lives > 0:
        guess = int(input("Guess the number "))

        if guess == numer:
            print("you win!!")
            break
        else:
            print("wrong ")
            lives -= 1

    print("out of lives")


def randomers(num):
    
    numbers = random.randrange(0,num)
    return numbers

main()

    