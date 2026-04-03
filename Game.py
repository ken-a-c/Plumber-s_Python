import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))



x = 50
y = 200
vel_y = 0

floor_y = 250
ground = floor_y - 20  

items = [110, 230, 300, 400, 500]
win = False

while True:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()




    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5

    if keys[pygame.K_SPACE] and y == ground:
        vel_y = -10




    vel_y += 1
    y += vel_y

    

    if y > ground:
        y = ground
        vel_y = 0

    
    for item in items[:]:
        if abs(x - item) < 20:
            items.remove(item)



    if len(items) == 0:
        win = True



    screen.fill((255,255,255))

    pygame.draw.rect(screen, (0,200,0), (0, floor_y, 600, 50))  
    pygame.draw.rect(screen, (0,0,255), (x, y, 20, 20))         

    for item in items:
        pygame.draw.rect(screen, (255,200,0), (item, 220, 10, 10))

    if win:
        font = pygame.font.SysFont(None, 40)
        text = font.render("YOU WIN :)", True, (0,0,0))
        screen.blit(text, (200, 100))

    pygame.display.update()
