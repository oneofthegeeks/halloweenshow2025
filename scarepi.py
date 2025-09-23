#!/usr/bin/env python3
"""
ScarePi - Network Chuck's Raspberry Pi Haunted House Project
Based on: https://www.youtube.com/watch?v=X2YH-XyqyXE&t=787s

Features:
- Motion sensor detection
- Relay control for Halloween props
- Camera recording
- Scary sound effects
- Automated Halloween scares
"""

import RPi.GPIO as GPIO
import time
import pygame
import signal
import sys
from datetime import datetime
from picamera import PiCamera

class ScarePi:
    def __init__(self, motion_pin=35, relay_pin=37):
        """Initialize ScarePi with motion sensor and relay pins."""
        self.motion_pin = motion_pin
        self.relay_pin = relay_pin
        self.running = True
        
        # Setup GPIO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        
        # Setup motion sensor (input)
        GPIO.setup(self.motion_pin, GPIO.IN)
        
        # Setup relay (output)
        GPIO.setup(self.relay_pin, GPIO.OUT)
        GPIO.output(self.relay_pin, GPIO.HIGH)  # Start with relay open
        
        # Setup camera
        self.camera = PiCamera()
        self.camera.resolution = (1920, 1080)
        self.camera.framerate = 30
        
        # Setup pygame for sound
        pygame.mixer.init()
        
        # Setup signal handlers for clean shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
        
        print("🎃 ScarePi initialized!")
        print(f"👁️ Motion sensor on pin: {self.motion_pin}")
        print(f"⚡ Relay on pin: {self.relay_pin}")
        print("🌙 Ready to spook!")
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully."""
        print("\nShutting down ScarePi...")
        self.running = False
        self.cleanup()
        sys.exit(0)
    
    def cleanup(self):
        """Clean up GPIO pins and camera."""
        GPIO.output(self.relay_pin, GPIO.HIGH)  # Open relay
        GPIO.cleanup()
        self.camera.close()
        print("GPIO and camera cleaned up.")
    
    def motion_detected(self):
        """Check if motion is currently detected."""
        return GPIO.input(self.motion_pin) == 1
    
    def trigger_prop(self, duration=2.0):
        """Trigger Halloween prop by closing relay."""
        print("🦇 BOO! Triggering prop...")
        GPIO.output(self.relay_pin, GPIO.LOW)  # Close relay
        time.sleep(duration)
        GPIO.output(self.relay_pin, GPIO.HIGH)  # Open relay
        print("⚡ Prop triggered!")
    
    def play_scary_sound(self, sound_file="scary_sound.ogg"):
        """Play scary sound effect."""
        try:
            scary_sound = pygame.mixer.Sound(sound_file)
            scary_sound.set_volume(1.0)  # Max volume
            scary_sound.play()
            print(f"🔊 Playing scary sound: {sound_file}")
        except pygame.error as e:
            print(f"❌ Could not play sound file {sound_file}: {e}")
            print("💡 Make sure you have a scary sound file in OGG format")
    
    def record_scare(self, filename=None):
        """Record video of the scare."""
        if filename is None:
            current = datetime.now()
            filename = f"scare_{current.strftime('%Y%m%d_%H%M%S')}.h264"
        
        print(f"📹 Recording scare: {filename}")
        self.camera.start_recording(filename)
        time.sleep(2)  # Record for 2 seconds
        self.camera.stop_recording()
        print(f"🎬 Scare recorded: {filename}")
        return filename
    
    def run_motion_detection(self):
        """Main loop - detect motion and trigger scares."""
        print("Motion detection active...")
        print("Waiting for motion...")
        
        while self.running:
            motion_detected = GPIO.input(self.motion_pin)
            
            if motion_detected == 1:
                print("MOTION DETECTED! BOO!")
                
                # Start recording first
                self.record_scare()
                
                # Trigger the prop
                self.trigger_prop()
                
                # Play scary sound
                self.play_scary_sound()
                
                # Wait a bit before detecting motion again
                time.sleep(5)
                print("Waiting for motion...")
            
            time.sleep(0.1)  # Small delay to prevent excessive CPU usage

def main():
    """Main function."""
    print("=== ScarePi - Network Chuck's Haunted House ===")
    print("Based on: https://www.youtube.com/watch?v=X2YH-XyqyXE")
    print()
    
    # Create ScarePi instance
    # Pin 35 for motion sensor, Pin 37 for relay (as per video)
    scarepi = ScarePi(motion_pin=35, relay_pin=37)
    
    try:
        # Start motion detection
        scarepi.run_motion_detection()
    
    except KeyboardInterrupt:
        print("\nStopping ScarePi...")
    finally:
        scarepi.cleanup()

if __name__ == "__main__":
    main()