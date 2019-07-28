"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
from game_state import GameState

# TODO: Adjust the type annotation as needed.


def interactive_strategy(game: Any) -> str:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> str:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def re_strategy_score(game: Any, state) -> list:
    """
    return a move score in [WIN, LOSE] of a move at current state

    """
    if game.is_over(state):
        if state.get_current_player_name() == 'p1':
            if game.is_winner('p1'):
                return [1]
            elif game.is_winner('p2'):
                return [-1]
        if state.get_current_player_name() == 'p2':
            if game.is_winner('p2'):
                return [1]
            elif game.is_winner('p1'):
                return [-1]
        else:
            return [0]
    else:
        scores = []
        for move in state.get_possible_moves():
            cur_state = state.make_move(move)
            game.current_state = cur_state
            scores.append(max(re_strategy_score(game, cur_state)) * -1)
        return scores


def recursive_strategy(game: Any) -> str:
    """
    return a move for game by picking a move which can produce the highest
    guaranteed score in recursice version.
    """
    state = game.current_state
    scores = re_strategy_score(game, state)
    high_score = max(scores)
    p_moves = state.get_possible_moves()
    return p_moves[scores.index(high_score)]


def iterative_strategy(game: Any) -> Any:
    """
    return a move for game by picking a move which can produce the highest
    guaranteed score in iterative version.
    """
    stack = []
    list = []
    cur_state = Cell(game.current_state)
    stack.append(cur_state)

    while stack:
        cur_pop = stack.pop()
        game.current_state = cur_pop.state
        if not cur_pop.state.get_possible_moves():
            cur_pop.score = 1
        elif cur_pop.subs:
            cur_pop.score = max([(sub.score * -1) for sub in cur_pop.subs])
        else:
            p_moves = cur_pop.state.get_possible_moves()
            new_subs = [Cell(cur_pop.state.make_move(move)) for move
                        in p_moves]
            cur_pop.subs += new_subs
            stack.append(cur_pop)
            stack.extend(new_subs)

    _moves = cur_state.state.get_possible_moves()
    list.extend([sub.score for sub in cur_state.subs])
    high_score = max(list)
    index = list.index(high_score)
    f_move = _moves[index]
    return f_move

class Cell:
    """
    a class which can store children and its scores
    """

    def __init__(self, state: GameState):
        """
        init a cell which can store the score and the substates of the       state
        """
        self.state = state
        self.score = 0
        self.subs = []


if __name__ == "__main__":
    from python_ta import check_all

    check_all(config="a2_pyta.txt")
