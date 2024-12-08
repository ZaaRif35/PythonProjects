fighters = []
heal_power = 10


# Define characters class to represent player attributes
class characters:
    def __init__(self, Name, Hp, Armor, Power):
        self.Name = Name
        self.Hp = Hp  # Set the HP directly, no addition here
        self.Armor = Armor
        self.Power = Power


# Define game class that extends characters and handles actions like healing and being attacked
class game(characters):
    def heal(self):
        global heal_power
        self.Hp += heal_power  # Increase HP by heal_power
        print(self.Name + " healed and now has ", self.Hp, "Hp left")

    def attacked(self, Damage):
        if self.Hp - Damage > 0:
            self.Hp -= Damage
            print(self.Name + " has ", self.Hp, "Hp left")
            return True
        else:
            print(self.Name, " is dead")
            return False


# Taking input for number of characters
while True:
    try:
        nr = int(input("How many characters are in the game? "))
        if nr < 2:
            print("At least 2 characters are required!")
            continue
        break
    except:
        print("Invalid input! Please enter a number.")
        continue

# Collect data for each character
for i in range(nr):
    name = input("Name of character: ")
    Hp = int(input("HP: "))
    Armor = int(input("Armor: "))
    Power = int(input("Power: "))
    fighters.append(game(name, Hp, Armor, Power))

# Set the first two players as the ones fighting
player1 = fighters[0]
player2 = fighters[1]

cur_player = player1
next_player = player2

alive = True

# Main game loop
while alive:
    print(f"\nIt's {cur_player.Name}'s turn!")
    print("1. Attack the other player")
    print("2. Heal")
    print("3. Continue (skip turn)")

    try:
        move = int(input("Choose an action: "))
    except:
        print("Invalid choice, try again.")
        continue

    if move == 1:
        # Attack the other player
        damage = cur_player.Power  # Assuming Power is the damage value
        alive = next_player.attacked(damage)
        if not alive:  # If the opponent is dead, game ends
            print(f"{cur_player.Name} wins!")
            break
    elif move == 2:
        # Heal the current player
        cur_player.heal()
    elif move == 3:
        print(f"{cur_player.Name} skips their turn.")
    else:
        print("Invalid choice, try again.")
        continue

    # Switch turns
    if cur_player == player1:
        cur_player = player2
        next_player = player1
    else:
        cur_player = player1
        next_player = player2
