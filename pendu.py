import pygame
import random

# Initialisation de Pygame
pygame.init()

# Charger les mots depuis un fichier texte
def charger_mots(fichier):
    try:
        with open(fichier, "r") as f:
            mots = f.read().splitlines()
            return [mot.strip() for mot in mots if mot.isalpha()]
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier} est introuvable.")
        return []

# Charger les images du pendu
def charger_images():
    images = []
    for i in range(7):
        try:
            image = pygame.image.load(f"pendu{i}.png")
            images.append(image)
        except pygame.error:
            print(f"Erreur : L'image pendu{i}.png est introuvable.")
            exit()
    return images

# Configuration de base
WIDTH, HEIGHT = 1000, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Police d'écriture
FONT = pygame.font.SysFont("comicsans", 40)

# Charger les mots et les images
mots = charger_mots("mots.txt")
images = charger_images()
if not mots:
    print("Le fichier 'mots.txt' est vide ou contient des données incorrectes.")
    exit()

# Initialisation des variables du jeu
def redemarrer():
    global mot_a_trouver, lettres_trouvees, tentatives_restantes, lettres_utilisees
    mot_a_trouver = random.choice(mots).upper()
    lettres_trouvees = ["_" for _ in mot_a_trouver]
    tentatives_restantes = 6
    lettres_utilisees = set()

redemarrer()

# Afficher un message
def afficher_message(message, couleur):
    win.fill(WHITE)
    texte = FONT.render(message, True, couleur)
    win.blit(texte, (WIDTH // 2 - texte.get_width() // 2, HEIGHT // 2 - texte.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

# Dessiner le jeu
def draw_game():
    win.fill(WHITE)
    display_word = " ".join(lettres_trouvees)
    mot_text = FONT.render(display_word, True, BLACK)
    win.blit(mot_text, (WIDTH // 2 - mot_text.get_width() // 2, 500))

    used_letters_text = FONT.render(" ".join(sorted(lettres_utilisees)), True, BLUE)
    win.blit(used_letters_text, (WIDTH // 2 - used_letters_text.get_width() // 2, 400))

    win.blit(images[6 - tentatives_restantes], (150, 100))
    remaining_text = FONT.render(f"Tentatives restantes: {tentatives_restantes}", True, RED)
    win.blit(remaining_text, (10, 10))
    pygame.display.update()

# Boucle principale
run = True
while run:
    draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            lettre = event.unicode.upper()
            if lettre.isalpha() and lettre not in lettres_utilisees:
                lettres_utilisees.add(lettre)
                if lettre in mot_a_trouver:
                    for i in range(len(mot_a_trouver)):
                        if mot_a_trouver[i] == lettre:
                            lettres_trouvees[i] = lettre
                else:
                    tentatives_restantes -= 1
            else:
                print(f"Lettre '{lettre}' déjà utilisée.")

    if "_" not in lettres_trouvees:
        afficher_message("Félicitations, vous avez gagné !", BLUE)
        redemarrer()

    if tentatives_restantes == 0:
        afficher_message(f"Vous avez perdu ! Le mot était {mot_a_trouver}", RED)
        redemarrer()

pygame.quit()
