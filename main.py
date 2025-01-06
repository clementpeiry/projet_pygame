import pygame
import random
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
LARGEUR = 800
HAUTEUR = 400
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du dinosaure")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Images
dino_image = pygame.image.load("dino.png")
dino_image = pygame.transform.scale_by(dino_image, 0.25)
fond_image = pygame.image.load("fond.jpg")
obstacle_sol_image = pygame.image.load("obstacle_sol.png")
obstacle_sol_image = pygame.transform.scale_by(obstacle_sol_image, 0.1)
obstacle_air_image = pygame.image.load("obstacle_air.png")
obstacle_air_image = pygame.transform.scale_by(obstacle_air_image, 0.1)

# Police
font = pygame.font.SysFont(None, 40)

# FPS
clock = pygame.time.Clock()
FPS = 60

# Classes
class Dino:
    def __init__(self):
        self.image = dino_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = HAUTEUR - 100
        self.en_air = False
        self.velocity = 0

    def update(self):
        if not self.en_air:
            self.rect.y += self.velocity
            if self.rect.y > HAUTEUR - 100:
                self.rect.y = HAUTEUR - 100
                self.velocity = 0

    def jump(self):
        if not self.en_air:
            self.en_air = True
            self.velocity = -20

    def apply_gravity(self):
        if self.en_air:
            self.velocity += 1
            self.rect.y += self.velocity
            if self.rect.y >= HAUTEUR - 100:
                self.rect.y = HAUTEUR - 100
                self.en_air = False

class Fond:
    def __init__(self):
        self.image = fond_image
        self.x1 = 0
        self.x2 = self.image.get_width()

    def update(self):
        self.x1 -= 5
        self.x2 -= 5

        if self.x1 + self.image.get_width() <= 0:
            self.x1 = self.x2 + self.image.get_width()
        if self.x2 + self.image.get_width() <= 0:
            self.x2 = self.x1 + self.image.get_width()

    def draw(self):
        screen.blit(self.image, (self.x1, 0))
        screen.blit(self.image, (self.x2, 0))

class Obstacle:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= 5

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class ObstacleSol(Obstacle):
    def __init__(self):
        super().__init__(obstacle_sol_image, LARGEUR, HAUTEUR - 50)

class ObstacleAir(Obstacle):
    def __init__(self):
        super().__init__(obstacle_air_image, LARGEUR, HAUTEUR - 150)

    def update(self):
        self.rect.x -= 10

# Fonction principale
def main():
    running = True
    game_started = False
    dino = Dino()
    fond = Fond()
    obstacles = []
    chrono = 0
    scores = []
    rand1 = 0
    rand2 = 500

    while running:
        screen.fill(BLANC)
        fond.update()
        fond.draw()

        # Quitter le jeu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            # Début du jeu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_started:
                        game_started = True
                        chrono = pygame.time.get_ticks()
                    dino.jump()

        # Ecran d'accueil
        if not game_started:
            text = font.render("Appuyez sur Espace pour sauter", True, NOIR)
            screen.blit(text, (LARGEUR // 2 - text.get_width() // 2, HAUTEUR // 2))
            pygame.display.flip()
            clock.tick(FPS)
            continue

        dino.apply_gravity()
        dino.update()
        screen.blit(dino.image, dino.rect)

        # Gestion des obstacles
        if random.randint(rand1, rand2) < 2:
            if random.choice([True, False]):
                obstacles.append(ObstacleSol())
            else:
                obstacles.append(ObstacleAir())
            rand2 -= 5
            if rand2 < 20:
                rand2 = 20

        for obstacle in obstacles[:]:
            obstacle.update()
            obstacle.draw()
            if obstacle.rect.right < 0:
                obstacles.remove(obstacle)

            if dino.rect.colliderect(obstacle.rect):
                running = False
                break

        # Affichage du chrono
        elapsed_time = (pygame.time.get_ticks() - chrono) // 1000
        text = font.render(f"Temps: {elapsed_time}s", True, NOIR)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    scores.append(elapsed_time)
    end_game(scores)

def end_game(scores):
    while True:
        screen.fill(BLANC)
        text = font.render(f"Score: {scores[-1]}s", True, NOIR)
        screen.blit(text, (LARGEUR // 2 - text.get_width() // 2, HAUTEUR // 2 - 50))

        text = font.render("Voulez-vous rejouer ? (O/N)", True, NOIR)
        screen.blit(text, (LARGEUR // 2 - text.get_width() // 2, HAUTEUR // 2))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    main()
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()