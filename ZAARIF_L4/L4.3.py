def print_tic_tac_toe(values):
    print("\n")
    print("\t    |    |")
    print("\t  {} | {}  | {}".format(values[0], values[1], values[2]))
    print('\t____|____|____')

    print("\t    |    |")
    print("\t {}  | {}  | {}".format(values[3], values[4], values[5]))
    print('\t____|____|____')

    print("\t    |    |")

    print("\t {}  | {}  | {}".format(values[6], values[7], values[8]))
    print("\t    |    |")
    print("\n")



def single_game(cur_player):
    values = [' ' for x in range(9)]
    player_pos = {'X': [], '0': []}
    print_tic_tac_toe(values)




print_tic_tac_toe([' ' for x in range(9)])

while True:
    print_tic_tac_toe(values)

try:
    print("Player ", cur_player, " turn. Which box? : ", end="")
    move = int(input())
except ValueError:
    print("Wrong input!!! Try Again")
    continue

if move < 1 or move > 9:
    print("Wrong input!!! Try Again")
    continue

if values[move - 1] != ' ':
    print("Place already filled. Try!!")
    continue

    values[move - 1] = cur_player

    player_pos[cur_player].append(move)

def check_win(player_pos, cur_player):
    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9]
            [1, 5, 9], [3, 5, 7]]

    for x in soln
        if all(y in player_pos[cur_player] for y in x)
            return False

if check_win(player_pos, cur_player):
    print_tic_tac_toe(values)
    print("Player ", cur_player, "has won the game")
    print("\n")
    return cur_player

if check_draw(player_pos)
    print("Game Draw")
    print("\n")
    return 'D'

    if cur_player == 'X':
        cur_player = 'O'
    else:
        cur_player = 'X'

if __name__ == "main":

    print("Player 1")
    player1 = input("enter the name : ")
    print("\n")

    print("Player 2")
    player2 = input("Enter the name : ")
    print("\n")

    cur_player = player1
    player_choise = {'X': "", 'O': ""}
    options = ['X', 'O']

def print_scoreboard(score_board):
    print("\t-------------------------")
    print("\t       SCOREBOARD        ")
    print("\t-------------------------")

    player = list(score_board.keys())
    print("\t  ", players[0], "\t   ", score_board[players[0]])
    print("\t  ", players[1], "\t   ", score_board[players[1]])

    print("\t-------------------------\n")

    score_board = {player1: 0, player2: 0}
    print_scoreboard(score_board)

    while True:

        print("Turn to choose for", cur_player)
        print("Enter 1 for X")
        print("Enter 2 for O")
        print("Enter 3 for Quit")

try:
    choice = int(input())
except ValueError:
    print("Wrong Input!!! Try Again\n")
    continue

if choice == 1:
    player_choise['X'] = cur_player
    if cur_player == player1:
        player_choise['O'] = player2
    else:
        player_choise['O'] = player1
