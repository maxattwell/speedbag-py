import time
import pygame

pygame.mixer.init()


def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()


def timer(seconds):
    play_sound("1_audio_1.wav")
    time.sleep(seconds)
    play_sound("1_audio_1.wav")


if __name__ == "__main__":
    timer(4)
