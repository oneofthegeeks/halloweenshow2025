#!/usr/bin/env python3
"""
Motion Test - Test motion sensor detection
Based on Network Chuck's tutorial: https://www.youtube.com/watch?v=X2YH-XyqyXE&t=787s

This script tests the motion sensor to make sure it's working properly.
"""

import RPi.GPIO as GPIO
import time

def main():
    """Test motion sensor."""
    # Setup GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    
    # Motion sensor on pin 35
    motion_pin = 35
    GPIO.setup(motion_pin, GPIO.IN)
    
    print("Motion sensor test active...")
    print("Wave your hand in front of the sensor!")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            motion_detected = GPIO.input(motion_pin)
            print(f"Motion sensor reading: {motion_detected}")
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\nStopping motion test...")
    finally:
        GPIO.cleanup()
        print("GPIO cleaned up.")

if __name__ == "__main__":
    main()
