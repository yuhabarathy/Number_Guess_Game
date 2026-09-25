import random
class Game:
    def __init__(self, name, target, max_attempts=5):
        self.name = name
        self.target = target
        self.max_attempts = max_attempts
        self.computer_number = random.randint(1, target)
        self.attempt_count = 0

    def greet(self):
        print(f"\nWelcome {self.name}!")

    def instructions(self):
        print("\n========== Instructions ==========\n")
        print("1. The computer chooses a random number between 1 and your maximum number.")
        print("2. You must guess the secret number.")
        print("3. The game will tell you if your guess is too high or too low.")
        print(f"4. You have {self.max_attempts} attempts.")
        print("5. The game ends when you find the number or run out of attempts.")
        print("6. You can choose to play again.\n")

    def game_start(self):
        print(f"The computer has chosen a number between 1 and {self.target}.")

        while self.attempt_count < self.max_attempts:

            try:
                guess = int(input("\nGuess the number: "))

                if guess < 1 or guess > self.target:
                    print(f"Please enter a number between 1 and {self.target}.")
                    continue

            except ValueError:
                print("Please enter a valid number.")
                continue

            self.attempt_count += 1

            if guess > self.computer_number:
                print("Too High!")

            elif guess < self.computer_number:
                print("Too Low!")

            else:
                print("\nYou found the secret number!")
                print(f"The number was: {self.computer_number}")
                print(f"Total attempts: {self.attempt_count}")
                return True

        print("\nYou ran out of attempts!")
        print(f"The secret number was: {self.computer_number}")
        return False


def main():
    print("========== NUMBER GUESSING GAME ==========")
    while True:
        name = input("\nEnter Player Name: ")
        try:
            target = int(input("Enter a maximum number: "))
            if target < 2:
                print("Please enter a number greater than 1.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        player = Game(name, target)
        player.greet()
        player.instructions()
        player.game_start()

        play_again = input("\nWould you like to play again? (yes/no): ").lower()

        if play_again != "yes":
            print("\nThanks for playing!")
            break
        
main()