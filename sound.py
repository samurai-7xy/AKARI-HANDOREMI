import pygame
from hand_detect import detect_hand

def play_sound():
    pygame.mixer.init()

    sounds = {
        0: pygame.mixer.Sound("sounds/do.wav"),
        1: pygame.mixer.Sound("sounds/re.wav"),
        2: pygame.mixer.Sound("sounds/mi.wav")
    }

    hand_id = detect_hand()
    sounds[hand_id].play()