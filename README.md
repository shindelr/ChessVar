ChessVar README
ChessVar
Robin Shindelman
8/29/2023
Welcome to ChessVar!
I initially created the 'backend' of this game as the final project in my second ever computer science class at OSU. To get full credit, we weren't required to implement anything resembling a user interface or even a particularly simple way for a user to interact with the game. However, upon completing what was at the time my most complex project to date, It felt a shame to leave the thing without a face.
So, without further adieu, here is my first ever attempt at creating anything resembling a finished piece of software!!
How To Play:
The game is won by racing your King to the final row of the board before your opponent can do the same.
-White always goes first. Thus, if the White King is the first to make it to the final row, the Black team has one more turn to do the same, resulting in a tie.
-Pieces may not occupy the same square as another piece unless the pieces are on opposite teams, in which case the non-moving piece will be captured.
-A piece must be moved on your turn, picking a piece up and then placing it down in the same exact square is considered illegal.
Hot Keys:
R -- Restart the game at any point.
U -- Undo the current move, only works if the piece has not already been "placed".
Move rules:
King:
Can move one square in any direction, diagonally, horizontally, or vertically.
IMPORTANT: The King cannot be placed in check (become vulnerable to capture) by either the King's opponent or owner. This means that the King can never be captured by its opponent, nor can any other piece be placed in a position where capture would be possible.
Can capture any opponent piece occupying its destination square.
Cannot jump other pieces.


Rook:
Can move as far as possible horizontally or vertically, but not diagonally. Can capture any opponent piece occupying its destination square. Cannot jump other pieces.


Bishop:
Can move as far as possible, but only diagonally.
Can capture any opponent piece occupying its destination square. Cannot jump other pieces.


Knight:
Can move in a L shape.
Two squares horizontally/vertically, then one square perpendicularly to the first two squares. Or, the Knight can move one square horizontally/vertically, then two squares perpendicularly to the original path.
Can capture any opponent piece occupying its destination square.
Can jump any piece
 
 Enjoy!
