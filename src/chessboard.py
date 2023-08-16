from src.pieces import Rook, King, Pawn, Knight, Queen, Bishop, Colour, Empty
from colorama import Back, Style
import string


class ChessBoard:
    pos = [[Rook(Colour.Black), Knight(Colour.Black), Bishop(Colour.Black), Queen(Colour.Black), King(Colour.Black),
            Bishop(Colour.Black), Knight(Colour.Black), Rook(Colour.Black)],
           [Pawn(Colour.Black), Pawn(Colour.Black), Pawn(Colour.Black), Pawn(Colour.Black), Pawn(Colour.Black),
            Pawn(Colour.Black), Pawn(Colour.Black), Pawn(Colour.Black)],
           [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
           [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
           [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
           [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
           [Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn(), Pawn()],
           [Rook(), Knight(), Bishop(), Queen(), King(), Bishop(), Knight(), Rook()]]

    def bprint(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    print(Back.LIGHTWHITE_EX + '\033[1m' + f' {self.pos[i][j].show()} ' + '\033[0m' + Back.RESET,
                          end='')

                else:
                    print(Back.BLACK + f' {self.pos[i][j].show()} ' + Back.RESET, end='')

            print(Back.BLACK + "" + Back.RESET + f" {8 - i}")

        x = 0
        for letter in string.ascii_uppercase:
            print(" " + letter, end=" ")
            x += 1
            if x == 8:
                break
        print("")

    def turn(self):

        # choosing piece
        while True:
            piece = list(input("Which piece you want to move: \n"))
            fig = self.pos[8 - int(piece[1])][ord(piece[0].lower()) - 97]
            if len(piece) == 2 and 7 >= 8 - int(piece[1]) >= 0 and 7 >= ord(piece[0].lower()) - 97 >= 0 and fig.show() \
                    != ' ':
                break
            print("Wrong input! \n")

        # showing possible moves
        print(Back.RED + fig.show() + Back.RED, end='')

    def king_list_moves(self, piece_pos):
        legal_moves = []
        if 7 >= piece_pos[0] >= 0:
            if 7 >= piece_pos[1] >= 0:
                # |X|0|X|
                # |X|K|X|
                # |X|X|X|
                if piece_pos[0] - 1 >= 0:
                    legal_moves.apped((piece_pos[0] - 1, piece_pos[1]))
                # |X|X|X|
                # |X|K|X|
                # |X|0|X|
                if piece_pos[0] + 1 <= 7:
                    legal_moves.apped((piece_pos[0] + 1, piece_pos[1]))
                # |X|X|X|
                # |0|K|X|
                # |X|X|X|
                if piece_pos[1] - 1 >= 0:
                    legal_moves.apped((piece_pos[0], piece_pos[1] - 1))
                # |X|X|X|
                # |X|K|0|
                # |X|X|X|
                if piece_pos[1] + 1 <= 7:
                    legal_moves.apped((piece_pos[0], piece_pos[1] + 1))
                # |0|X|X|
                # |X|K|X|
                # |X|X|X|
                if piece_pos[0] - 1 >= 0 and piece_pos[1] - 1 >= 0:
                    legal_moves.apped((piece_pos[0] - 1, piece_pos[1] - 1))
                # |X|X|0|
                # |X|K|X|
                # |X|X|X|
                if piece_pos[0] - 1 >= 0 and piece_pos[1] + 1 <= 7:
                    legal_moves.apped((piece_pos[0] - 1, piece_pos[1] + 1))
                # |X|X|X|
                # |X|K|X|
                # |0|X|X|
                if piece_pos[0] + 1 <= 7 and piece_pos[1] - 1 >= 0:
                    legal_moves.apped((piece_pos[0] + 1, piece_pos[1] - 1))
                # |X|X|X|
                # |X|K|X|
                # |X|X|0|
                if piece_pos[0] + 1 <= 7 and piece_pos[1] + 1 <= 7:
                    legal_moves.apped((piece_pos[0] + 1, piece_pos[1] + 1))

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

        if 7 >= piece.piece_pos[0] >= 0:
            if 7 >= piece.piece_pos[1] >= 0:

                if piece.piece_pos[0] - 1 >= 0 and piece.piece_pos[1] - 2 >= 0:
                    legal_moves.apped((piece.piece_pos[0] - 1, piece.piece_pos[1] - 2))

                if piece.piece_pos[0] - 1 >= 0 and piece.piece_pos[1] + 2 <= 7:
                    legal_moves.apped((piece.piece_pos[0] - 1, piece.piece_pos[1] + 2))

                if piece.piece_pos[0] + 1 <= 7 and piece.piece_pos[1] - 2 >= 0:
                    legal_moves.apped((piece.piece_pos[0] + 1, piece.piece_pos[1] - 2))

                if piece.piece_pos[0] + 1 <= 7 and piece.piece_pos[1] + 2 <= 7:
                    legal_moves.apped((piece.piece_pos[0] + 1, piece.piece_pos[1] + 2))

    def rook_list_moves(self, piece):
        legal_moves = []

        if 7 >= piece.piece_pos[0] >= 0:
            if 7 >= piece.piece_pos[1] >= 0:
                while True:
                    pass

    def queen_list_moves(self, piece):
        legal_moves = []

        if 7 >= piece.piece_pos[0] >= 0:
            if 7 >= piece.piece_pos[1] >= 0:
                pass

    def bishop_list_moves(self, piece):
        legal_moves = []

        if 7 >= piece.piece_pos[0] >= 0:
            if 7 >= piece.piece_pos[1] >= 0:
                pass
