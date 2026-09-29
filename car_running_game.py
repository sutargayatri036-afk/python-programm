import turtle
import random

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(600, 700)
screen.bgcolor("green")
screen.title("🏎️ Car Racing Game")
screen.tracer(0)

# ---------------- ROAD ----------------
road = turtle.Turtle()
road.shape("square")
road.color("gray")
road.shapesize(stretch_wid=35, stretch_len=20)
road.penup()
road.goto(0, 0)

# ---------------- ROAD LINES ----------------
lines = []

for y in range(-300, 350, 100):
    line = turtle.Turtle()
    line.shape("square")
    line.color("white")
    line.shapesize(stretch_wid=3, stretch_len=0.5)
    line.penup()
    line.goto(0, y)
    lines.append(line)

# ---------------- PLAYER CAR ----------------
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.shapesize(stretch_wid=1.5, stretch_len=1)
player.penup()
player.goto(0, -250)

# ---------------- ENEMY CARS ----------------
enemies = []

for x in [-120, 0, 120]:
    enemy = turtle.Turtle()
    enemy.shape("square")
    enemy.color("red")
    enemy.shapesize(stretch_wid=1.5, stretch_len=1)
    enemy.penup()
    enemy.goto(x, random.randint(200, 500))
    enemies.append(enemy)

# ---------------- SCORE ----------------
score = 0
speed = 5

score_text = turtle.Turtle()
score_text.color("white")
score_text.penup()
score_text.hideturtle()
score_text.goto(-270, 310)

score_text.write(
    "Score: 0",
    font=("Arial", 18, "bold")
)

# ---------------- PLAYER MOVEMENT ----------------
def move_left():
    if player.xcor() > -150:
        player.setx(player.xcor() - 30)

def move_right():
    if player.xcor() < 150:
        player.setx(player.xcor() + 30)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# ---------------- GAME ----------------
def game():
    global score, speed

    # Move road lines
    for line in lines:
        line.sety(line.ycor() - speed)

        if line.ycor() < -350:
            line.sety(350)

    # Move enemy cars
    for enemy in enemies:
        enemy.sety(enemy.ycor() - speed)

        # Reset enemy when it leaves screen
        if enemy.ycor() < -350:
            enemy.goto(
                random.choice([-120, 0, 120]),
                random.randint(300, 600)
            )

            score += 1

            score_text.clear()
            score_text.write(
                "Score: " + str(score),
                font=("Arial", 18, "bold")
            )

            # Increase speed
            if score % 5 == 0:
                speed += 1

        # Collision
        if player.distance(enemy) < 30:
            score_text.goto(-110, 0)
            score_text.clear()
            score_text.write(
                "GAME OVER!",
                font=("Arial", 28, "bold")
            )
            return

    screen.update()
    screen.ontimer(game, 30)


# ---------------- START ----------------
game()
turtle.mainloop()
