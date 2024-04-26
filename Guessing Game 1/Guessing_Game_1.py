import random
print("Enter your desired limit to be able to make a guess: ")
user_input = int(input("Enter something: "))
if user_input <= 100:  # Set your desired limit
    def play():
        x = random.randint(1, user_input)

        guess = int(input("Guess a number between 1 and your desired limit: "))
        while True:
            if guess > x:
                print("Sorry, unfortunately your guess was too high. Try again!")
                guess = int(input("Guess a number between 1 and your desired limit: "))
            elif guess < x:
                print("Sorry, unfortunately your guess was too low. Try again!")
                guess = int(input("Guess a number between 1 and your desired limit: "))
            else:
                print("WooHoo!! You got it correct!")
                break
    play()
    answer = input("Do you want to play again? (yes/no): ")
    if answer.lower() == 'yes':
        print("Let's play again!\n")
        play()
else:
    print("Input too long. Please try again.")
