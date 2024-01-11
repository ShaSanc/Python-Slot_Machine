import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "Z": 2,
    "A": 4,
    "B": 6,
    "C": 8,
}

def check_winnings(coloumns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = coloumns[0][line]
        for column in coloumns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            
    return winnings
            

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                 print(column[row], end="")
                 
        print()



def deposit():
    while True:
        amount = input("How much money would you like to deposit ?")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("ENTER THE NUMBER OF LINES TO BET ON.(1-" + str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
            
    return lines

def get_bet():
      while True: 
        amount = input("What would you like to bet on each line ?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")
            
        return amount
    
def main():
    balance = deposit()
    string = get_number_of_lines()
    print = (balance, string)
    while True:
        bet = get_bet()
        total_bet= bet * string
        
        if total_bet > balance:
            print("You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
            
    print(f"You are betting ${bet} on {string} lines. Total bet is equal to: ${total_bet}")
    
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
main()