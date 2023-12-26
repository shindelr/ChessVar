if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

import arcade
from arcade import Sprite
import ChessVar
import logging


class StartChessView(arcade.View):
    """
    Initialize the chess game.
    Must inherit arcade.Window in order to get all of Arcade's
    functionality.
    """

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BATTLESHIP_GREY)

        # Initializing ChessVar
        self._game = ChessVar.ChessVariant()

        # Initialize chessboard background.
        self._shape_list = None

        # Initializing Black sprites
        self._black_k_sprite = None
        self._black_bi1_sprite = None
        self._black_bi2_sprite = None
        self._black_r_sprite = None
        self._black_kn1_sprite = None
        self._black_kn2_sprite = None

        # Initializing White sprites
        self._white_k_sprite = None
        self._white_bi1_sprite = None
        self._white_bi2_sprite = None
        self._white_r_sprite = None
        self._white_kn1_sprite = None
        self._white_kn2_sprite = None

        # Create sprite lists here for the black & white pieces.
        self._black_sprites = None
        self._white_sprites = None

        # Initialize tile sprites
        self._tiles = None
        self._square = None

        # Initialize movement data members
        self._moving_piece = None
        self._moving_piece_og_pos = None

        # Text to be written
        self._turn_mssg = None
        self._illegal_mssg = None
        self._game_over_mssg = None

    def setup(self):
        """
        Use to set up the beginning of the game. Can be used to start the game
        over again once play has finished, etc..
        """
        self._shape_list = arcade.ShapeElementList()
        self.blank_board()

        # Fill the black sprites list with Sprite objects starting at their start positions
        self._black_sprites = []
        self.initialize_black_sprites()
        self._black_sprites = arcade.SpriteList()
        self.populate_black_sprites()

        # Fill the white sprites list with Sprite objects starting at their start positions
        self._white_sprites = []
        self.initialize_white_sprites()
        self._white_sprites = arcade.SpriteList()
        self.populate_white_sprites()

        # Set up piece movement
        self._moving_piece = None
        self._moving_piece_og_pos = None

        # Fill the tiles sprite list with sprites
        self._tiles = None
        self._square = None
        self._tiles = arcade.SpriteList()
        self.populate_tile_sprites()

        # Text to be displayed
        self._turn_mssg = None
        self._illegal_mssg = None
        self._game_over_mssg = None

    def initialize_black_sprites(self):
        """
        Re-Initialize all black sprite data members.
        """
        # Initializing Black sprites
        self._black_k_sprite = None
        self._black_bi1_sprite = None
        self._black_bi2_sprite = None
        self._black_r_sprite = None
        self._black_kn1_sprite = None
        self._black_kn2_sprite = None

    def initialize_white_sprites(self):
        """
        Re-Initialize all white sprite data members.
        """
        self._white_k_sprite = None
        self._white_bi1_sprite = None
        self._white_bi2_sprite = None
        self._white_r_sprite = None
        self._white_kn1_sprite = None
        self._white_kn2_sprite = None

    def blank_board(self):
        """
        Display a blank 8x8 chessboard.
        Tile sides = 90
        """
        # Blank chess board displayer.
        alternator = True
        count = 0
        win_y_pos = 45  # 45 indicates the center of the square.
        win_x_pos = 45  # So, even though a side is 90px, a square is defined from the center.
        square_side = 90  # The right size to fit an 8x8 board in a 720x720 window.
        while count != 8:
            for rep in range(9):
                if alternator is True:  # Beigish
                    shape = arcade.create_rectangle_filled(win_x_pos, win_y_pos, square_side,
                                                           square_side, arcade.color.BEIGE)  # OG is BEIGE
                    win_y_pos += square_side
                    alternator = False
                    self._shape_list.append(shape)
                else:  # Greyish
                    shape = arcade.create_rectangle_filled(win_x_pos, win_y_pos, square_side,
                                                           square_side, arcade.color.OUTER_SPACE)  # OG is Outer Space
                    win_y_pos += square_side
                    alternator = True
                    self._shape_list.append(shape)
            win_y_pos = (square_side / 2)
            win_x_pos += square_side
            count += 1
        return self._shape_list

    def populate_tile_sprites(self):
        """
        Fill self._tiles sprite list with sprites. Creates
        a grid of tiles formatted specifically for a 720x720
        board with 8x8 squares, side length 90.
        """
        win_y_pos = 675  # Start at top left
        win_x_pos = 45  # Start at far left
        for row in self._game.get_board():
            for tup in row:
                self._square = arcade.Sprite()
                self._square.center_x = win_x_pos
                self._square.center_y = win_y_pos
                self._tiles.append(self._square)
                if win_x_pos == 675:
                    win_x_pos = 45
                    win_y_pos -= 90
                else:
                    win_x_pos += 90

    def populate_black_sprites(self):
        """
        Create all the black sprites using the dictionaries in
        ChessVar.py
        :return: Fills self._black_sprites with Sprite objects
        """
        for elem in self._game.get_roster('BLACK'):
            if elem.get_symbol() == 'BLACK K':
                self._black_k_sprite = arcade.Sprite('chess_sprites_images/black_king.png', .08)
                self._black_k_sprite.center_x = 675
                self._black_k_sprite.center_y = 45
                self._black_sprites.append(self._black_k_sprite)
            if elem.get_symbol() == 'BLACK Bi' and self._black_bi1_sprite is None:
                self._black_bi1_sprite = arcade.Sprite('chess_sprites_images/black_bi.png', .08)
                self._black_bi1_sprite.center_x = 585
                self._black_bi1_sprite.center_y = 45
                self._black_sprites.append(self._black_bi1_sprite)
            if elem.get_symbol() == 'BLACK Bi' and self._black_bi2_sprite is None:
                self._black_bi2_sprite = arcade.Sprite('chess_sprites_images/black_bi.png', .08)
                self._black_bi2_sprite.center_x = 585
                self._black_bi2_sprite.center_y = 135
                self._black_sprites.append(self._black_bi2_sprite)
            if elem.get_symbol() == 'BLACK R':
                self._black_r_sprite = arcade.Sprite('chess_sprites_images/black_r.png', .08)
                self._black_r_sprite.center_x = 675
                self._black_r_sprite.center_y = 135
                self._black_sprites.append(self._black_r_sprite)
            if elem.get_symbol() == 'BLACK Kn' and self._black_kn1_sprite is None:
                self._black_kn1_sprite = arcade.Sprite('chess_sprites_images/black_kn.png', .08)
                self._black_kn1_sprite.center_x = 495
                self._black_kn1_sprite.center_y = 45
                self._black_sprites.append(self._black_kn1_sprite)
            if elem.get_symbol() == 'BLACK Kn' and self._black_kn2_sprite is None:
                self._black_kn2_sprite = arcade.Sprite('chess_sprites_images/black_kn.png', .08)
                self._black_kn2_sprite.center_x = 495
                self._black_kn2_sprite.center_y = 135
                self._black_sprites.append(self._black_kn2_sprite)

    def populate_white_sprites(self):
        """
        Create all the white sprites using the dictionaries in
        ChessVar.py
        :return: Fills self._white_sprites with Sprite objects
        """
        for elem in self._game.get_roster('WHITE'):
            if elem.get_symbol() == 'WHITE K':
                self._white_k_sprite = arcade.Sprite('chess_sprites_images/white_king.png', .08)
                self._white_k_sprite.center_x = 45
                self._white_k_sprite.center_y = 45
                self._white_sprites.append(self._white_k_sprite)
            if elem.get_symbol() == 'WHITE Bi' and self._white_bi1_sprite is None:
                self._white_bi1_sprite = arcade.Sprite('chess_sprites_images/white_bish.png', .08)
                self._white_bi1_sprite.center_x = 135
                self._white_bi1_sprite.center_y = 45
                self._white_sprites.append(self._white_bi1_sprite)
            if elem.get_symbol() == 'WHITE Bi' and self._white_bi2_sprite is None:
                self._white_bi2_sprite = arcade.Sprite('chess_sprites_images/white_bish.png', .08)
                self._white_bi2_sprite.center_x = 135
                self._white_bi2_sprite.center_y = 135
                self._white_sprites.append(self._white_bi2_sprite)
            if elem.get_symbol() == 'WHITE R':
                self._white_r_sprite = arcade.Sprite('chess_sprites_images/white_r.png', .08)
                self._white_r_sprite.center_x = 45
                self._white_r_sprite.center_y = 135
                self._white_sprites.append(self._white_r_sprite)
            if elem.get_symbol() == 'WHITE Kn' and self._white_kn1_sprite is None:
                self._white_kn1_sprite = arcade.Sprite('chess_sprites_images/white_kn.png', .08)
                self._white_kn1_sprite.center_x = 225
                self._white_kn1_sprite.center_y = 45
                self._white_sprites.append(self._white_kn1_sprite)
            if elem.get_symbol() == 'WHITE Kn' and self._white_kn2_sprite is None:
                self._white_kn2_sprite = arcade.Sprite('chess_sprites_images/white_kn.png', .08)
                self._white_kn2_sprite.center_x = 225
                self._white_kn2_sprite.center_y = 135
                self._white_sprites.append(self._white_kn2_sprite)

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Allow for input from the keyboard.
        U -- Undo current move, cannot be done if piece is already "set down"
        R -- Restart game
        """
        if symbol == 117:  # 117 equals U
            if self._moving_piece is not None:
                self._moving_piece.position = self._moving_piece_og_pos
                self._moving_piece = None
                self._moving_piece_og_pos = None
            else:
                pass
        if symbol == 114:  # 114 equals R
            self._game = ChessVar.ChessVariant()
            self.setup()

    def on_draw(self):
        """
        Used to draw on the window. on_draw is an Arcade method
        inherited by Arcade's Window class.
        :return: Display a chess board.
        """
        self.clear()

        self._shape_list.draw()
        self._black_sprites.draw()
        self._white_sprites.draw()
        self._tiles.draw()

        # Messages!
        if self._game_over_mssg is not None and self._illegal_mssg is None:
            arcade.draw_text(self._game_over_mssg, 360, 370, arcade.color.RED_DEVIL, 80, 20, 'center', 'garamond', True)
            arcade.draw_text('Press R to restart.', 90, 410, arcade.color.RED_DEVIL, 20, 5, 'left', 'garamond', True)

        if self._illegal_mssg is not None:
            arcade.draw_text(self._illegal_mssg, 550, 410, arcade.color.RED_DEVIL, 20, 5, 'center','garamond', True)

        if self._turn_mssg is not None and self._illegal_mssg is None:
            arcade.draw_text(self._turn_mssg, 550, 420, arcade.color.RED_DEVIL, 20, 5, 'center', 'garamond', True)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """
        Upon pressing the left mouse button, you will select a piece to move.
        """
        logging.debug(f'{button} pressed.')
        # Clear any messages
        self._illegal_mssg = None
        self._turn_mssg = None

        column_key = [(45, 'a'), (135, 'b'), (225, 'c'), (315, 'd'), (405, 'e'), (495, 'f'), (585, 'g'), (675, 'h')]
        row_key = [(45, 1), (135, 2), (225, 3), (315, 4), (405, 5), (495, 6), (585, 7), (675, 8)]
        counter = 0

        # Get whatever sprite is at the point
        white_pieces: list[Sprite] = arcade.get_sprites_at_point((x, y), self._white_sprites)
        black_pieces: list[Sprite] = arcade.get_sprites_at_point((x, y), self._black_sprites)

        # Assign values to appropriate movement data members
        # Clicking on a piece.
        if self._moving_piece is None:
            if len(white_pieces) > 0:
                self._moving_piece = white_pieces[0]
                self._moving_piece_og_pos = self._moving_piece.position
                white_pieces.clear()
            elif len(black_pieces) > 0:
                self._moving_piece = black_pieces[0]
                self._moving_piece_og_pos = self._moving_piece.position
                black_pieces.clear()
            else:
                print('That isn\'t a piece!')
        # If you have a piece in your hand, press on the square you want.
        else:
            # Validate compliance with the rules
            for tile in self._tiles:
                if self._moving_piece is not None:
                    if (abs(tile.center_x - self._moving_piece.center_x) < 45) \
                            and (abs(tile.center_y - self._moving_piece.center_y) < 45):  # Piece landing in a square?
                        origin = self.translate_origin(column_key, row_key)  # Translate origin coords.
                        destination = self.translate_destination(column_key, row_key, tile)  # Translate destination coords
                        if self._game.make_move(origin, destination) is True:  # Main portal to ChessVar
                            self._moving_piece.position = tile.position  # Move piece successfully

                            # Make any captures in the GUI
                            if self._moving_piece in self._black_sprites:
                                self.capture_white_piece()
                            if self._moving_piece in self._white_sprites:
                                self.capture_black_piece()
                            break

                        else:
                            logging.warning('Illegal Move.')
                            self._illegal_mssg = 'Illegal move!'
                            self._moving_piece.position = self._moving_piece_og_pos
                            self._moving_piece = None
                            self._moving_piece_og_pos = None

            self._moving_piece = None
            self._moving_piece_og_pos = None

            # Check on game state!
            if self._game.get_game_state() == 'BLACK_WON' and self._illegal_mssg is None:
                self._game_over_mssg = 'BLACK WINS'
            elif self._game.get_game_state() == 'TIE' and self._illegal_mssg is None:
                self._game_over_mssg = 'IT\'S A TIE'
            elif self._game.get_game_state() == 'WHITE_WON' \
                    and self._game.get_turn_state() == 'WHITE' and self._illegal_mssg is None:
                self._game_over_mssg = 'WHITE WINS'
            else:
                if self._game.get_turn_state() == 'WHITE':
                    self._turn_mssg = 'White team\'s turn!'
                else:
                    self._turn_mssg = 'Black team\'s turn!'

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        """
        Drag the piece to where you want it to go.
        """
        if self._moving_piece is not None:
            self._moving_piece.center_x += dx
            self._moving_piece.center_y += dy
        else:
            return

    def translate_origin(self, column_key, row_key):
        """
        Translate the origin square in the GUI to the string
        that ChessVar needs to satisfy make_move().
        :param column_key: A list of tuples like -- (45, 'a')
        :param row_key: A list of tuples like -- (45, 1)
        :return: GUI coordinates as string -- 'letter+num'
        """
        if self._moving_piece in self._white_sprites or self._moving_piece in self._black_sprites:
            # Translate the origin square
            for pair in column_key:
                if abs((self._moving_piece_og_pos[0] - pair[0])) <= 45:
                    trans_col = pair[1]
                    for tup in row_key:
                        if abs((self._moving_piece_og_pos[1] - tup[0])) <= 45:
                            trans_row = tup[1]
                            origin = f'{trans_col}{trans_row}'
                            return origin

    def translate_destination(self, column_key, row_key, tile):
        """
        Translate the destination square in the GUI to the string
        that ChessVar needs to satisfy make_move(). Also validates
        whether the piece is being placed on a tile or not.
        :param column_key: A list of tuples like -- (45, 'a')
        :param row_key: A list of tuples like -- (45, 1)
        :param tile: The tile sprite object currently being accessed in the for loop.
        :return: GUI coordinates as string -- 'letter+num'
        """
        for pair in column_key:  # Translating the 'letter' in the tuple in ChessVar DESTINATION
            if abs((tile.center_x - pair[0])) <= 45:
                trans_col = pair[1]
                for tup in row_key:  # Translating the 'int' in the tuple in ChessVar DESTINATION
                    if abs((tile.center_y - tup[0])) <= 45:
                        trans_row = str(tup[1])
                        destination = f'{trans_col}{trans_row}'
                        return destination

    def capture_white_piece(self):
        """
        Iterate through the white_sprite roster,
        if a piece is in the same square, remove it.
        :return: Remove opponent piece from the board.
        """
        for opponent in self._white_sprites:
            if self._moving_piece.position == opponent.position:
                Sprite.kill(opponent)

    def capture_black_piece(self):
        """
        Iterate through the black_sprite roster,
        if a piece is in the same square, remove it.
        :return: Remove opponent piece from the board.
        """
        for opponent in self._black_sprites:
            if self._moving_piece.position == opponent.position:
                Sprite.kill(opponent)


class WelcomeView(arcade.View):
    """
    Welcome the user to ChessVar! Allow them to either
    view the instructions, or start a new game.
    """

    def __init__(self):
        super().__init__()
        self._background = None

    def setup(self):
        """
        Set up the window.
        """
        self._background = arcade.load_texture('chess_sprites_images/title_screen.jpg')

    def on_show_view(self):
        """
        Run when called to show view.
        """
        arcade.set_background_color(arcade.color.COCOA_BROWN)

    def on_draw(self):
        """
        Draw things on the screen.
        """
        # Draw dope intro image
        arcade.draw_lrwh_rectangle_textured(0, 0, 720, 720, self._background)

    def on_key_press(self, symbol: int, modifiers: int):
        """
        Press any key to start a new game!
        """
        new_game = StartChessView()
        new_game.setup()
        self.window.show_view(new_game)


def main():
    window = arcade.Window(720, 720, 'Chess!')
    welcome_view = WelcomeView()
    window.show_view(welcome_view)
    welcome_view.setup()
    arcade.run()


if __name__ == '__main__':
    main()
