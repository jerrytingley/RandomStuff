import pygame

def jplusj(sa, sb):
  pygame.mixer.init()
  pygame.init()
  sounds = [pygame.mixer.Sound(sa), pygame.mixer.Sound(sb)]
  for song in sounds:
    song.play()
