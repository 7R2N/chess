from colorama import Back, Style
import string


class ChessBoard:
    pos = [["r", "n", "b", "q", "k", "b", "n", "r"],
           ["p", "p", "p", "p", "p", "p", "p", "p"],
           [" ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " "],
           [" ", ' ', " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " "],
           ["P", "P", "P", "P", "P", "P", "P", "P"],
           ["R", "N", "B", "Q", "K", "B", "N", "R"]]

    def print(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    print(Back.LIGHTWHITE_EX + '\033[1m' + f' {self.pos[i][j]} ' + '\033[0m' + Back.RESET, end='')

                else:
                    print(Back.BLACK + f' {self.pos[i][j]} ' + Back.RESET, end='')

            print(Back.BLACK + "" + Back.RESET + f" {8 - i}")

        x = 0
        for letter in string.ascii_uppercase:
            print(" " + letter, end=" ")
            x += 1
            if x == 8:
                break
        print("")

    def turn(self):
        piece = input("Which piece you want to move (P if you want to move pawn): \n")
        if piece == "K":
            pass
        elif piece == "P":
            pass
        elif piece == "Q":
            pass
        elif piece == "R":
            pass
        elif piece == "N":
            pass
        elif piece == "B":
            pass

        # print possible moves there

        # specify which piece you should move if there are two possibilities

        move = list(input("Make your move: \n"))

    def king_list_moves(self, piece):
        legal_moves = []
        if 7 >= piece.piece_pos[0] >= 0:
            if 7 >= piece.piece_pos[1] >= 0:
                # |X|0|X|
                # |X|K|X|
                # |X|X|X|
                if piece.piece_pos[0] - 1 >= 0:
                    legal_moves.apped((piece.piece_pos[0] - 1, piece.piece_pos[1]))
                # |X|X|X|
                # |X|K|X|
                # |X|0|X|
                if piece.piece_pos[0] + 1 <= 7:
                    legal_moves.apped((piece.piece_pos[0] + 1, piece.piece_pos[1]))
                # |X|X|X|
                # |0|K|X|
                # |X|X|X|
                if piece.piece_pos[1] - 1 >= 0:
                    legal_moves.apped((piece.piece_pos[0], piece.piece_pos[1] - 1))
                # |X|X|X|
                # |X|K|0|
                # |X|X|X|
                if piece.piece_pos[1] + 1 <= 7:
                    legal_moves.apped((piece.piece_pos[0], piece.piece_pos[1] + 1))
                # |0|X|X|
                # |X|K|X|
                # |X|X|X|
                if piece.piece_pos[0] - 1 >= 0 and piece.piece_pos[1] - 1 >= 0:
                    legal_moves.apped((piece.piece_pos[0] - 1, piece.piece_pos[1] - 1))
                # |X|X|0|
                # |X|K|X|
                # |X|X|X|
                if piece.piece_pos[0] - 1 >= 0 and piece.piece_pos[1] + 1 <= 7:
                    legal_moves.apped((piece.piece_pos[0] - 1, piece.piece_pos[1] - 1))
                # |X|X|X|
                # |X|K|X|
                # |0|X|X|
                if piece.piece_pos[0] + 1 <= 7 and piece.piece_pos[1] - 1 >= 0:
                    legal_moves.apped((piece.piece_pos[0] - 1, piece.piece_pos[1] - 1))
                # |X|X|X|
                # |X|K|X|
                # |X|X|0|
                if piece.piece_pos[0] + 1 <= 7 and piece.piece_pos[1] + 1 <= 7:
                    legal_moves.apped((piece.piece_pos[0] - 1, piece.piece_pos[1] - 1))

    def pawn_list_moves(self, piece):
        legal_moves = []
        if 7 >= piece.piece_pos[0] >= 0:
            if 7 >= piece.piece_pos[1] >= 0:

                if piece.colour == 'W':

                    # moving

                    if not piece.moved:
                        if piece.piece_pos[0] - 2 >= 0:
                            legal_moves.apped((piece.piece_pos[0] - 2, piece.piece_pos[1]))
                    if piece.piece_pos[0] - 1 >= 0:
                        legal_moves.apped((piece.piece_pos[0] - 1, piece.piece_pos[1]))

                    # capturing without en passant

                    if self.pos[piece.piece_pos[0] - 1][piece.piece_pos[1] - 1] != '' and piece.piece_pos[0] - 1 >= 0 \
                            and piece.piece_pos[1] - 1 >= 0:
                        pass

                    if self.pos[piece.piece_pos[0] - 1][piece.piece_pos[1] + 1] != '' and piece.piece_pos[0] - 1 >= 0 \
                            and piece.piece_pos[1] + 1 <= 7:
                        pass

                if piece.colour == "B":

                    # moving

                    if not piece.moved:
                        if piece.piece_pos[0] + 2 >= 0:
                            legal_moves.apped((piece.piece_pos[0] + 2, piece.piece_pos[1]))
                    if piece.piece_pos[0] + 1 >= 0:
                        legal_moves.apped((piece.piece_pos[0] + 1, piece.piece_pos[1]))

                    # capturing without en passant

                    if self.pos[piece.piece_pos[0] + 1][piece.piece_pos[1] - 1] != '' and piece.piece_pos[0] + 1 <= 7 \
                            and piece.piece_pos[1] - 1 >= 0:
                        pass

                    if self.pos[piece.piece_pos[0] + 1][piece.piece_pos[1] + 1] != '' and piece.piece_pos[0] + 1 <= 7 \
                            and piece.piece_pos[1] + 1 <= 7:
                        pass

    def knight_list_moves(self, piece):
        legal_moves = []


    def rook_list_moves(self, piece):
        legal_moves = []

    def queen_list_moves(self, piece):
        legal_moves = []

    def bishop_list_moves(self, piece):
        legal_moves = []
