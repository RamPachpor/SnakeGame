from turtle import  Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal ")

class  ScoreBoard(Turtle):

    def __init__(self):
        '''Initialise Scoreboard attributes'''
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as f:
            self.high_score = int(f.read())
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        '''Updates the Scoreboard'''
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(f"{self.high_score}")
        
        self.score=0
        self.update_scoreboard()
    

    def increase_score(self):
        '''Increases the Score'''
        self.score += 1
        self.update_scoreboard()
    
    