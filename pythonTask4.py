class Chess:
    def __init__(self, color):
        self.color = color

    def check(self, start, end):
        pass


class Pawn(Chess):
    def __init__(self, color):
        super().__init__(color)

    def check(self, start, end):
        start_x, start_y = start
        end_x, end_y = end

        if self.color == "white":
            return start_x == end_x and end_y == start_y + 1
        elif self.color == "black":
            return start_x == end_x and end_y == start_y - 1
        else:
            return False


class Knight(Chess):
    def __init__(self, color):
        super().__init__(color)

    def check(self, start, end):
        start_x, start_y = start
        end_x, end_y = end

        return (abs(end_x - start_x) == 2 and abs(end_y - start_y) == 1) or \
               (abs(end_y - start_y) == 2 and abs(end_x - start_x) == 1)


knight = Knight("black")
print(knight.check((1, 2), (3, 3)))  
print(knight.check((1, 2), (1, 4)))  

knight_white = Knight("white")
print(knight_white.check((1, 2), (1, 3))) 
print(knight_white.check((1, 2), (1, 4))) 
