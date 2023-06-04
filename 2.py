#实现方块自动增加

import pygame
import random
import sys

pygame.init()


window_size = (600, 400)

screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('my first game')


ball_pos = [50, 50]
ball_speed = [0, 0]
# print(ball_speed)
ball_color = (255, 0, 0)
circle_radius = 8

clock = pygame.time.Clock()

font = pygame.font.Font(None, 33)

ball_count = [[90, 30]]

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('上')
                ball_speed[1] = 1
                ball_speed[0] = 0
                ball_speed[1] = -ball_speed[1]
            if event.key == pygame.K_DOWN:
                print('下')
                ball_speed[0] = 0
                ball_speed[1] = 1

            if event.key == pygame.K_RIGHT:
                ball_speed[1] = 0
                print('右')
                ball_speed[0] = 1

            if event.key == pygame.K_LEFT:
                print('左')
                ball_speed[0] = 1
                ball_speed[1] = 0
                ball_speed[0] = -ball_speed[0]

    for ball_pos in ball_count:
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

    if ball_pos[0] > window_size[0] or ball_pos[0] < 0:
        ball_speed[0] = -ball_speed[0]
        # ball_speed[0] = 0
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if ball_pos[1] > window_size[1] or ball_pos[1] < 0:
        ball_speed[1] = -ball_speed[1]
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    screen.fill((0, 0, 0))

    for ball_pos in ball_count:
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(ball_pos[0], ball_pos[1], 10, 10))


    ball_fixed = [60, 60]
    pygame.draw.circle(screen, (255, 255, 255), ball_fixed, 8)

    if ball_pos[0] == ball_fixed[0] and ball_pos[1] == ball_fixed[1]:
        print('碰到一次')
        ball_count.append([ball_pos[0]+10, ball_pos[1]])

    # pygame.draw.rect(screen, ball_color, ball_pos, circle_radius)

    pygame.display.flip()
