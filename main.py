import pygame

def main():

    # initialize pygame
    pygame.init()

    # set caption
    pygame.display.set_caption("Runner")

    # create an empty window of size 800X400
    screen = pygame.display.set_mode((800, 400))

    # setup font
    font = pygame.font.Font("font/Pixeltype.ttf", 50)

    # set up clock to use for configuring the frame rate
    clock = pygame.time.Clock()

    sky_surface = pygame.image.load("graphics/sky.png").convert()
    ground_surface = pygame.image.load("graphics/ground.png").convert()
    score_surf = font.render("Snail Sprint", False, (64,64,64))
    score_rect = score_surf.get_rect(centerx = 400, centery = 50)

    # Creating a Snail rectangle
    snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
    snail_rect = snail_surf.get_rect(midbottom = (600, 300))

    # Creating a player rectangle
    player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
    player_rect = player_surf.get_rect(midbottom = (80, 300))
    player_gravity = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                     
            if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE) and (player_rect.bottom == 300):
                        player_gravity = -20

            if pygame.mouse.get_pressed()[0]:
                if player_rect.collidepoint(pygame.mouse.get_pos()) and (player_rect.bottom == 300):
                    player_gravity = -20
                          
        # static part/images on the screen
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, "#c0e8ec", score_rect)
        pygame.draw.rect(screen, "#c0e8ec", score_rect, 6)
        screen.blit(score_surf, score_rect)

        # dynamic part of the screen
        snail_rect.x -= 4
        if snail_rect.right <=0: snail_rect.left = 800 
        screen.blit(snail_surf, snail_rect)

        player_gravity +=1
        player_rect.bottom += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
                                                                 
        pygame.display.update()
        clock.tick(60)  #sets frame rate to 60, i.e, changes the images/surfaces 60 times per second

if __name__ == "__main__":
    main()