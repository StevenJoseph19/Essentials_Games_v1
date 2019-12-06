import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:
    #Just like before to help us remember
    #pygame.draw.circle(WHERE TO DRAW, (RED, GREEN,
    # BLUE), (X COORDINATE, Y COORDINATE), RADIUS, HEIGHT,
    # WIDTH)
        # pygame.draw.circle(window, (255,255,0),
        #                     (250, 200), 20, 0)
        # pygame.draw.circle(window, (255,255,0),
        #                     (250, 200), 20, 2)

        # pygame.draw.ellipse(window, (255, 0, 0),
        #                     (100, 100, 100, 50))
        # pygame.draw.ellipse(window, (0, 255, 0),
        #             (100, 150, 80, 40))
        # pygame.draw.ellipse(window, (0, 0, 255),
        #             (100, 190, 60, 30))

        pygame.draw.rect(window, (255, 0, 0),
                        (100, 100, 100, 50), 2)
        pygame.draw.ellipse(window, (255, 0, 0),
                        (100, 100, 100, 50))
        pygame.draw.rect(window, (0, 255, 0),
                        (100, 150, 80, 40), 2)
        pygame.draw.ellipse(window, (0, 255, 0),
                           (100, 150, 80, 40))
        pygame.draw.rect(window, (0, 0, 255),
                        (100, 190, 60, 30), 2)
        pygame.draw.ellipse(window, (0, 0, 255),
                        (100, 190, 60, 30))
        
        #Circle
        pygame.draw.ellipse(window, (0, 0, 255),
                           (100, 250, 40, 40))
        
        pygame.display.update()
