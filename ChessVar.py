# Author: Robin Shindelman
# GitHub Username: shindelr
# Date: 08/07/23
# Description: This program is a simulation of a variant of Chess. The two players are signified by white and black
# pieces. The types of pieces are  King, Bishop, Rook, and Knight. Each type of piece has its own set of rules for
# movement and capturing other pieces. There is also a board, through which the user can know the location of all the
# pieces in the game, whose turn it is, and know where the edges of the board are. The class ChessVar will keep track
# of the game state as informed by the board and also serve as the portal through which the user will make moves and
# interact with the game. The game can be won by either king being able to move all the way across the board and reach
# the last row. Though the game can tie if the other king also reaches the last row on its last turn.


class ChessVariant:
    """
    Keep track of current game state, announce the end of the game, allows the
    user to move their pieces, can request the state of the board from Board class,
    knows which player is which & whose turn it is. Informs board of the starting
    positions. Creates the board. Collaboration with Board piece movement and board
    visualization.
    """
    def __init__(self):
        self._board = Board()

    def make_move(self, origin, destination):
        """
        Allow user to move a piece on the board. The parameter 'origin' describes the
        square from which the piece is moving. 'destination' describes the square to which
        the piece is going. Returns False if the move is illegal, returns True otherwise.
        """
        if self._board.get_turn_state() == 'WHITE':
            if origin == destination:
                return False
            return self._board.set_white_piece_location(origin, destination)
        if self._board.get_turn_state() == 'BLACK':
            if origin == destination:
                return False
            return self._board.set_black_piece_location(origin, destination)

    def get_game_state(self):
        """
        Retrieve the current game state stored as one of ChessVar's data members. Can be any
        of the following strings: "WHITE_WON", "BLACK_WON", "TIE", or "UNFINISHED". Takes no
        parameters and returns whichever of the strings above that are the current setting.
        """
        return self._board.get_game_state()

    def get_board(self):
        """
        Retrieve a visual representation of the chessboard using the Board class. Takes no
        parameters and just returns a printed chessboard with the locations of all the pieces
        in play.
        """
        # print(self._board.get_blank_board_layout())  # Turned off for testing
        #print(self._board.get_board_and_pieces())
        return self._board.get_board()

    def get_roster(self, white_or_black):
        """
        Retrieve the team roster for either White or Black.
        :param white_or_black: Input "WHITE" for _white_dict & "BLACK" for _black_dict
        :return: The dictionary containing information about each team of pieces. Where
        {key : pieceObject}
        """
        if white_or_black == "BLACK":
            return self._board.get_roster('BLACK')
        if white_or_black == "WHITE":
            return self._board.get_roster('WHITE')

    def get_turn_state(self):
        """
        Return the current turn state of the game.
        """
        return self._board.get_turn_state()

    def __repr__(self):
        """
        Allows the debugger to show an object's attributes rather than its
        address in memory.
        """
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)


class Board:
    """
    Keep track of the state of the board (where pieces & edges are), Informs ChessVar
    of the game state per turn, removes a piece from active duty when captured,
    updates piece locations as ChessVar makes moves. Collaboration with Piece & ChesVar
    for things like game state, piece movement, and board representation.
    """
    def __init__(self):
        self._turn_state = "WHITE"  # White is default for first turn
        self._game_state = "UNFINISHED"  # May also be: "WHITE_WON", "BLACK_WON", "TIE"
        self._white_dict = [
                King('WHITE'),
                Bishop('WHITE', 1),
                Bishop('WHITE', 2),
                Rook('WHITE'),
                Knight('WHITE', 1),
                Knight('WHITE', 2)
        ]
        self._black_dict = [
                King('BLACK'),
                Bishop('BLACK', 1),
                Bishop('BLACK', 2),
                Rook('BLACK'),
                Knight('BLACK', 1),
                Knight('BLACK', 2)
            ]
        self._board = [  # Made non-private to be used easily by ChessVarGUI
            [('a', 8),('b', 8),('c', 8),('d', 8),('e', 8),('f', 8),('g', 8),('h', 8),],
            [('a', 7),('b', 7),('c', 7),('d', 7),('e', 7),('f', 7),('g', 7),('h', 7),],
            [('a', 6),('b', 6),('c', 6),('d', 6),('e', 6),('f', 6),('g', 6),('h', 6),],
            [('a', 5),('b', 5),('c', 5),('d', 5),('e', 5),('f', 5),('g', 5),('h', 5) ],
            [('a', 4),('b', 4),('c', 4),('d', 4),('e', 4),('f', 4),('g', 4),('h', 4),],
            [('a', 3),('b', 3),('c', 3),('d', 3),('e', 3),('f', 3),('g', 3),('h', 3) ],
            [('a', 2),('b', 2),('c', 2),('d', 2),('e', 2),('f', 2),('g', 2),('h', 2),],
            [('a', 1),('b', 1),('c', 1),('d', 1),('e', 1),('f', 1),('g', 1),('h', 1),]
        ]
        self._board_w_pieces = [
            [18, 28, 38, 48, 58, 68, 78, 88],  # 8
            [17, 27, 37, 47, 57, 67, 77, 87],  # 7
            [16, 26, 36, 46, 56, 66, 76, 86],  # 6
            [15, 25, 35, 45, 55, 65, 75, 85],  # 5
            [14, 24, 34, 44, 54, 64, 74, 84],  # 4
            [13, 23, 33, 43, 53, 63, 73, 83],  # 3
            [12, 22, 32, 42, 52, 62, 72, 82],  # 2
            [11, 21, 31, 41, 51, 61, 71, 81],  # 1
            #  a,  b,  c,  d,  e,  f,  g,  h
        ]

    def get_game_state(self):
        """
        Retrieve the current game state stored as one of ChessVar's data members. Can be any
        of the following strings: "WHITE_WON", "BLACK_WON", "TIE", or "UNFINISHED". Takes no
        parameters and returns whichever of the strings above that are the current setting.
        """
        return self._game_state

    def set_game_state(self, new_game_state):
        """
        Inform Board that the game state has changed, and therefore it should change
        its data member. Valid input to the new_game_state parameter may be: "WHITE_WON",
        "BLACK_WON", "TIE", or "UNFINISHED". Returns nothing.
        """
        if new_game_state == "WHITE_WON":
            self._game_state = "WHITE_WON"
        if new_game_state == "BLACK_WON":
            self._game_state = "BLACK_WON"
        if new_game_state == "TIE":
            self._game_state = "TIE"
        if new_game_state == 'UNFINISHED':
            self._game_state = 'UNFINISHED'

    def get_turn_state(self):
        """
        Retrieve the game's current turn state.
        :return: board's self._turn_state.
        """
        return self._turn_state

    def get_roster(self, white_or_black):
        """
        Retrieve the team roster for either White or Black.
        :param white_or_black: Input "WHITE" for _white_dict & "BLACK" for _black_dict
        :return: The dictionary containing information about each team of pieces. Where
        {key : pieceObject}
        """
        if white_or_black == "BLACK":
            return self._black_dict
        if white_or_black == "WHITE":
            return self._white_dict

    def get_blank_board_layout(self):
        """
        Retrieve the board in its current layout. Takes no parameters and returns
        the board as well as the positions of all the pieces.
        """
        for row in self._board:
            print(f'{row}\n')

    def get_board(self):
        """
        Retrieve the self._board data member.
        """
        return self._board

    def get_board_and_pieces(self):
        """
        Retrieve the game's current board layout, including all the pieces
        and their positions.
        """
        column_key = [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7)]

        for piece in self._white_dict:  # Write locations of all white pieces.
            if piece.get_location() is not None:
                loc_tuple = piece.get_location()
                piece_row = abs(loc_tuple[1] - 8)  # Establish nesting index.
                for location in column_key:
                    if loc_tuple[0] in location:  # Establish inner index.
                        piece_column: int = location[1]
                self._board_w_pieces[piece_row][piece_column] = piece.get_symbol()

        for piece in self._black_dict:  # Write locations of all black pieces.
            if piece.get_location() is not None:
                loc_tuple = piece.get_location()
                piece_row = abs(loc_tuple[1] - 8)  # Establish nesting index.
                for location in column_key:
                    if loc_tuple[0] in location:  # Establish inner index.
                        piece_column = location[1]
                self._board_w_pieces[piece_row][piece_column] = piece.get_symbol()

        for row in self._board_w_pieces:
            print(f'{row}\n')

    def set_turn_state(self, new_state):
        """
        Set the status of the turn state.
        :param new_state: Either 'WHITE' or 'BLACK'
        :return: None.
        """
        self._turn_state = new_state

    def set_white_piece_location(self, origin, destination):
        """
        Collaborate with ChessVar's make_move() method in order to move pieces around
        the board.
        :param origin: The square from which the piece is moving.
        :param destination: The square to which the piece is going.
        :return: False if move is illegal, otherwise: True, and update the
        piece's location, whose turn it is, removes any pieces that were captured,
        and if need be, updates the game state.
        """
        column_loc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        if self._turn_state == 'WHITE' and self.get_game_state() == 'UNFINISHED':  # White piece turn.
            for elem in self._white_dict:  # White piece is moving.
                # Is the piece actually at the origin and ACTIVE?
                if elem.get_location() is not None and elem.get_location() == (origin[0], int(origin[1])):
                    # On the board?
                    if destination[0] not in column_loc or int(destination[1]) < 0 or int(destination[1]) > 8:
                        print('That\'s off the board! Try again.')
                        return False

                    for opponent in self._black_dict:  # Square occupied by Black?
                        if opponent.get_location() == (destination[0], int(destination[1])):
                            if self.check_for_check(destination, origin, elem.get_symbol()) is True:
                                elem.set_location(destination)
                                self.remove_piece(opponent)
                                opponent.set_duty('CAPTURED')
                                self.set_turn_state('BLACK')
                                print(f'You\'ve captured {opponent.get_symbol()}! Nice job.')
                                print('It\'s Black player\'s turn now.')
                                return True
                            else:
                                return False

                    if self.check_square((destination[0], int(destination[1]))) == 'EMPTY':  # Square empty?
                        if self.check_for_check(destination, origin, elem.get_symbol()) is True:
                            elem.set_location(destination)
                            self.set_turn_state('BLACK')
                            print('It\'s Black player\'s turn now.')
                            return True
                        else:
                            return False

                    if 'WHITE' in self.check_square((destination[0], int(destination[1]))):  # Square has white piece?
                        print('Square occupied by your own team! Try again.')
                        return False
        return False  # Move failed.

    def set_black_piece_location(self, origin, destination):
        """
        Collaborate with ChessVar's make_move() method in order to move pieces around
        the board.
        :param origin: The square from which the piece is moving.
        :param destination: The square to which the piece is going.
        :return: False if move is illegal, otherwise: True, and update the
        piece's location, whose turn it is, removes any pieces that were captured,
        and if need be, updates the game state.
        """
        column_loc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        if self._turn_state == 'BLACK' and (self.get_game_state() == 'UNFINISHED' or self.get_game_state() == 'WHITE_WON'):  # Black piece turn
            for elem in self._black_dict:  # Black piece is moving.
                # Is the piece actually at the origin and ACTIVE?
                if elem.get_location() is not None and elem.get_location() == (origin[0], int(origin[1])):
                    # On the board?
                    if destination[0] not in column_loc or int(destination[1]) < 0 or int(destination[1]) > 8:
                        print('That\'s off the board! Try again.')
                        return False

                    for opponent in self._white_dict:  # Square occupied by White?
                        if opponent.get_location() == (destination[0], int(destination[1])):
                            if self.check_for_check(destination, origin, elem.get_symbol()) is True:
                                elem.set_location(destination)
                                self.remove_piece(opponent)
                                opponent.set_duty('CAPTURED')
                                self.set_turn_state('WHITE')
                                print(f'You\'ve captured {opponent.get_symbol()}! Nice job.')
                                print('It\'s White player\'s turn now.')
                                return True

                    if self.check_square((destination[0], int(destination[1]))) == 'EMPTY':  # Square empty?
                        if self.check_for_check(destination, origin, elem.get_symbol()) is True:
                            elem.set_location(destination)
                            self.set_turn_state('WHITE')
                            if self.get_game_state() == 'BLACK_WON' or self.get_game_state() == 'TIE':
                                print('Game over!')
                                return True
                            print('It\'s White player\'s turn now.')
                            return True

                    if 'BLACK' in self.check_square((destination[0], int(destination[1]))):  # Square has Black piece?
                        print('Square occupied by your own team! Try again.')
                        return False
        return False  # Move failed.

    def move_rules(self, origin, destination, piece, og_loc=None):
        """
        Define a series of test cases to determine whether the requested move is valid,
        depending on the unique behavior of this type of chess piece.
        :param origin: The square being moved from, 'letter + num'
        :param destination: The square being moved to, 'letter + num'
        :param piece: piece.get_symbol must have been called and passed.
        :param og_loc: Passed only by check_for_check as a way to look at king check rules.
        :return: True if move is legal, False if Illegal (including King being put into check).
        """
        bool_list = []
        column_key = [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7)]
        destination_loc = (destination[0], int(destination[1]))

        if og_loc is None:  # To account for a special case in the check_for_check function.
            # Get origin location
            if 'WHITE' in piece:
                for elem in self._white_dict:
                    if elem.get_location() == (origin[0], int(origin[1])):
                        og_loc = elem.get_location()
            if 'BLACK' in piece:
                for elem in self._black_dict:
                    if elem.get_location() == (origin[0], int(origin[1])):
                        og_loc = elem.get_location()

        # Translate letter columns to numbers using the column key, for origin piece
        for elem in column_key:
            if og_loc[0] in elem:  # Establish inner index.
                og_column_loc: int = elem[1]
        # For destination piece
        for elem in column_key:
            if destination_loc[0] in elem:
                destination_column_loc: int = elem[1]
                # Equals the number in the tuple of the corresponding letter in the column key.

        # Knight
        if 'Kn' in piece:
            bool_list = self.knight_move(destination, origin, destination_column_loc, og_column_loc,
                                         bool_list)
        # Bishop
        elif 'Bi' in piece:
            bool_list = self.bishop_move(destination, origin, destination_column_loc, og_column_loc,
                                         bool_list, piece)
        # Rook
        elif 'R' in piece:
            bool_list = self.rook_move(destination, origin, destination_column_loc, og_column_loc,
                                       bool_list, piece)
        # King
        elif 'K' in piece:
            self.king_move(destination, origin, destination_column_loc, og_column_loc,
                           bool_list, og_loc, destination_loc, piece)

        if False not in bool_list:
            bool_list.clear()
            return True
        return False

    def check_for_check(self, destination, origin, current_piece):
        """
        Check the destination square to make sure that the requested move does not
        place the opponent's King piece in check.
        :param destination: The square the current player's piece is moving to as 'letter + num'
        :param origin: The square the current player's piece is moving from as 'letter + num'
        :param current_piece: The 'owner + piece-type' symbol of the current player's piece
        :return: True if valid, False if illegal.
        """
        # King objects
        white_k = self.get_king('WHITE')
        black_k = self.get_king('BLACK')
        bool_list = []

        if self.get_turn_state() == 'BLACK':
            # Validating the entire basic movement rules here for the current piece.
            if self.move_rules(origin, destination, current_piece) is True:
                white_king_loc: tuple[str, int] = white_k.get_location()  # 'letter + num'
                # Could the current piece capture the King from the destination square?
                if self.move_rules(destination, white_king_loc, current_piece, og_loc=destination) is True:
                    bool_list.append(False)

                # Can anyone in the White roster capture the Black King?
                for elem in self._white_dict:
                    if elem.get_location() is None:  # Account for being in piece jail
                        bool_list.append('JAIL')
                    # If the piece moving is the King, can any opponent pieces move to where it's going on next turn?
                    elif current_piece == black_k.get_symbol():
                        if self.move_rules(elem.get_location(), destination, elem.get_symbol()) is True:
                            bool_list.append(False)  # If so, you can't move there, the King will be in danger.
                    elif self.move_rules(elem.get_location(), black_k.get_location(), elem.get_symbol()) is True:
                        bool_list.append(False)  # If so, that move is illegal.
                    else:
                        bool_list.append(True)
                # Can anyone in the Black roster capture the White King?
                for elem in self._black_dict:
                    if elem.get_location() is None:  # Account for being in piece jail
                        bool_list.append('JAIL')
                    elif self.move_rules(elem.get_location(), white_k.get_location(), elem.get_symbol()) is True:
                        bool_list.append(False)  # That move is illegal too.
                    else:
                        bool_list.append(True)
            else:
                return False

        if self.get_turn_state() == 'WHITE':
            # Validating the entire basic movement rules here for the current piece.
            if self.move_rules(origin, destination, current_piece) is True:
                black_king_loc: tuple[str, int] = black_k.get_location()  # 'letter + num'
                # Could the current piece capture the King from the destination square?
                if self.move_rules(destination, black_king_loc, current_piece, og_loc=destination) is True:
                    bool_list.append(False)

                # Can anyone in the White roster capture the Black King?
                for elem in self._white_dict:
                    if elem.get_location() is None:  # Account for being in piece jail
                        bool_list.append('JAIL')
                    elif self.move_rules(elem.get_location(), black_k.get_location(), elem.get_symbol()) is True:
                        bool_list.append(False)
                    else:
                        bool_list.append(True)
                # Can anyone in the Black roster capture the White King?
                for elem in self._black_dict:
                    if elem.get_location() is None:  # Account for being in piece jail
                        bool_list.append('JAIL')
                    # If the piece moving is the King, can any opponent pieces move to where it's going next turn?
                    elif current_piece == white_k.get_symbol():
                        if self.move_rules(elem.get_location(), destination, elem.get_symbol()) is True:
                            bool_list.append(False)  # If so, you can't move there, the King will be in danger.
                    elif self.move_rules(elem.get_location(), white_k.get_location(), elem.get_symbol()) is True:
                        bool_list.append(False)
                    else:
                        bool_list.append(True)
            else:
                return False

        if False not in bool_list and self.get_game_state() == 'UNFINISHED':  # Normal state of play. Mid-game
            bool_list.clear()
            return True
        elif False not in bool_list and self.get_game_state() != 'UNFINISHED':  # Legal endgame
            bool_list.clear()
            return True
        else:  # False in bool_list and game_state != 'UNFINISHED', set game state back to unfinished and continue.
            bool_list.clear()
            self.set_game_state('UNFINISHED')
            return False

        #if False not in bool_list:
         #   bool_list.clear()
          #  return True
        #return False

    def jump_rule(self, destination, origin, destination_column_loc, og_column_loc, bool_list, piece, og_loc=None):
        """
        Check for piece jump capability. Limits all pieces but the knight from jumping.
        :param destination: The square the current player's piece is moving to as 'letter + num'
        :param origin: The square the current player's piece is moving from as 'letter + num'
        :param destination_column_loc: The translated 'letter' in the destination location tuple.
        :param og_column_loc: The translated 'letter' in the origin location tuple.
        :param piece: The piece being moved as 'OWNER + SYMBOL'
        :param bool_list: The container to place True or False in.
        :param og_loc: Used for a special case in the check_for_check function.
        :return: True if piece can jump, False if not.
        """
        column_key = [('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6), ('h', 7)]
        horz_dist = abs(destination_column_loc - og_column_loc)
        vert_dist = abs(int(destination[1]) - int(origin[1]))

        if 'WHITE' in piece:
            for elem in self._white_dict:
                if elem.get_symbol() == piece:
                    piece_obj: King | Bishop | Rook | Knight = elem
        if 'BLACK' in piece:
            for elem in self._black_dict:
                if elem.get_symbol() == piece:
                    piece_obj: King | Bishop | Rook | King = elem

        # White pieces in the way
        for elem in self._white_dict:  # Check the whole roster
            if elem.get_location() is None:
                bool_list.append('JAIL')

            elif 'Bi' not in piece_obj.get_symbol():  # Doesn't apply to bishops
                # Horizontal
                if int(origin[1]) == elem.get_location()[1]:  # Is this other piece in the same row?
                    for index in column_key:
                        if elem.get_location()[0] == index[0]:  # Establish inner index.
                            elem_column: int = index[1]
                            if og_column_loc > elem_column > destination_column_loc or \
                                    og_column_loc < elem_column < destination_column_loc:
                                bool_list.append(False)  # If the piece is in the same row, it'll be in the way.
                            else:
                                bool_list.append(True)

                # Vertical
                if piece_obj.get_location()[0] == elem.get_location()[0]:  # Is this other piece in the same column?
                    if int(origin[1]) < elem.get_location()[1] < int(destination[1]) or \
                            int(origin[1]) > elem.get_location()[1] > int(destination[1]):
                        bool_list.append(False)
                    else:
                        bool_list.append(True)

                # Diagonal
                elif horz_dist == vert_dist:
                    # Check vertical problem first because it's easier
                    if int(origin[1]) < elem.get_location()[1] < int(destination[1]) or \
                            int(origin[1]) > elem.get_location()[1] > int(destination[1]):
                        for index in column_key:  # Then check horizontal issue using column key technique
                            if elem.get_location()[0] == index[0]:  # Establish inner index.
                                elem_column: int = index[1]
                                if og_column_loc > elem_column > destination_column_loc or \
                                        og_column_loc < elem_column < destination_column_loc:
                                    # If both these conditions are True, then the elem piece may be in the way,
                                    # check using slope! If the slope of the elem_piece location is equal to |1|
                                    # then it is in the path of the bishop!
                                    elem_coords = (int(elem.get_location()[1]), elem_column)
                                    bish_origin_coords = (int(origin[1]), og_column_loc)
                                    elem_slope = abs((bish_origin_coords[1] - elem_coords[1])
                                                     / (bish_origin_coords[0] - elem_coords[0]))
                                    if elem_slope == 1:
                                        bool_list.append(False)
                else:
                    bool_list.append(True)

            # Diagonal
            elif horz_dist == vert_dist:  # A bishop always moves with a linear slope of |1|
                # Check vertical problem first because it's easier
                if int(origin[1]) < elem.get_location()[1] < int(destination[1]) or \
                        int(origin[1]) > elem.get_location()[1] > int(destination[1]):
                    for index in column_key:  # Then check horizontal issue using column key technique
                        if elem.get_location()[0] == index[0]:  # Establish inner index.
                            elem_column: int = index[1]
                            if og_column_loc > elem_column > destination_column_loc or \
                                    og_column_loc < elem_column < destination_column_loc:
                                # If both these conditions are True, then the elem piece may be in the way,
                                # check using slope! If the slope of the elem_piece location is equal to |1|
                                # then it is in the path of the bishop!
                                elem_coords = (int(elem.get_location()[1]), elem_column)
                                bish_origin_coords = (int(origin[1]), og_column_loc)
                                elem_slope = abs((bish_origin_coords[1] - elem_coords[1])
                                                 / (bish_origin_coords[0] - elem_coords[0]))
                                if elem_slope == 1:
                                    bool_list.append(False)
                            else:
                                bool_list.append(True)

        # Black pieces in the way?
        for elem in self._black_dict:  # Check the whole roster
            if elem.get_location() is None:
                bool_list.append('JAIL')

            elif 'Bi' not in piece_obj.get_symbol():  # Doesn't apply to bishops
                # Horizontal
                if int(origin[1]) == elem.get_location()[1]:  # Is this other piece in the same row?
                    for index in column_key:
                        if elem.get_location()[0] == index[0]:  # Establish inner index.
                            elem_column: int = index[1]
                            if og_column_loc > elem_column > destination_column_loc or \
                                    og_column_loc < elem_column < destination_column_loc:
                                bool_list.append(False)  # If the piece is in the same row, it'll be in the way.
                            else:
                                bool_list.append(True)

                # Vertical
                if piece_obj.get_location()[0] == elem.get_location()[0]:  # Is this other piece in the same column?
                    if int(origin[1]) < elem.get_location()[1] < int(destination[1]) or \
                            int(origin[1]) < elem.get_location()[1] < int(destination[1]):
                        bool_list.append(False)
                    else:
                        bool_list.append(True)

                # Diagonal
                if horz_dist == vert_dist:
                    # Check vertical problem first because it's easier
                    if int(origin[1]) < elem.get_location()[1] < int(destination[1]) or \
                            int(origin[1]) > elem.get_location()[1] > int(destination[1]):
                        for index in column_key:  # Then check horizontal issue using column key technique
                            if elem.get_location()[0] == index[0]:  # Establish inner index.
                                elem_column: int = index[1]
                                if og_column_loc > elem_column > destination_column_loc or \
                                        og_column_loc < elem_column < destination_column_loc:
                                    # If both these conditions are True, then the elem piece may be in the way,
                                    # check using slope! If the slope of the elem_piece location is equal to |1|
                                    # then it is in the path of the bishop!
                                    elem_coords = (int(elem.get_location()[1]), elem_column)
                                    bish_origin_coords = (int(origin[1]), og_column_loc)
                                    elem_slope = abs((bish_origin_coords[1] - elem_coords[1])
                                                     / (bish_origin_coords[0] - elem_coords[0]))
                                    if elem_slope == 1:
                                        bool_list.append(False)
                else:
                    bool_list.append(True)

            # Diagonal
            elif horz_dist == vert_dist:
                # Check vertical problem first because it's easier
                if int(origin[1]) < elem.get_location()[1] < int(destination[1]) or \
                        int(origin[1]) > elem.get_location()[1] > int(destination[1]):
                    for index in column_key:  # Then check horizontal issue using column key technique
                        if elem.get_location()[0] == index[0]:  # Establish inner index.
                            elem_column: int = index[1]
                            if og_column_loc > elem_column > destination_column_loc or \
                                    og_column_loc < elem_column < destination_column_loc:
                                # If both these conditions are True, then the elem piece may be in the way,
                                # check using slope! If the slope of the elem_piece location is equal to |1|
                                # then it is in the path of the bishop!
                                elem_coords = (int(elem.get_location()[1]), elem_column)
                                bish_origin_coords = (int(origin[1]), og_column_loc)
                                elem_slope = abs((bish_origin_coords[1] - elem_coords[1])
                                                 / (bish_origin_coords[0] - elem_coords[0]))
                                if elem_slope == 1:
                                    bool_list.append(False)
            else:
                bool_list.append(True)
        if False not in bool_list:
            return True
        else:
            return False

    def king_move(self, destination, origin, destination_column_loc, og_column_loc,
                  bool_list, og_loc, destination_loc, piece):
        """
        Validate the movement of the King piece.
        :param origin: The square being moved from, 'letter + num'
        :param destination: The square being moved to, 'letter + num'
        :param destination_loc: The destination as a tuple ('letter', num)
        :param destination_column_loc: The translated 'letter' in the destination location tuple.
        :param og_column_loc: The translated 'letter' in the origin location tuple.
        :param bool_list: The container to place True or False in.
        :param piece: Refers to the piece symbol 'Owner + Symbol'
        :param og_loc: Used for a special case in the check_for_check function.
        :return: True, if the move is legal, False otherwise.
        """
        # Horizontal move
        if int(destination[1]) == int(origin[1]):  # Horizontal move?
            if abs(destination_column_loc - og_column_loc) == 1:  # Kings can only move one square away.
                # Jump-check
                if self.jump_rule(destination, origin, destination_column_loc, og_column_loc,
                                  bool_list, piece) is False:
                    bool_list.append(False)
                    return bool_list
                else:
                    bool_list.append(True)
            else:
                bool_list.append(False)  # Too far to move

        # Vertical move, can win here
        elif destination_column_loc == og_column_loc:  # Then maybe it's a vertical move?
            if abs(og_loc[1] - destination_loc[1]) == 1:
                if self.jump_rule(destination, origin, destination_column_loc, og_column_loc,
                                  bool_list, piece) is False:
                    bool_list.append(False)
                    return bool_list
                else:
                    bool_list.append(True)
                    if destination_loc[1] == 8 and self.get_turn_state() == 'BLACK':  # Win on Black turn.
                        if self.get_game_state() == 'WHITE_WON':
                            print('It\'s a tie!!!')
                            self.set_game_state('TIE')
                        else:
                            self.set_game_state('BLACK_WON')
                    if destination_loc[1] == 8 and self.get_turn_state() == 'WHITE':  # Win on White turn.
                        print('White has won, but Black gets one more turn!')
                        self.set_game_state('WHITE_WON')
            else:
                bool_list.append(False)

        # Diagonal move, can win here too
        elif int(destination[1]) != int(origin[1]) and destination_column_loc != og_column_loc:  # Maybe diagonal?
            if abs(destination_column_loc - og_column_loc) == 1 and abs(og_loc[1] - destination_loc[1]) == 1:
                if self.jump_rule(destination, origin, destination_column_loc, og_column_loc,
                                  bool_list, piece) is False:
                    bool_list.append(False)
                    return bool_list
                else:
                    bool_list.append(True)
                    if destination_loc[1] == 8 and self.get_turn_state() == 'BLACK':  # Win on Black turn.
                        if self.get_game_state() == 'WHITE_WON':
                            print('It\'s a tie!!!')
                            self.set_game_state('TIE')
                        else:
                            self.set_game_state('BLACK_WON')
                    if destination_loc[1] == 8 and self.get_turn_state() == 'WHITE':  # Win on White turn.
                        print('White has won, but Black gets one more turn!')
                        self.set_game_state('WHITE_WON')
            else:
                bool_list.append(False)
        return bool_list

    def rook_move(self, destination, origin, destination_column_loc, og_column_loc, bool_list, piece):
        """
        Validate the movement of the Rook piece.
        :param origin: The square being moved from, 'letter + num'
        :param destination: The square being moved to, 'letter + num'
        :param destination_column_loc: The translated 'letter' in the destination location tuple.
        :param og_column_loc: The translated 'letter' in the origin location tuple.
        :param bool_list: The container to place True or False in.
        :param piece: The piece being moved as 'OWNER + SYMBOL'
        :return: True, if the move is legal, False otherwise.
        """
        horz_dist = abs(destination_column_loc - og_column_loc)
        vert_dist = abs(int(destination[1]) - int(origin[1]))

        if horz_dist == vert_dist:  # Diagonal movement check.
            bool_list.append(False)
            return bool_list

        elif int(destination[1]) == int(origin[1]):  # Horizontal move?
            # Jump-check
            if self.jump_rule(destination, origin, destination_column_loc, og_column_loc, bool_list, piece) is False:
                bool_list.append(False)
                return bool_list
            else:
                bool_list.append(True)
                return bool_list

        elif destination[0] == origin[0]:  # Vertical move?
            # Jump-check
            if self.jump_rule(destination, origin, destination_column_loc, og_column_loc, bool_list, piece) is False:
                bool_list.append(False)
                return bool_list
            else:
                bool_list.append(True)
                return bool_list
        else:
            bool_list.append(False)
            return bool_list

    def knight_move(self, destination, origin, destination_column_loc, og_column_loc, bool_list):
        """
        Validate the movement of the Knight piece.
        :param origin: The square being moved from, 'letter + num'
        :param destination: The square being moved to, 'letter + num'
        :param destination_column_loc: The translated 'letter' in the destination location tuple.
        :param og_column_loc: The translated 'letter' in the origin location tuple.
        :param bool_list: The container to place True or False in.
        :return: True, if the move is legal, False otherwise.
        """
        # Vertical 2 & horizontal 1
        if abs(int(destination[1]) - int(origin[1])) == 2 and abs(destination_column_loc - og_column_loc) == 1:
            bool_list.append(True)
        # Horizontal 2 & vertical 1
        elif abs(int(destination[1]) - int(origin[1])) == 1 and abs(destination_column_loc - og_column_loc) == 2:
            bool_list.append(True)
        else:
            bool_list.append(False)
        return bool_list

    def bishop_move(self, destination, origin, destination_column_loc, og_column_loc, bool_list, piece):
        """
        Validate the movement of the Bishop piece.
        :param origin: The square being moved from, 'letter + num'
        :param destination: The square being moved to, 'letter + num'
        :param destination_column_loc: The translated 'letter' in the destination location tuple.
        :param og_column_loc: The translated 'letter' in the origin location tuple.
        :param bool_list: The container to place True or False in.
        :param piece: The piece being moved as 'OWNER + SYMBOL'
        :return: True, if the move is legal, False otherwise.
        """
        horz_dist = abs(destination_column_loc - og_column_loc)
        vert_dist = abs(int(destination[1]) - int(origin[1]))

        if int(destination[1]) == int(origin[1]):  # Horizontal move? Same row?
            bool_list.append(False)

        elif destination[0] == origin[0]:  # Vertical move? Same column?
            bool_list.append(False)

        elif int(destination[1]) != int(origin[1]) and destination_column_loc != og_column_loc:  # Maybe diagonal?
            if horz_dist != vert_dist:
                bool_list.append(False)
            else:
                if self.jump_rule(destination, origin, destination_column_loc, og_column_loc,
                                  bool_list, piece) is False:
                    bool_list.append(False)
                    return bool_list
                else:
                    bool_list.append(True)
        return bool_list

    def check_square(self, square):
        """
        Inquire into the current occupation of a square.
        :param square: Refers to the square that is being investigated, given as a string "letter + num"
        ie "a1".
        :return: "OCCUPIED" if the square has a piece on it, "EMPTY" if the square
        is unoccupied, and "INVALID" if the square is off the board.
        """
        for piece in self._white_dict:
            if piece.get_location() == square:
                return piece.get_symbol()
        for piece in self._black_dict:
            if piece.get_location() == square:
                return piece.get_symbol()
        return 'EMPTY'

    def remove_piece(self, piece):
        """
        Remove a piece from the game, happens after a legal and valid capture
        has been made by an opponent piece.
        :param piece: Refers to the key value in the appropriate dictionary of pieces. i.e. 'WHITE K'
        :return: Updates piece object's duty and location data members.
        """
        return piece.set_location(None)

    def get_king(self, black_or_white):
        """
        Retrieve the King object from the piece roster dictionary in _board.
        :param black_or_white: Indicates whether to access the black or white roster, can be 'WHITE' or 'BLACK'
        :return: King object from the relevant dictionary specified by the parameter.
        """
        if black_or_white == 'WHITE':
            for elem in self._white_dict:
                if elem.get_symbol() == 'WHITE K':
                    return elem
        else:
            for elem in self._black_dict:
                if elem.get_symbol() == 'BLACK K':
                    return elem

    def __repr__(self):
        """
        Allows the debugger to show an object's attributes rather than its
        address in memory.
        """
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)


class Piece:
    """
    Informs Board of whether a move is legal for that piece to make.
    If a move is deemed legal by the rules stored in Piece, this class
    tells Board to update the piece location & remove any captured pieces.
    Collaboration with Board to validate the legality of a move or inform Board
    when a King has crossed the finish line.
    Children: King, Bishop, Rook, Knight.
    """

    def __init__(self, owned_by):
        self._owned_by = owned_by
        self._duty = "ACTIVE"  # Can be changed to "CAPTURED" otherwise.

    def set_duty(self, new_duty):
        """
        Set the piece object's duty parameter to a different status. Active means
        a piece is still in play, otherwise Captured indicates that a piece is
        out-of-play.
        :param new_duty: Acceptable inputs are "ACTIVE" or "CAPTURED".
        :return: Changes the status of the piece's duty.
        """
        self._duty = new_duty
        return self._duty

    def get_owned_by(self):
        """
        Retrieve the owner of this chess piece.
        :return: Either "WHITE" or "BLACK" depending on who owns the piece.
        """
        return self._owned_by

    def get_duty(self):
        """
        Retrieve the duty status of this chess piece.
        :return: Either "ACTIVE" or "CAPTURED" depending on the status.
        """
        return self._owned_by

    def set_location(self, new_loc):
        """
        Change the location of the piece on the board.
        :param new_loc: Can be None to clear the location, or ('letter',square) for a new square.
        :return: Updated piece location.
        """
        if new_loc is None:
            self._location = None
            return self._location
        self._location = (new_loc[0], int(new_loc[1]))

    def get_location(self):
        """
        Retrieve piece location on the board in the form of a tuple.
        :return: Type Tuple: ('letter' , number)
        """
        return self._location

    def __repr__(self):
        """
        Allows the debugger to show an object's attributes rather than its
        address in memory.
        """
        return "{}({!r})".format(self.__class__.__name__, self.__dict__)


class King(Piece):
    """
    Knows the specific movement and capture rules of a King piece.
    Also informs Board when to update the game state due to a Winning
    or Tying condition. Knows its symbol on the board, "K".
    """

    def __init__(self, owned_by):
        super().__init__(owned_by)
        if self._owned_by == 'WHITE':
            self._location = ('a', 1)  # CHANGE BACK TO 'a1'
        if self._owned_by == 'BLACK':
            self._location = ('h', 1)  # CHANGE BACK TO 'h1'
        self._symbol = 'K'

    def get_location(self):
        """
        Retrieve the physical location of the chess piece on the playing board.
        :return: A string indicating the row and column that the piece is occupying.
        """
        return self._location

    def get_symbol(self):
        """
        Retrieve the symbol of this piece.
        :return: A string representing the piece's Type.
        """
        return self._owned_by + ' ' + self._symbol

    def win_game(self, origin, destination):
        """
        Check each time the King piece is moved. If the return is True, then the game is won
        for the player who owns this piece. If the player is WHITE then player BLACK will get
        one more turn following this one. If BLACK also completes the game, then the game state
        will be set to "TIE".
        :param origin: The square being moved from.
        :param destination: The square being moved to.
        :return: Updates game state to either "WHITE_WINS", "BLACK_WINS", or "TIE"
        """
        pass


class Bishop(Piece):
    """
    Knows the specific movement and capture rules of a Bishop piece.
    Knows its symbol on the board, "B".
    """

    def __init__(self, owned_by, one_or_two):
        super().__init__(owned_by)
        if one_or_two == 1:
            if self._owned_by == 'WHITE':
                self._location = ('b', 1)
            if self._owned_by == 'BLACK':
                self._location = ('g', 1)
        if one_or_two == 2:
            if self._owned_by == 'BLACK':
                self._location = ('g', 2)
            if self._owned_by == 'WHITE':
                self._location = ('b', 2)  # SHOULD BE: 'b2'
        self._symbol = "Bi"

    def get_location(self):
        """
        Retrieve the physical location of the chess piece on the playing board.
        :return: A string indicating the row and column that the piece is occupying.
        """
        return self._location

    def get_symbol(self):
        """
        Retrieve the symbol of this piece.
        :return: A string representing the piece's Type.
        """
        return self._owned_by + ' ' + self._symbol


class Rook(Piece):
    """
    Knows the specific movement and capture rules of a Rook piece.
    Knows its symbol on the board, "R".
    """

    def __init__(self, owned_by):
        super().__init__(owned_by)
        if self.get_owned_by() == 'BLACK':
            self._location = ('h', 2)
        if self.get_owned_by() == 'WHITE':
            self._location = ('a', 2)  # SHOULD BE: 'a2'
        self._symbol = "R"

    def get_location(self):
        """
        Retrieve the physical location of the chess piece on the playing board.
        :return: A string indicating the row and column that the piece is occupying.
        """
        return self._location

    def get_symbol(self):
        """
        Retrieve the symbol of this piece.
        :return: A string representing the piece's Type.
        """
        return self._owned_by + ' ' + self._symbol


class Knight(Piece):
    """
    Knows the specific movement and capture rules of a Knight piece.
    Knows its symbol on the board, "Kn".
    """

    def __init__(self, owned_by, one_or_two):
        super().__init__(owned_by)
        if one_or_two == 1:
            if self._owned_by == 'WHITE':
                self._location = ('c', 1)
            if self._owned_by == 'BLACK':
                self._location = ('f', 1)
        if one_or_two == 2:
            if self._owned_by == 'BLACK':
                self._location = ('f', 2)
            if self._owned_by == 'WHITE':
                self._location = ('c', 2)  # SHOULD BE: 'c2'
        self._symbol = "Kn"

    def get_location(self):
        """
        Retrieve the physical location of the chess piece on the playing board.
        :return: A string indicating the row and column that the piece is occupying.
        """
        return self._location

    def get_symbol(self):
        """
        Retrieve the symbol of this piece.
        :return: A string representing the piece's Type.
        """
        return self._owned_by + ' ' + self._symbol


if __name__ == '__main__':
    game = ChessVariant()
