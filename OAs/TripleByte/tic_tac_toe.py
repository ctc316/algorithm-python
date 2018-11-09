import constants as const
import bisect
import random

def draw_board(board, show_pos=False):
    for i in range(0, 9, 3):
        print(' ' + (board[i] if not show_pos or board[i] != ' ' else str(i))              \
          + ' | ' + (board[i + 1] if not show_pos or board[i + 1] != ' ' else str(i + 1))  \
          + ' | ' + (board[i + 2] if not show_pos or board[i + 2] != ' ' else str(i + 2)))

        if i != 6:
            print('-----------')


def pick_side():
    input_str = ''
    while not (input_str == const.LETTER_O or input_str == const.LETTER_X):
        print('Do you want to be {} or {}? (input {} or {})'.format(const.LETTER_O, const.LETTER_X, const.LETTER_O, const.LETTER_X))
        input_str = input().upper()

    if input_str == const.LETTER_X:
        return const.LETTER_X, const.LETTER_O
    return const.LETTER_O, const.LETTER_X


def pick_turn():
    return random.choice([const.TURN_PLAYER, const.TURN_COMPUTER])
    # input_str = ''
    # while not (input_str == 'yes' or input_str == 'no'):
    #     print('Do you want to go first? (input yes or no)')
    #     input_str = input().lower()

    # if input_str == 'yes':
    #     return const.TURN_PLAYER
    # return const.TURN_COMPUTER


def get_player_move(board, moves):
    move = -1
    while move not in moves:
        print('Input your next move (0~8):')
        input_move = input()
        if not input_move.isdigit():
            continue
        move = int(input_move)

    return move


def get_comp_move(board, moves, comp_side, player_side):
    # check for winning
    for m in moves:
        board[m] = comp_side
        win = is_winner(board, comp_side)
        board[m] = const.LETTER_NONE
        if win:
            return m

    # check for losing
    for m in moves:
        board[m] = player_side
        win = is_winner(board, player_side)
        board[m] = const.LETTER_NONE
        if win:
            return m

    return random.choice(moves)


def is_winner(board, side):
    for row in range(0, 9, 3):
        if board[row] == side and board[row + 1] == side and board[row + 2] == side:
            return True

    for col in range(3):
        if board[col] == side and board[3 + col] == side and board[6 + col] == side:
            return True

    # diagonal
    if board[4] == side and (board[0] == side and board[8] == side 
                             or board[2] == side and board[6] == side):
        return True


def main():
    board = [const.LETTER_NONE] * 10
    moves = [i for i in range(9)]
    rounds = 1

    player_side, comp_side = pick_side()
    turn = pick_turn()

    print("Player picks", player_side)
    print(turn, "goes first.")

    while rounds < 10:
        print("---------------------------------")
        print("Round:", rounds, "({})".format(turn))

        if turn == const.TURN_PLAYER:
            draw_board(board, True)
            move = get_player_move(board, moves)
            board[move] = player_side
            draw_board(board, True)
            if is_winner(board, player_side):
                print("\n ==> Player won.")
                break

        else:
            draw_board(board, True)
            move = get_comp_move(board, moves, comp_side, player_side)
            board[move] = comp_side
            print('Computer\'s move:', move)
            draw_board(board, True)
            if is_winner(board, comp_side):
                print("\n ==> Computer won.")
                break

        moves.pop(bisect.bisect_left(moves, move))

        if turn == const.TURN_PLAYER:
            turn = const.TURN_COMPUTER
        else:
            turn = const.TURN_PLAYER

        rounds += 1

    if rounds == 10:
        print("\n ==> Tie Game")

if __name__ == '__main__':
    main()