import pgzrun

WIDTH = 900
HEIGHT = 800

square = Actor("square")
square.x = WIDTH // 2
square.y = HEIGHT // 1
bottom_y = HEIGHT - 30
y_jump = HEIGHT - 200


def bounce():
    y_final = HEIGHT - 50
    y_jump = HEIGHT - 200
    animate(square, duration=0.5, y=y_jump, tween='linear', on_finished=back_to_the_ground)

def back_to_the_ground():
    animate(square, duration=0.5, y=HEIGHT - 50, tween='bounce_end')

def on_mouse_down(pos):
    bounce()


def draw():
    screen.clear()
    square.draw()

def update():
        square.clamp_ip(0, 0, WIDTH, HEIGHT)
