import pygame
import sys
import time
# Inizializza Pygame
pygame.init()

# Imposta le dimensioni della schermata
schermata = pygame.display.set_mode((800, 600))

# Imposta il titolo della finestra
pygame.display.set_caption("Schermata di gioco vuota")

# Carica l'immagine del personaggio e ridimensionala
personaggio = pygame.image.load("python/pygame/pg.png")
personaggioSinistra = pygame.image.load("python/pygame/pgSinistra.png")

lvl1background = pygame.image.load("python/pygame/lvl1background.png")
lvl1background = pygame.transform.scale(lvl1background, (800, 600))  # Ridimensiona l'immagine alla dimensione della schermata


dimensione_personaggio_x = 100
dimensione_personaggio_y = 100
personaggio = pygame.transform.scale(personaggio, (dimensione_personaggio_x, dimensione_personaggio_y))
personaggioSinistra = pygame.transform.scale(personaggioSinistra, (dimensione_personaggio_x, dimensione_personaggio_y))

direzionePersonaggio = personaggio

x_personaggio = 50
y_personaggio = 420

pavimento1_x = 0
pavimento1_y = 515
pavimento1 = pygame.Rect(pavimento1_x, pavimento1_y, 800, 20) # Rettangolo del pavimento alle coordinate (0, 500) e dimensioni (800, 100)

pavimento2_x = 373
pavimento2_y = 447
pavimento2 = pygame.Rect(pavimento2_x, pavimento2_y, 400, 100) # Rettangolo del pavimento alle coordinate (0, 500) e dimensioni (800, 100)


Pavimenti = [pavimento1, pavimento2]

# Inizializza le coordinate del personaggio


y_iniziale_salto = y_personaggio

altezza_salto = 100
speed = 0.07
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
        if oggetto.colliderect(pygame.Rect(x_personaggio-7, y_personaggio, dimensione_personaggio_x, 0)):
            return True

    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x_personaggio > 0:
        x_personaggio -= speed 
        direzionePersonaggio = personaggioSinistra

    if keys[pygame.K_RIGHT] and x_personaggio < 700 :
        direzionePersonaggio = personaggio
        if(not calcoloCollisioneSingoloX(pavimento2)):
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



    pygame.draw.rect(schermata, (255, 0, 0), pavimento2)
    
    pygame.draw.rect(schermata, (0, 255, 0), pavimento1)

    
    pygame.display.update()

pygame.quit()
