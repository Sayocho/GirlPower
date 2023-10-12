import pygame

pygame.init()

# Initialize the mixer (you must do this before using sound)
pygame.mixer.init()

# Load a sound file
sound = pygame.mixer.Sound('C:\Users\blood\Downloads\untitled_zd2ts4l-audiotrimmer_7vAtKUf.mp3')

# Play the sound
sound.play()

# Wait for the sound to finish playing
pygame.time.wait(int(sound.get_length() * 1000))  # wait in milliseconds

# Clean up
pygame.quit()
