import random 

print("I am thinking of a number between 1 and 20.")
random_number = random.randint(1,20)
i=0

while True:
    i+=1
    guess_number = int(input("Take a guess!\n"))
    if(guess_number<random_number):
        print("Your guess is too low.")
    elif(guess_number>random_number):
        print("Your guess is too high.")
    else:
        print('Good job! Your guessed my number in {} guesses!'.format(i))
        break