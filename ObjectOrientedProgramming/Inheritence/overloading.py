class PrintSquare:
    def __init__(self, side):
        self.side = side

    def __add__(square_1, square_2):
        return((4 * square_1.side) + (4 * square_2.side))


square_1 = PrintSquare(2)
square_2 = PrintSquare(5)

print("Sum of both sides of the square = ", square_1 + square_2)
