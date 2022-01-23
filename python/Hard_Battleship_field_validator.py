# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
'''
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a
valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array.
Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players.
Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by
targetting individual cells on his field. The ship occupies one or more cells in the grid.
Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.


Before the game begins, players set up the board and place the ships accordingly to the following rules:
There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1).
Any additional ships are not allowed, as well as missing ships.
Each ship must be a straight line, except for submarines, which are just single cell.
'''

def validate_battlefield(field):
    coords = set()
    coord = []

    for indexi, i in enumerate(field):
        for indexj, j in enumerate(i):

            if field[indexj][indexi] == 1:
                if f"[{indexj},{indexi}]" not in coords:
                    coords.add(f"[{indexj},{indexi}]")
                    coord.append([indexj, indexi])
    coord.sort()
    shipnames = set()
    ship = dict()

    for index, i in enumerate(coord):
        # Check if they have one variable in common (i, j) if so, add to the parent object
        #  if not in ship, add to ship and reference itself. create ship object named itself and add to list
        # check up left right. If found in ship, add this coordinate to the ship object
        '''
        y: i[0]
        x: i[1]
        '''
        shipnames.add(f"[{i[0]},{i[1]}]")
        if f"[{i[0] - 1},{i[1] - 1}]" in shipnames or f"[{i[0] - 1},{i[1] + 1}]" in shipnames or f"[{i[0] + 1},{i[1] - 1}]" in shipnames or f"[{i[0] + 1},{i[1] + 1}]" in shipnames:
            return False
        if f"[{i[0] - 1},{i[1]}]" in shipnames:
            # Do something Left
            ship[f"[{i[0]},{i[1]}]"] = ship[f"[{i[0] - 1},{i[1]}]"]
        elif f"[{i[0]},{i[1] - 1}]" in shipnames:
            ship[f"[{i[0]},{i[1]}]"] = ship[f"[{i[0]},{i[1] - 1}]"]

        else:
            ship[f"[{i[0]},{i[1]}]"] = f"[{i[0]},{i[1]}]"
    shiptrails = dict()

    for key, val in ship.items():
        if val not in shiptrails:
            key = key.strip('][').split(', ')
            key[0] = list((int(key[0][0]), int(key[0][2])))
            key = key[0]
            shiptrails[val] = [key]
        else:
            key = key.strip('][').split(', ')
            key[0] = list((int(key[0][0]), int(key[0][2])))
            key = key[0]
            shiptrails[val].append(key)
    H = True
    V = not H
    isFalse = False
    if len(shiptrails) != 10:
        return False
    ace = []
    for i in shiptrails:
        ace.append([len(shiptrails[i])])
    ace.sort()

    for i in shiptrails:
        for j, x in enumerate(shiptrails[i]):
            if len(shiptrails[i]) <= 2:
                break
            if x[0] != shiptrails[i][-1][0] and x[1] != shiptrails[i][-1][1]:
                isFalse = True

            if isFalse:
                break
        if isFalse:
            break

    return not isFalse and ace.count([1]) == 4 and ace.count([2]) == 3 and ace.count([3]) == 2 and ace.count([4]) == 1
# This was the most exciting problem I have solved so far! It took me about 3 hours to complete
# I initially wanted to create a separate ship object to do the comparison but after more planning and drawing I noticed that I did not have to
