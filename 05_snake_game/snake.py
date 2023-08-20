from turtle import Turtle

Left = 180
Right = 0
Up = 90
Down = 270
move_distance = 20

class Snake:
    def __init__(self, length):
        # generate snake shape
        self.snake = []
        self.ate = False
        for i in range(length):
            self.extend(0 - move_distance * i, 0)
        self.snakeHead = self.snake[0]
        self.snakeHead.color("orange")

    def tail_position(self):
        return self.snake[len(self.snake)-1].pos()

    def tail(self):
        return self.snake[len(self.snake)-1]

    def move(self):
        length = len(self.snake)
        for i in range(len(self.snake) - 1, 0, -1):
            if self.snake[0] is i:
                continue
            self.snake[i].setpos(self.snake[i - 1].pos()[0], self.snake[i - 1].pos()[1])
        self.snakeHead.forward(move_distance)
        if self.ate:
            self.extend(self.tail_position()[0], self.tail_position()[1])
            self.ate = False


    def left(self):
        if self.snakeHead.heading() != Right:
            self.snakeHead.setheading(Left)

    def right(self):
        if self.snakeHead.heading() != Left:
            self.snakeHead.setheading(Right)

    def up(self):
        if self.snakeHead.heading() != Down:
            self.snakeHead.setheading(Up)

    def down(self):
        if self.snakeHead.heading() != Up:
            self.snakeHead.setheading(Down)

    def eat_own_tail(self):
        for segment in self.snake[1:]:
            if self.snakeHead.distance(segment) < 10:
                return True
        return False

    def extend(self, x, y):
        self.snake.append(Turtle(shape="square"))
        self.tail().color("white")
        self.tail().penup()
        self.tail().setpos(x, y)

