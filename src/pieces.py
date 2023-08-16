import enum


class Colour(enum.Enum):
    White = 0
    Black = 1


class King:
    check = False
    moved = False

    def __init__(self, colour: Colour = Colour.White):
        self.colour = colour

    def show(self):
        if self.colour == Colour.White:
            return 'K'
        else:
            return 'k'


class Pawn:
    moved = False

    def __init__(self, colour: Colour = Colour.White):
        self.colour = colour

    def show(self):
        if self.colour == Colour.White:
            return 'P'
        else:
            return 'p'


class Knight:

    def __init__(self, colour: Colour = Colour.White):
        self.colour = colour

    def show(self):
        if self.colour == Colour.White:
            return 'N'
        else:
            return 'n'


class Bishop:

    def __init__(self, colour: Colour = Colour.White):
        self.colour = colour

    def show(self):
        if self.colour == Colour.White:
            return 'B'
        else:
            return 'b'


class Rook:
    moved = False

    def __init__(self, colour: Colour = Colour.White):
        self.colour = colour

    def show(self):
        if self.colour == Colour.White:
            return 'R'
        else:
            return 'r'


class Queen:

    def __init__(self, colour: Colour = Colour.White):
        self.colour = colour

    def show(self):
        if self.colour == Colour.White:
            return 'Q'
        else:
            return 'q'


class Empty:

    def __init__(self):
        pass

    def show(self):
        return ' '
