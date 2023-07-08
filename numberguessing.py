import random
import sys


def main():
    number = generate_random()
    guessing(number)


def generate_random():
 while True:
    try:
        lower_range= int(input("Enter the lower range "))
        break
    except ValueError:
        print ("Enter integers only!!")
        continue
 while True:
    try:
        upper_range = int(input ("Enter the upper range "))
        if upper_range <= lower_range:
            print("Upper Range should be greater than lower range ")
            continue
        else:
            break
    except ValueError:
        print("Enter integers only!!")
 return (random.randrange(lower_range, upper_range))


def guessing (n):
    count =1
    while True:
        try:
            guessed_number= int(input("\n Guess the number "))
        except ValueError:
            print ("Enter integers only!!")
            continue
        if guessed_number == n:
            if count<=5:
                print(f"Congrats!! You guessed it in {count} attempts")
                sys.exit()
            else:
                print("Better luck next time, you took too long")
                sys.exit()
        elif guessed_number < n:
            print ("You guessed too low")
            count = count+1
            continue
        else:
            print ("You guessed too high")
            count= count+1
            continue


if __name__ == "__main__":
    main()
