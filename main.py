import random

initial_balance = 1000
initial_bet = 10

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
            #chosen_color = random.choice(['Red', 'Black'])
            chosen_color = 'Red'
            if print_output:
                print(f"You have chosen {chosen_color}")
            if self.color == chosen_color:
                return amount * 2 - amount
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
            if print_output:
                print("Invalid bet type.")
            return 0

# Example usage:
roulette = Roulette()

# Prompt user for the number of simulations and whether to print intermediate results
num_simulations = int(input("How many simulations would you like to run? "))
sim_no = 0
print_output = input("Do you want to print intermediate results? (yes/no): ").strip().lower() == 'yes'

total_final_balance = 0
simulations_won = 0
simulations_lost = 0

for sim in range(num_simulations):
    sim_no += 1
    if print_output:
        print(f"\nStarting simulation {sim + 1}...")
    balance = initial_balance
    amount = initial_bet
    play_no = 0
    playing = True

    while playing:
        play_no += 1
        if print_output:
            print("\n--------------------")
            print(f"Play number: {play_no}")
            print(f"Current balance: ${balance}")
            print(f"Next bet amount: ${amount}")

        if amount > balance:
            if print_output:
                print("Insufficient balance!")
            keep_playing = False

        winnings = roulette.bet('color', amount)
        roulette.spin()
        if print_output:
            print(f"The ball landed on {roulette.pocket_number} {roulette.color}.")
        balance += winnings

        if winnings > 0:
            amount = initial_bet
            if print_output:
                print(f"You won ${winnings}!")
        else:
            amount = amount * 2
            if print_output:
                print(f"You lost ${-winnings}.")

        if balance <= 0:
            total_final_balance -= initial_balance
            print(f"Simulation: {sim_no}. Play number: {play_no}. Final balance: ${balance}. Current total balance: ${total_final_balance}")
            playing = False
            simulations_lost += 1
        else:
            keep_playing = True

        if play_no > 100:
            playing = False
            if balance > initial_balance:
                simulations_won += 1
                total_final_balance += balance - initial_balance
                print(f"Simulation: {sim_no}. Play number: {play_no}. Final balance: ${balance}. Current total balance: ${total_final_balance}")
            else:
                total_final_balance -= initial_balance
                simulations_lost += 1

# Summary of all simulations
print("\n====================")
print(f"Simulations complete.")
print(f"Total simulations run: {num_simulations}")
print(f"Simulations won: {simulations_won}")
print(f"Simulations lost: {simulations_lost}")
print(f"Initial balance: ${initial_balance}")
print(f"Initial bet amount: ${initial_bet}")
print(f"Final balance after all simulations: ${total_final_balance}")
