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
                    print(Back.WHITE + f' {self.pos[i][j]} ' + Back.RESET, end='')

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
                    legal_moves.apped((piece_pos[0] - 1, piece_pos[1] - 1))
                # |X|X|X|
                # |X|K|X|
                # |0|X|X|
                if piece_pos[0] + 1 <= 7 and piece_pos[1] - 1 >= 0:
                    legal_moves.apped((piece_pos[0] - 1, piece_pos[1] - 1))
                # |X|X|X|
                # |X|K|X|
                # |X|X|0|
                if piece_pos[0] + 1 <= 7 and piece_pos[1] + 1 <= 7:
                    legal_moves.apped((piece_pos[0] - 1, piece_pos[1] - 1))

    def pawn_list_moves(self, piece_pos):
        legal_moves = []


if __name__ == "__main__":
    ChessBoard().print()
    ChessBoard().turn()
# move = list(input("Make your move: \n"))
# od a do h
# print(ord('h')-96)
