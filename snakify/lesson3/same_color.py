# https://snakify.org/en/lessons/if_then_else_conditions/problems/

# Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
# The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

square1x = int(input('Sqaure1 X: '))
square1y = int(input('Sqaure1 Y: '))
square2x = int(input('Sqaure2 X: '))
square2y = int(input('Sqaure2 Y: '))

# BLACK = COLUMN ODD, ROW ODD OR COLUMN EVEN, ROW EVEN

if square1x % 2 == square1y % 2:
    square1_color = 'black'
else:
    square1_color = 'white'

if square2x % 2 == square2y % 2:
    square2_color = 'black'
else:
    square2_color = 'white'

if square1_color == square2_color:
    print("YES")
else:
    print("NO")
