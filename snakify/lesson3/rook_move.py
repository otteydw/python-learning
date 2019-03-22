# https://snakify.org/en/lessons/if_then_else_conditions/problems/

# Chess rook moves horizontally or vertically. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.
# The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.

startx = int(input('Start X: '))
starty = int(input('Start Y: '))
endx = int(input('Start X: '))
endy = int(input('Start Y: '))

if startx == endx or starty == endy:
    print('YES')
else:
    print('NO')
