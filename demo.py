####chatgpt自动生产程序



import pygame
import sys

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
window_size = (800, 600)

# 创建窗口
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My First Pygame Program")

# 设置小球的初始位置和速度
ball_pos = [400, 300]
ball_speed = [2, 2]

# 创建计时器对象
clock = pygame.time.Clock()

# 游戏主循环
while True:
    # 设置帧率（每秒钟的帧数）
    frame_rate = 60
    clock.tick(frame_rate)

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 移动小球
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # 碰撞检测
    if ball_pos[0] < 0 or ball_pos[0] > window_size[0]:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] < 0 or ball_pos[1] > window_size[1]:
        ball_speed[1] = -ball_speed[1]

    # 填充背景色
    screen.fill((0, 0, 0))

    # 绘制小球
    pygame.draw.circle(screen, (255, 255, 255), ball_pos, 20)

    # 更新屏幕
    pygame.display.flip()
