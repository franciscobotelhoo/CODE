import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load(r"Exercícios/Mundo 1/021.mp3")
pygame.mixer.music.set_volume(0.5)  # Máximo
pygame.mixer.music.play()

time.sleep(500)  # Aguarda 500 segundos para tocar
