#!/usr/bin/env python3
"""
ScarePi Audio - Basic scary sound script
Based on Network Chuck's tutorial: https://www.youtube.com/watch?v=X2YH-XyqyXE&t=787s

This is the basic audio-only version for Level 1 spookiness.
"""

import time
import pygame

def main():
    """Play scary sound effect."""
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load scary sound (you need to add your own scary_sound.ogg file)
    try:
        scary_sound = pygame.mixer.Sound("scary_sound.ogg")
        scary_sound.set_volume(1.0)  # Max volume
        
        print("Playing scary sound...")
        scary_sound.play()
        
        # Wait for sound to finish
        time.sleep(5)
        
    except pygame.error as e:
        print(f"Could not play sound file: {e}")
        print("Make sure you have a 'scary_sound.ogg' file in the same directory")
        print("You can convert any audio file to OGG format using Audacity or similar")

if __name__ == "__main__":
    main()
