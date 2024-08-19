import random
import time


class Roulette:
    def __init__(self):
        self.pocket_number = None
        self.color = None

    def spin(self):
        self.pocket_number = random.randint(0, 36)
        self.color = self.determine_color(self.pocket_number)
        return self.pocket_number, self.color

    def determine_color(self, number):
        if number == 0:
            return 'Green'
        elif number in (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36):
            return 'Red'
        else:
            return 'Black'

    def bet(self, bet_type, amount):
        if bet_type == "number":
            chosen_number = int(input("Choose a number between 0 and 36: "))
            if self.pocket_number == chosen_number:
                return amount * 35
            else:
                return -amount
        elif bet_type == "color":
            chosen_color = random.choice(['Red', 'Black'])
            print(f"you have chosen {chosen_color}")
            if self.color == chosen_color:
                return amount * 2
            else:
                return -amount
        elif bet_type == "odd_even":
            chosen_type = input("Choose Odd or Even: ").capitalize()
            if (self.pocket_number != 0 and
               ((chosen_type == "Odd" and self.pocket_number % 2 != 0) or
                (chosen_type == "Even" and self.pocket_number % 2 == 0))):
                return amount * 2
            else:
                return -amount
        else:
            print("Invalid bet type.")
            return 0


# Example usage:
roulette = Roulette()
balance = 100
initial_bet = 10 
playing = True

amount = initial_bet
play_no = 0

while playing:
    play_no += 1
    print("\n--------------------")
    print(f"Play number: {play_no}")
    print(f"Current balance: ${balance}")
    bet_type = 'color'
    
    if amount > balance:
        print("Insufficient balance!")
        keep_playing = False

    winnings = roulette.bet(bet_type, amount)

    roulette.spin()
    print(f"The ball landed on {roulette.pocket_number} {roulette.color}.")

    balance += winnings

    if winnings > 0:
        amount = initial_bet
        print(f"You won ${winnings}! Current Balance: ${balance}")
    else:
        amount = amount * 2
        print(f"You lost ${-winnings}.")
    
    print(f"Next bet amount: ${amount}")

    if balance <= 0:
        print("You're out of money! Game over.")
        playing = False
    else:
        keep_playing = True
        time.sleep(3)
