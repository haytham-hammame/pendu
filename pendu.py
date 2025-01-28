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