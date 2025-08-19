import pygame
import time
import random

# 初始化 pygame
pygame.init()

# 定義遊戲視窗大小
width = 600
height = 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('貪食蛇遊戲')

# 顏色設定
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# 蛇的基本設定
snake_block = 10
snake_speed = 15
snake_pos = [[100, 50], [90, 50], [80, 50]] # 初始蛇的身體位置
direction = 'RIGHT'

# 時鐘物件：控制遊戲速度
clock = pygame.time.Clock()

# 產生食物
def generate_food():
    x = round(random.randrange(0, width - snake_block) / 10.0) * 10
    y = round(random.randrange(0, height - snake_block) / 10.0) * 10
    return [x, y]

food_pos = generate_food()

# 遊戲主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 鍵盤控制方向
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'

    # 移動蛇頭
    head = snake_pos[0][:]
    if direction == 'LEFT':
        head[0] -= snake_block
    elif direction == 'RIGHT':
        head[0] += snake_block
    elif direction == 'UP':
        head[1] -= snake_block
    elif direction == 'DOWN':
        head[1] += snake_block

    snake_pos.insert(0, head)

    # 檢查是否吃到食物
    if head == food_pos:
        food_pos = generate_food()
    else:
        snake_pos.pop()  # 沒吃到就移除尾巴

    # 撞牆或撞到自己 = 遊戲結束
    if (
        head[0] < 0 or head[0] >= width or
        head[1] < 0 or head[1] >= height or
        head in snake_pos[1:]
    ):
        running = False

    # 畫面更新
    win.fill(black)
    for segment in snake_pos:
        pygame.draw.rect(win, green, [segment[0], segment[1], snake_block, snake_block])

    pygame.draw.rect(win, red, [food_pos[0], food_pos[1], snake_block, snake_block])
    pygame.display.update()

    clock.tick(snake_speed)

# 結束畫面
font = pygame.font.SysFont("Arial", 35)
text = font.render("GAME OVER", True, red)
win.blit(text, [width / 2 - 80, height / 2 - 20])
pygame.display.update()
time.sleep(2)
pygame.quit()