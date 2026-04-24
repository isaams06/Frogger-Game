"""
File:    frogger.py
Author:  Isaam Sayed
Date:    22 November 2024
Section: 71
E-mail:  isaams1@umbc.edu
Description:
  Program lets use play frogger game, where frog must avoid cars and get to the other side
  similar to modern day crossy road.
"""


import os

root, directories, files = next(os.walk('.'))

#frog = '\U0001F438'  # the emoji one
frog = '\U0001318F'  # the hieroglyphic one


def select_game_file():

    #function lets user choose file from directory
    list_frogs = []
    for i in files:
        if i.split('.')[1] == "frog":
            list_frogs.append(i)

    for i in range(len(list_frogs)):
        print(f"{[i + 1]} {list_frogs[i]}")

    game_option = int(input("Enter an option: "))
    #validation check for valid file input
    while game_option > len(list_frogs):
        print("Invalid input. Please choose a valid file number.. ")
        game_option = int(input("Enter an option: "))

    if game_option:
        option_number = int(game_option)
        if 1 <= option_number <= len(list_frogs):
            selected_file = list_frogs[option_number - 1]

            #open the selected file and read lines
            with open(selected_file, "r") as my_file:
                the_lines = my_file.readlines()

            #allows first line values to be saved in variables till needed
            first_line = the_lines[0].strip().split()
            num_rows = int(first_line[0])
            num_columns = int(first_line[1])
            num_jumps = int(first_line[2])

            speeds = []
            for speed in the_lines[1].strip().split():
                speeds.append(int(speed))

            map_rows = []
            #lines 2 onwards are appended to map
            for line in the_lines[2:]:
                map_rows.append(line.strip())

            #dictionary to store values from files
            game_dict = {
                "num_rows": num_rows,
                "num_columns": num_columns,
                "num_jumps": num_jumps,
                "speeds": speeds,
                "map_rows": map_rows
            }

            return game_dict


def board_print(game_file, frog_row, frog_col):

    #print the frog row separately
    map_rows = game_file["map_rows"]

    if frog_row == -1:  #only runs when frog starts at row -1
        above_map_row = " " * frog_col + frog + " " * (game_file["num_columns"] - frog_col - 1)
        print(above_map_row)

    for row_index in range(len(map_rows)):
        row_str = ""
        for col_index in range(len(map_rows[row_index])):
            if row_index == frog_row and col_index == frog_col:  # froggy's position printed
                row_str += frog
            else:
                row_str += map_rows[row_index][col_index]  # otherwise continues w printing like orig file
        print(row_str)  # Print the row with or without the frog
    if frog_row == game_file["num_rows"]:  #handles printing frog below map (win condition)
        below_map_row = " " * frog_col + frog + " " * (game_file["num_columns"] - frog_col - 1)
        print(below_map_row)

    print()


def rotate_map(map_rows, speeds):

    #rotates each row based on corresponding speed stored in dictionary from earlier
    for i in range(len(map_rows)):
        speed = speeds[i]
        row = map_rows[i]
        #allows it to make a right rotation
        map_rows[i] = row[-speed:] + row[:-speed]


def check_collision(game_file, new_row, new_col):

    #function used to determine if x is at same index as frog
    if 0 <= new_row < game_file["num_rows"]:
        row_content = game_file["map_rows"][new_row]
        return row_content[new_col] == "X"
    return False


def frogger_game(game_file):

    frog_row = -1  #frog starts above the map
    frog_col = game_file["num_columns"] // 2
    move_count = 1

    board_print(game_file, frog_row, frog_col)

    while True:
        move = input("Move (WASDJ): ").lower()
        move_count += 1
        print(f"Move count: {move_count}")

        if move == "":
            rotate_map(game_file["map_rows"], game_file["speeds"])
        elif move not in ['w', 'a', 's', 'd'] and move[0] != "j":
            print("Invalid move. Use WASDJ.")
        else:
            #rotate the map first before froggy moves
            rotate_map(game_file["map_rows"], game_file["speeds"])

            #determines new frog position
            new_row = frog_row
            new_col = frog_col

            if move == "w" and frog_row > -1:
                new_row -= 1
            elif move == "s":
                new_row += 1
                #check if frog has moved past the last row
                if new_row >= game_file["num_rows"]:
                    frog_row = new_row  #updates frog's position
                    board_print(game_file, frog_row, frog_col)
                    print("You won, Frog lives to cross another day.")
                    return
            elif move == "a" and frog_col > 0:
                new_col -= 1
            elif move == "d" and frog_col < game_file["num_columns"] - 1:
                new_col += 1
            elif move[0] == "j":
                values_j = move.split()

                if (len(values_j) == 3 and
                        values_j[1] and values_j[2] and
                        game_file["num_jumps"] > 0):

                    new_row = int(values_j[1]) - 1
                    new_col = int(values_j[2]) - 1

                    if (0 <= new_row <= game_file["num_rows"] and
                    0 <= new_col <= game_file["num_columns"] and
                    (new_row == frog_row - 1 or new_row == frog_row or new_row == frog_row + 1)):

                        #if valid it moves frogs position and removes 1 from # of jumps allows
                        frog_row = new_row
                        frog_col = new_col
                        game_file["num_jumps"] -= 1


                    else:
                        print("position not in valid bounds")
                        new_row = frog_row  #keeps at current position
                        new_col = frog_col
                else:
                    print("Invalid. You either ran out of jumps or did not enter column and row value after j")




            #collision check after frog moves
            if check_collision(game_file, new_row, new_col):
                frog_row = new_row
                frog_col = new_col
                board_print(game_file, frog_row, frog_col)
                print("You Lost, Sorry Frog")
                return

            #updates frog move if valid and no collision
            frog_row = new_row
            frog_col = new_col

        #collision check even if no move, but board rotates
        if check_collision(game_file, frog_row, frog_col):
            board_print(game_file, frog_row, frog_col)  #shows last move where collision occurs
            print("You Lost, Sorry Frog")
            return

        #prints updated board
        board_print(game_file, frog_row, frog_col)


if __name__ == '__main__':
    selected_game_file = select_game_file()
    frogger_game(selected_game_file)
