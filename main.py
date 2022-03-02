import pygame

# import time
# import os

pygame.init()

screen = pygame.display.set_mode((1200, 674))
background = pygame.image.load("background1.png")
fps = 165
ani = 4
clock = pygame.time.Clock()

playerImg = pygame.image.load("mainplayer.png")
playerImgR = pygame.image.load("mainplayerR.png")
player1X = 0
player1Y = 593
player1X_change = 0
player1Y_change = 0
direction1 = "right"
player2X = 1120
player2Y = 593
player2X_change = 0
player2Y_change = 0
direction2 = "left"

jumps = 2


class Player:
    def __init__(self, x, y, d, xchange, ychange):
        self.x = x
        self.y = y
        self.d = d
        self.xchange = xchange
        self.ychange = ychange
        self.image = playerImg

    def make_player(self):
        if self.d == "right":
            screen.blit(playerImg, (self.x, self.y))
        else:
            screen.blit(playerImgR, (self.x, self.y))


def make_platforms():
    pygame.draw.rect(screen, (30, 38, 32), (200, 500, 150, 8))
    pygame.draw.rect(screen, (30, 38, 32), (350, 350, 150, 8))
    pygame.draw.rect(screen, (30, 38, 32), (475, 150, 150, 8))
    pygame.draw.rect(screen, (30, 38, 32), (800, 500, 150, 8))
    pygame.draw.rect(screen, (30, 38, 32), (700, 250, 150, 8))
    pygame.draw.rect(screen, (30, 38, 32), (600, 400, 150, 8))
    pygame.draw.rect(screen, (30, 38, 32), (1000, 200, 150, 8))
    pygame.draw.rect(screen, (30, 38, 32), (25, 175, 150, 8))


"""def players(x1, y1, x2, y2, d1, d2):
    if d1 == "right":
        screen.blit(playerImg, (x1, y1))
    else:
        screen.blit(playerImgR, (x1, y1))
    if d2 == "right":
        screen.blit(playerImg, (x2, y2))
    else:
        screen.blit(playerImgR, (x2, y2))"""
player1 = Player(player1X, player1Y, direction1, player1X_change, player1Y_change)
player2 = Player(player2X, player2Y, direction2, player2X_change, player2Y_change)

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_a:
                player1X_change = -8
                direction1 = "left"
            if ev.key == pygame.K_d:
                player1X_change = 8
                direction1 = "right"
            if ev.key == pygame.K_RIGHT:
                player2X_change = 8
                direction2 = "right"
            if ev.key == pygame.K_LEFT:
                player2X_change = -8
                direction2 = "left"
            if ev.key == pygame.K_w:
                player1Y_change = -20
                jumps -= 1
            if ev.key == pygame.K_UP:
                player2Y_change = -20
                jumps -= 1
        if ev.type == pygame.KEYUP:
            if ev.key == pygame.K_a or ev.key == pygame.K_d:
                player1X_change = 0
            if ev.key == pygame.K_RIGHT or ev.key == pygame.K_LEFT:
                player2X_change = 0
            if ev.key == pygame.K_w:
                player1Y_change = 0
            if ev.key == pygame.K_UP:
                player2Y_change = 0

    player1X += player1X_change
    player1Y += player1Y_change
    player2X += player2X_change
    player2Y += player2Y_change

    if player1X < 0:
        player1X = 1120
    elif player1X > 1120:
        player1X = 0
    if player1Y > 593:
        player1Y = 593
    elif player1Y < 0:
        player1Y = 0
    if player2X < 0:
        player2X = 1120
    elif player2X > 1120:
        player2X = 0
    if player2Y > 593:
        player2Y = 593
    elif player2Y < 0:
        player2Y = 0

    player1Y += 1.5
    player2Y += 1.5
    make_platforms()
    #players(player1X, player1Y, player2X, player2Y, direction1, direction2)
    player1.make_player()
    player2.make_player()
    clock.tick(fps)
    pygame.display.update()
