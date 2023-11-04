#初步认识pygame

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
                ball_speed[0] =0
                ball_speed[1] = -ball_speed[1]
            if event.key == pygame.K_DOWN:
                print('下')
                ball_speed[0] =0
                ball_speed[1] = 1
                # ball_speed[1] = -ball_speed[1]
            if event.key == pygame.K_RIGHT:
                ball_speed[1] =0
                print('右')
                ball_speed[0] = 1
                
            if event.key == pygame.K_LEFT:
                print('左')
                ball_speed[0] = 1
                ball_speed[1] =0
                ball_speed[0] = -ball_speed[0]


    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]


        

    if ball_pos[0] > window_size[0] or ball_pos[0] < 0:
        ball_speed[0] = -ball_speed[0]
        # ball_speed[0] = 0
        ball_color = (random.randint(0, 255), 0, random.randint(0, 255))

    if ball_pos[1] > window_size[1] or ball_pos[1] < 0:
        ball_speed[1] = -ball_speed[1]
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    screen.fill((0, 0, 0))

    # text_surface = font.render('{},{}'.format(ball_pos[0], ball_pos[1]), True, (255, 255, 255))

    # screen.blit(text_surface, (ball_pos[0]+2, ball_pos[1]+4))

    pygame.draw.circle(screen, ball_color, ball_pos, circle_radius)

    # ball_fixed = [60,60]
    # pygame.draw.circle(screen, (255,255,255), ball_fixed, 8)

    # if ball_pos[0] == ball_fixed[0]:
    #     print('碰到一次')
    #     pygame.draw.circle(screen, (255,255,255), [ball_pos[0]+10, ball_pos[1]+10], 8)



    pygame.display.flip()
