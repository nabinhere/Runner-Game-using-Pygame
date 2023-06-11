import pygame

def main():

    # initialize pygame
    pygame.init()

    # set caption
    pygame.display.set_caption("Runner")

    # create an empty window of size 800X400
    screen = pygame.display.set_mode((800, 400))

    # setup font
    test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

    # set up clock to use for configuring the frame rate
    clock = pygame.time.Clock()

    sky_surface = pygame.image.load("graphics/sky.png").convert()
    ground_surface = pygame.image.load("graphics/ground.png").convert()
    text_surface = test_font.render("My game", False, "black")

    # Creating a Snail rectangle
    snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
    snail_rect = snail_surf.get_rect(midbottom = (600, 300))

    # Creating a player rectangle
    player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
    player_rect = player_surf.get_rect(midbottom = (80, 300))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # static part/images on the screen
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(text_surface, (300, 50))

        # dynamic part of the screen
        snail_rect.x -= 4
        if snail_rect.right <=0: snail_rect.left = 800 
        screen.blit(snail_surf, snail_rect)
        screen.blit(player_surf, player_rect)

        pygame.display.update()
        clock.tick(60)  #sets frame rate to 60, i.e, changes the images/surfaces 60 times per second

if __name__ == "__main__":
    main()