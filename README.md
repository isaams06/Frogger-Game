# Frogger Game (Python)

## Project Overview
This project is a implementation of a Frogger game written in Python. Player controls a frog that must safely cross a map filled with moving obstacles. 
The map is loaded from external files, which (I also provided) define the board layout, obstacle speeds, and number of allowed jumps.


## How to Run:
```
python3 frogger.py
```

## Sample Output:
```
[1] game1.frog
[2] game2.frog
[3] game3.frog
Enter an option: 1
        𓆏       
XXX__XX___XX____
XX__XX___XXX__X_
_XX__XXXX_XX_XX_

Move (WASDJ): s
Move count: 2
_XXX__XX𓆏__XX___
X_XX__XX___XXX__
XX__XX__XXXX_XX_

Move (WASDJ): s
Move count: 3
__XXX__XX___XX__
__X_XX__𓆏X___XXX
XX_XX__XX__XXXX_

You Lost, Sorry Frog
