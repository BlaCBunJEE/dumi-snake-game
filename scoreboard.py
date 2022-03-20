from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('courier', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.score_update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.score_update()



