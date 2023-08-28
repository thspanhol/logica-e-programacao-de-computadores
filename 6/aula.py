#count = 10
#while count > 0:
#    print(count)
#    count -= 1
#print("Lançamento!")

import random

number_to_guess = random.randint(1, 100)
guessed = False

while not guessed:
    guess = int(input("Tente adivinhar o número: "))
    if guess == number_to_guess:
        print("Parabéns, você acertou!")
        guessed = True
    elif guess < number_to_guess:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")