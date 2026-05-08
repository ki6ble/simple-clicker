import pygame; from random import randint; import sys
pygame.init()
s_wid = 800; s_len = 600
screen = pygame.display.set_mode((s_wid, s_len))
pygame.display.set_caption("Simple clicker")

clock = pygame.time.Clock()

normal_font = pygame.font.Font(None, 36)
logo_font = pygame.font.Font(None, 72)

        
running = True
points = 0
pts_gain = 1
c_u_p = 100
game_state = "main"

def h_or_t(bet):
    global points
    flip = randint(1,2)
    if flip == 2:
        points+=bet
    else:
        points-=bet
        
while running:  
    
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT and game_state == "main":
                    points+=pts_gain
                    screen.blit(normal_font.render(f"Points: {points}", True, (255, 255, 255)), (50, 100))
            if event.type == pygame.KEYDOWN:
                if event.keu == pygame.K_F1:
                    points+=1000
                if event.key == pygame.K_m:
                    game_state = "shop"    
                if event.key == pygame.K_n:
                    game_state = "main"
                if event.key == pygame.K_b:
                    game_state = "casino"
                if event.key == pygame.K_1 and game_state == "shop" and points >= c_u_p:
                    points-= c_u_p
                    c_u_p += 150
                    pts_gain += 1     
                if event.key == pygame.K_1 and game_state == "casino" and points >= 100:
                    h_or_t(100)
                elif event.key == pygame.K_2 and game_state == "casino" and points >= 500:
                    h_or_t(500)
                elif event.key == pygame.K_3 and game_state == "casino" and points >= 500:
                    h_or_t(1000)
        
            
        if game_state == "main":
            screen.blit(normal_font.render("Main", True, (255, 255, 255)), (50, 375))
            screen.blit(normal_font.render("Press M for shop", True, (150, 150, 150)), (50, 410))
            screen.blit(normal_font.render("Press B for casino", True, (150, 150, 150)), (50, 445))
            screen.blit(normal_font.render(f"Points: {points}", True, (255, 255, 255)), (50, 100))
            screen.blit(normal_font.render(f"Points gain: {pts_gain}", True, (255, 255, 255)), (50, 150))
            screen.blit(logo_font.render("Simple clicker", True, (255, 255, 255)), (5, 550))
        
        elif game_state == "shop":
            screen.blit(normal_font.render("Shop", True, (255, 255, 255)), (50, 375))
            screen.blit(normal_font.render("Press N for menu", True, (150, 150, 150)), (50, 410))
            screen.blit(normal_font.render(f"1. +1 to your clicks! Price: {c_u_p} points", True, (255, 255, 255)), (50, 100))
            screen.blit(logo_font.render("Simple clicker", True, (255, 255, 255)), (5, 550))
            
        elif game_state == "casino":
            screen.blit(normal_font.render("HEADS OR TAILS.", True, (255, 255, 0)), (280, 100))
            screen.blit(normal_font.render("1. Bet 100", True, (255, 255, 255)), (100, 150))
            screen.blit(normal_font.render("2. Bet 500", True, (255, 255, 255)), (100, 200))
            screen.blit(normal_font.render("3. Bet 1000", True, (255, 255, 255)), (100, 250))
            screen.blit(logo_font.render("Simple clicker", True, (255, 255, 255)), (5, 550))
            screen.blit(normal_font.render(f"Points: {points}", True, (255, 255, 255)), (50, 100))
            screen.blit(normal_font.render("Press N for menu", True, (150, 150, 150)), (50, 410))
            screen.blit(normal_font.render("Casino", True, (255, 255, 255)), (50, 375))
            
        pygame.display.flip()
            
            
        clock.tick(30)
            
   
        
        

            