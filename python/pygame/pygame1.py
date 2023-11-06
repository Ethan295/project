import pygame
import sys
import time
# Inizializza Pygame
pygame.init()

# Imposta le dimensioni della schermata
x_schermata = pygame.display.Info().current_w
y_schermata = pygame.display.Info().current_h-50
schermata = pygame.display.set_mode((x_schermata, y_schermata))

# Imposta il titolo della finestra
pygame.display.set_caption("Schermata di gioco vuota")

# Carica l'immagine del personaggio e ridimensionala
personaggio = pygame.image.load("python/pygame/pg.png")
personaggioSinistra = pygame.image.load("python/pygame/pgSinistra.png")

lvl1background = pygame.image.load("python/pygame/lvl1background.png")
lvl1background = pygame.transform.scale(lvl1background, (x_schermata, y_schermata))  # Ridimensiona l'immagine alla dimensione della schermata


dimensione_personaggio_x = 200
dimensione_personaggio_y = 200
personaggio = pygame.transform.scale(personaggio, (dimensione_personaggio_x, dimensione_personaggio_y))
personaggioSinistra = pygame.transform.scale(personaggioSinistra, (dimensione_personaggio_x, dimensione_personaggio_y))


direzionePersonaggio = personaggio



pavimento1_x = 0
pavimento1_y = (y_schermata/100*85.5)
pavimento1 = pygame.Rect(pavimento1_x, pavimento1_y, x_schermata, 20) # Rettangolo del pavimento alle coordinate () e dimensioni ()

pavimento2_x = x_schermata/2.2
pavimento2_y = (y_schermata/100*74)
pavimento2 = pygame.Rect(pavimento2_x, pavimento2_y, x_schermata/2, y_schermata/10) 

pavimento3_x = x_schermata/7
pavimento3_y = y_schermata/1.27
pavimento3 = pygame.Rect(pavimento3_x, pavimento3_y, x_schermata/18, y_schermata/10)

pavimento4_x = 0
pavimento4_y = y_schermata/1.54
pavimento4 = pygame.Rect(pavimento4_x, pavimento4_y, x_schermata/8.7, 5)




Pavimenti = [pavimento1, pavimento2, pavimento3, pavimento4]

# Inizializza le coordinate del personaggio

x_personaggio = 50
y_personaggio = int(pavimento1_y/1.2)

y_iniziale_salto = y_personaggio

altezza_salto = 200
speed = 3
salto = False
run = True

discesa_salto = False




while run:
    def calcoloCollisioneTutto():
        for pavimento in Pavimenti:
            if pavimento.colliderect(pygame.Rect(x_personaggio, y_personaggio, dimensione_personaggio_x, dimensione_personaggio_y)):
                return True
        return False
    
    def calcoloCollisioneSingoloY(oggetto):
        if oggetto.colliderect(pygame.Rect(x_personaggio, y_personaggio-1, dimensione_personaggio_x, dimensione_personaggio_y)):
            return True
    def calcoloCollisioneSingoloX(oggetto):
        if oggetto.colliderect(pygame.Rect(x_personaggio-7, y_personaggio, 0, 0)):
            return True

    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_personaggio > 0:
        x_personaggio -= speed 
        direzionePersonaggio = personaggioSinistra

    if keys[pygame.K_RIGHT] and x_personaggio < x_schermata - dimensione_personaggio_x :
        direzionePersonaggio = personaggio
 
        x_personaggio += speed 

    if keys[pygame.K_UP] and not salto and not discesa_salto:
        salto = True
        y_iniziale_salto = y_personaggio
        

   

    if salto:
        y_personaggio -= speed * 2
        if y_personaggio < y_iniziale_salto - altezza_salto:
            salto = False
   


    if not calcoloCollisioneTutto() and not salto:
        y_personaggio += speed * 2
        discesa_salto = True
        
    if calcoloCollisioneTutto():
        discesa_salto = False
    
        
    schermata.blit(lvl1background, (0, 0))


    schermata.blit(direzionePersonaggio, (x_personaggio, y_personaggio))


    pygame.draw.rect(schermata, (0, 255, 0), pavimento1)
    pygame.draw.rect(schermata, (255, 0, 0), pavimento2)
    pygame.draw.rect(schermata, (0, 0, 255), pavimento3)
    pygame.draw.rect(schermata, (0, 255, 255), pavimento4)
    

    
    pygame.display.update()

pygame.quit()

#790.3750000000001 pavimento1.top
#1188
# 990.3750000000001 y_personaggio-dimensione_personaggio_y
#200

