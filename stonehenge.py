from game_state import GameState
from game import Game


class StonehengeGame(Game):
    """
    Initialize the Stonehenge to implement the specific methods of this
    game.
    """

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player
        is.
        """
        length = int(input("gvie a side length:"))
        self.current_state = StonehengeState(p1_starts, length)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        @return :str
        """
        return "Players take turn claiming the cells, the person who captures" \
               " at least half of the ley-lines is the winner."

    def is_over(self, state: GameState) -> bool:
        """
        Return whether or not this game is over at state.
        @return : bool
        """
        _1 = state.get_score('p1')
        _2 = state.get_score('p2')
        total_l = len(state.lines)
        if (_1 >= 1/2*total_l) or (_2 >= 1/2*total_l):
            return True
        return False

    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        return (self.current_state.get_current_player_name() != player and
                self.is_over(self.current_state))

    def str_to_move(self, string: str) -> str:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        @param str string: the input string of move
        @return: str
        """
        if not string.strip().isalpha():
            return '-1'
        return str(string.strip())


class StonehengeState(GameState):
    """
    Initilaize stone_state and contain all the specific state methods for
    this game.
    """
    WIN: int = 1
    LOSE: int = -1
    DRAW: int = 0
    p1_turn: bool

    def __init__(self, is_p1_turn: bool, length: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        """
        self.p1_turn = is_p1_turn
        self.length = length
        self.cells = []
        self.cells_r = []
        self.lines = []
        if self.length == 1:
            self.cells = ["AB",
                          "C",
                          "A", "BC",
                          "AC", "B"]
            self.cells_r = ["AB",
                            " C"]
            self.lines = ['@', '@', '@', '@', '@', '@']
        if self.length == 2:
            self.cells = ["AB",
                          "CDE",
                          "FG",
                          "AC", "BDF", "EG",
                          "CF", "ADG", "BE"]
            self.cells_r = [" AB",
                            "CDE",
                            "FG ", ]
            self.lines = ['@', '@', '@', '@', '@', '@', '@', '@', '@']
        if self.length == 3:
            self.cells = ["AB",
                          "CDE",
                          "FGHI",
                          "JKL",
                          "ACF", "BDGJ", "EHK", "IL",
                          "FJ", "CGK", "ADHL", "BEI"]
            self.cells_r = ["  AB",
                            " CDE",
                            "FGHI",
                            "JKL ", ]
            self.lines = ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@',
                          '@']
        if self.length == 4:
            self.cells = ["AB",
                          "CDE",
                          "FGHI",
                          "JKLMN",
                          "OPQR",
                          "ACFJ", "BDGKO", "EHLP", "IMQ", "NR",
                          "JO", "FKP", "CGLQ", "ADHMR", "BEIN"]
            self.cells_r = ["   AB",
                            "  CDE",
                            " FGHI",
                            "JKLMN",
                            "OPQR ", ]
            self.lines = ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@',
                          '@', '@', '@', '@']
        if self.length == 5:
            self.cells = ["AB",
                          "CDE",
                          "FGHI",
                          "JKLMN",
                          "OPQRST",
                          "UVWXY",
                          "ACFJO", "BDGKPU", "EHLQV", "IMRW", "NSX", "TY",
                          "OU", "JPV", "FKQW", "CGLRX", "ADHMSY", "BEINT"]
            self.cells_r = ["    AB",
                            "   CDE",
                            "  FGHI",
                            " JKLMN",
                            "OPQRST",
                            "UVWXY "]
            self.lines = ['@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@',
                          '@', '@', '@', '@', '@', '@', '@']

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        >>> print(StonehengeState(True, 1).__str__())
        @ @
        @ A B
        @ C @
        @
        >>> print(StonehengeState(True, 2).__str__())
        @ @
        @ A B @
        @ C D E
        @ F G @
        @ @
        >>> print(StonehengeState(True, 3).__str__())
        @ @
        @ A B @
        @ C D E @
        @ F G H I
        @ J K L @
        @ @ @
        >>> print(StonehengeState(True, 4).__str__())
        @ @
        @ A B @
        @ C D E @
        @ F G H I @
        @ J K L M N
        @ O P Q R @
        @ @ @ @
        >>> print(StonehengeState(True, 5).__str__())
        @ @
        @ A B @
        @ C D E @
        @ F G H I @
        @ J K L M N @
        @ O P Q R S T
        @ U V W X Y @
        @ @ @ @ @
        """
        l = self.lines
        m = []
        i = 0
        if self.length == 1:
            while i < 2:
                m += self.cells[i]
                i += 1
            return ('{} {}\n'
                    '{} {} {}\n'
                    '{} {} {}\n'
                    '{}').format(l[2], l[3],
                                 l[0], m[0], m[1],
                                 l[1], m[2], l[5],
                                 l[4])
        if self.length == 2:
            while i < 3:
                m += self.cells[i]
                i += 1
            return ('{} {}\n'
                    '{} {} {} {}\n'
                    '{} {} {} {}\n'
                    '{} {} {} {}\n'
                    '{} {}').format(l[3], l[4],
                                    l[0], m[0], m[1], l[5],
                                    l[1], m[2], m[3], m[4],
                                    l[2], m[5], m[6], l[8],
                                    l[6], l[7])
        if self.length == 3:
            while i < 5:
                m += self.cells[i]
                i += 1
            return ('{} {}\n'
                    '{} {} {} {}\n'
                    '{} {} {} {} {}\n'
                    '{} {} {} {} {}\n'
                    '{} {} {} {} {}\n'
                    '{} {} {}').format(l[4], l[5],
                                       l[0], m[0], m[1], l[6],
                                       l[1], m[2], m[3], m[4], l[7],
                                       l[2], m[5], m[6], m[7], m[8],
                                       l[3], m[9], m[10], m[11], l[11],
                                       l[8], l[9], l[10])
        if self.length == 4:
            while i < 6:
                m += self.cells[i]
                i += 1
            return ('{} {}\n'
                    '{} {} {} {}\n'
                    '{} {} {} {} {}\n'
                    '{} {} {} {} {} {}\n'
                    '{} {} {} {} {} {}\n'
                    '{} {} {} {} {} {}\n'
                    '{} {} {} {}').format(l[5], l[6],
                                          l[0], m[0], m[1], l[7],
                                          l[1], m[2], m[3], m[4], l[8],
                                          l[2], m[5], m[6], m[7], m[8], l[9],
                                          l[3], m[9], m[10], m[11], m[12], m[13],
                                          l[4], m[14], m[15], m[16], m[17], l[14],
                                          l[10], l[11], l[12], l[13])

        if self.length == 5:
            while i < 7:
                m += self.cells[i]
                i += 1
            return ('{} {}\n'
                    '{} {} {} {}\n'
                    '{} {} {} {} {}\n'
                    '{} {} {} {} {} {}\n'
                    '{} {} {} {} {} {} {}\n'
                    '{} {} {} {} {} {} {}\n'
                    '{} {} {} {} {} {} {}\n'
                    '{} {} {} {} {}').format(l[6], l[7],
                                             l[0], m[0], m[1], l[8],
                                             l[1], m[2], m[3], m[4], l[9],
                                             l[2], m[5], m[6], m[7], m[8], l[10],
                                             l[3], m[9], m[10], m[11], m[12], m[13], l[11],
                                             l[4], m[14], m[15], m[16], m[17], m[18], m[19],
                                             l[5], m[20], m[21], m[22], m[23], m[24], l[17],
                                             l[12], l[13], l[14], l[15], l[16])

    def __repr__(self) -> str:
        """
        Return a representation of this state that can be used for
        equality testing.
        """
        return "P1's Turn: {} \n Board: \n{}".format(self.p1_turn,self.__str__())

    def get_possible_moves(self) -> list:
        """
        Return all possible moves that can be applied to this state.
        >>> StonehengeState(True, 2).get_possible_moves()
        ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        """
        m = []
        p_moves = []
        i = 0
        _1 = self.get_score('p1')
        _2 = self.get_score('p2')
        total_l = len(self.lines)

        if (_1 >= 1 / 2 * total_l) or (_2 >= 1 / 2 * total_l):
            p_moves = []
        elif self.length == 1:
            while i < 2:
                m += self.cells[i]
                i += 1
        elif self.length == 2:
            while i < 3:
                m += self.cells[i]
                i += 1
        elif self.length == 3:
            while i < 5:
                m += self.cells[i]
                i += 1
        elif self.length == 4:
            while i < 6:
                m += self.cells[i]
                i += 1
        elif self.length == 5:
            while i < 7:
                m += self.cells[i]
                i += 1
        for move in m:
            if move.isalpha():
                p_moves.append(move)
        return p_moves

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.
        >>> StonehengeState(True, 2).get_current_player_name()
        'p1'
        >>> StonehengeState(False, 2).get_current_player_name()
        'p2'
        """
        if self.p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move) -> 'GameState':
        """
        Return the GameState that results from applying move to this GameState.
        >>> print (StonehengeState(True, 2).make_move('A'))
        1 @
        1 1 B @
        @ C D E
        @ F G @
        @ @
        >>> print (StonehengeState(False, 2).make_move('G'))
        @ @
        @ A B 2
        @ C D E
        2 F 2 @
        @ @
        >>> S = StonehengeState(False, 2).make_move('G')
        >>> print (S.make_move('A'))
        1 @
        1 1 B 2
        @ C D E
        2 F 2 @
        @ @
        """
        new_state = StonehengeState(True, 0)
        old_lines = self.lines
        new_lines = []
        old_cells = self.cells
        new_cells = []
        new_cells.extend(old_cells)
        new_lines.extend(old_lines)

        i_1 = -1
        i_2 = 0
        _len = self.length
        cur_player = self.get_current_player_name()

        while i_1 < len(new_cells):
            for _str in new_cells:
                i_1 += 1
                if move in _str:
                    if cur_player == 'p1':
                        n_str = _str.replace(move, '1')
                        new_cells[i_1] = n_str
                    if cur_player == 'p2':
                        n_str = _str.replace(move, '2')
                        new_cells[i_1] = n_str

        while i_2 < len(new_lines):
            for str in new_cells:
                count = 0
                i_2 += 1
                if cur_player == 'p1':
                    for each in str:
                        if each == '1':
                            count += 1
                    if count >= 1/2 * len(str):
                        if new_lines[i_2-1] == '@':
                            new_lines[i_2-1] = '1'
                if cur_player == 'p2':
                    for each in str:
                        if each == '2':
                            count += 1
                    if count >= 1/2 * len(str):
                        if new_lines[i_2 - 1] == '@':
                            new_lines[i_2-1] = '2'

        if self.get_current_player_name() == 'p1':
            new_state.p1_turn = False
        else:
            new_state.p1_turn = True

        new_state.cells = new_cells
        new_state.lines = new_lines
        new_state.length = _len

        return new_state

    def is_valid_move(self, move: str) -> bool:
        """
        Return whether move is a valid move for this GameState.
        """
        return move in self.get_possible_moves()

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        >>> S = StonehengeState(False, 2).make_move('G')
        >>> S.rough_outcome()
        -1
        >>> S = StonehengeState(False, 2).make_move('G').make_move('A').make_move('B').make_move('C')
        >>> S.rough_outcome()
        1
        >>> S = StonehengeState(False, 1).make_move('A')
        >>> S.rough_outcome()
        -1
        """
        state = self

        _1 = self.get_score('p1')
        _2 = self.get_score('p2')
        total_l = len(self.lines)

        if (_1 >= 1 / 2 * total_l) or (_2 >= 1 / 2 * total_l):
            return -1

        for move in state.get_possible_moves():
            n_state = state.make_move(move)
            if (n_state.get_score('p1') >= 1 / 2 * total_l) or (
                    n_state.get_score('p2') >= 1 / 2 * total_l):
                return 1
            elif n_state.get_possible_moves():
                for mov in n_state.get_possible_moves():
                    l_state = n_state.make_move(mov)
                    if (l_state.get_score('p1') >= 1 / 2 * total_l) or (
                    l_state.get_score('p2') >= 1 / 2 * total_l):
                        return -1
        else:
            return 0


    def get_score(self, player: str) -> int:
        """
        a helper function to get the numer of lines that the palyer claimed
        >>> StonehengeState(True, 2).get_score('p1')
        0
        >>> S = StonehengeState(True, 2)
        >>> S.make_move('A').get_score('p1')
        2
        >>> S = StonehengeState(True, 2)
        >>> cur_S = S.make_move('A')
        >>> cur_S.get_score('p1')
        2
        >>> S = StonehengeState(False, 2)
        >>> cur_S = S.make_move('B')
        >>> cur_S.get_score('p2')
        2
        >>> S = StonehengeState(True, 2)
        >>> cur_S = S.make_move('A')
        >>> curr_S = cur_S.make_move('B')
        >>> curr_S.get_score('p2')
        1
        >>> S = S = StonehengeState(True, 1)
        >>> cur_S = S.make_move('A')
        >>> cur_S.get_score('p1')
        3
        """
        count_1 = 0
        count_2 = 0

        for each in self.lines:
            if each == '1':
                count_1 += 1
            elif each == '2':
                count_2 += 1
        if player == 'p1':
            return count_1
        return count_2


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
