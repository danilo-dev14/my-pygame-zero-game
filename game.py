import pgzrun
import random
import time

WIDTH = 1000
HEIGHT = 794
game_over = False
player = Actor('square')
GO = Actor('gameover')
GO.x = WIDTH // 2
GO.y = HEIGHT // 2
enemy = Actor('enemy')
player.x = WIDTH // 2
player.y = HEIGHT // 1
count = 0


enemies = []

spawn_timer = 10
SPAWN_INTERVAL = 100
ENEMY_SPEED = 3

def bounce():
    y_final = HEIGHT - 50
    y_jump = HEIGHT - 200
    animate(player, duration=0.1, y=y_jump, tween='linear', on_finished=back_to_the_ground)

def back_to_the_ground():
    animate(player, duration=0.5, y=HEIGHT - 50, tween='bounce_end')


def create_enemy():
    """Cria um novo inimigo em uma posição Y aleatória e o adiciona à lista."""
    start_x = WIDTH + 50
    start_y = random.randint(0, HEIGHT)
    new_enemy = Actor('enemy', (start_x, start_y))
    enemies.append(new_enemy)

def update():
    global game_over
    if keyboard.left:
        player.x -= 5
    if keyboard.right:
        player.x += 5
    if keyboard.up:
        bounce()
    if keyboard.down:
        player.image = 'evade'
        animate(player, duration=2.0, on_finished=lambda: setattr(player, 'image', 'square'))
    if game_over == True:
        if keyboard.r:
            screen.clear()
            enemies.clear()
            game_over = False

    
    player.clamp_ip(0, 0, WIDTH, HEIGHT)
    global spawn_timer

    spawn_timer += 1
    if spawn_timer >= SPAWN_INTERVAL:
        create_enemy()
        spawn_timer = 0
        
    # Movimento e Remoção dos Inimigos
    enemies_to_remove = []
    
    for enemy in enemies:
        # Move para a esquerda
        enemy.x -= ENEMY_SPEED
        
        # Marca para remoção se sair da tela (X < -50)
        if enemy.right < 0:
            enemies_to_remove.append(enemy)

    # Remove os inimigos que saíram da tela
    for enemy in enemies_to_remove:
        enemies.remove(enemy)

def draw():
    global game_over
    if game_over == False:
        screen.draw.text(str(count), pos=(10, 10), color="white", fontsize=24)

        screen.clear()
        player.draw()
        for enemy in enemies:
            enemy.draw()
            if game_over == True:
                time.sleep(1)
                GO.draw()
                print('game over.')
            if (player.colliderect(enemy)):
                game_over = True
                

pgzrun.go()


