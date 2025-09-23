#!/usr/bin/env python3
"""
ScarePi Web UI - Mock Version for Local Testing
A spooky web interface for testing on Mac/Windows without Raspberry Pi hardware!
"""

from flask import Flask, render_template, jsonify, request
import threading
import time
import json
import os
from datetime import datetime

app = Flask(__name__)

# Mock ScarePi instance for testing
class MockScarePi:
    def __init__(self, motion_pin=35, relay_pin=37):
        """Mock ScarePi for local testing."""
        self.motion_pin = motion_pin
        self.relay_pin = relay_pin
        self.running = True
        print("🎃 Mock ScarePi initialized for local testing!")
        print(f"👁️ Mock Motion sensor on pin: {self.motion_pin}")
        print(f"⚡ Mock Relay on pin: {self.relay_pin}")
        print("🌙 Ready to spook (virtually)!")
    
    def motion_detected(self):
        """Mock motion detection - returns random results for testing."""
        import random
        return random.choice([True, False, False, False])  # 25% chance of motion
    
    def trigger_prop(self, duration=2.0):
        """Mock prop trigger."""
        print("🦇 BOO! Mock prop triggered!")
        time.sleep(duration)
        print("⚡ Mock prop finished!")
    
    def play_scary_sound(self, sound_file="scary_sound.ogg"):
        """Mock sound playing."""
        print(f"🔊 Mock playing scary sound: {sound_file}")
        time.sleep(1)  # Simulate sound duration
    
    def record_scare(self, filename=None):
        """Mock video recording."""
        if filename is None:
            current = datetime.now()
            filename = f"mock_scare_{current.strftime('%Y%m%d_%H%M%S')}.h264"
        
        print(f"📹 Mock recording scare: {filename}")
        time.sleep(2)  # Simulate recording time
        print(f"🎬 Mock scare recorded: {filename}")
        return filename

# Global mock ScarePi instance
scarepi = None
motion_enabled = False
motion_thread = None

def init_scarepi():
    """Initialize the mock ScarePi system."""
    global scarepi
    try:
        scarepi = MockScarePi(motion_pin=35, relay_pin=37)
        return True
    except Exception as e:
        print(f"Failed to initialize mock ScarePi: {e}")
        return False

def motion_detection_loop():
    """Background thread for mock motion detection."""
    global motion_enabled, scarepi
    print("Mock motion detection thread started...")
    
    while motion_enabled and scarepi:
        try:
            motion_detected = scarepi.motion_detected()
            if motion_detected:
                print("MOCK MOTION DETECTED! BOO!")
                # Trigger full scare sequence
                trigger_full_scare()
                time.sleep(5)  # Cooldown period
            time.sleep(0.1)
        except Exception as e:
            print(f"Mock motion detection error: {e}")
            break

def trigger_full_scare():
    """Trigger the complete mock scare sequence."""
    if scarepi:
        scarepi.record_scare()
        scarepi.trigger_prop()
        scarepi.play_scary_sound()

@app.route('/')
def index():
    """Main Halloween control panel."""
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    """Get current system status."""
    return jsonify({
        'motion_enabled': motion_enabled,
        'scarepi_initialized': scarepi is not None,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/motion/toggle', methods=['POST'])
def toggle_motion():
    """Toggle motion detection on/off."""
    global motion_enabled, motion_thread
    
    motion_enabled = not motion_enabled
    
    if motion_enabled:
        if motion_thread is None or not motion_thread.is_alive():
            motion_thread = threading.Thread(target=motion_detection_loop, daemon=True)
            motion_thread.start()
        return jsonify({'status': 'enabled', 'message': 'Mock motion detection activated! 👻'})
    else:
        return jsonify({'status': 'disabled', 'message': 'Mock motion detection deactivated 🛑'})

@app.route('/api/scare/full', methods=['POST'])
def trigger_full_scare_api():
    """Manually trigger full scare sequence."""
    if scarepi:
        threading.Thread(target=trigger_full_scare, daemon=True).start()
        return jsonify({'message': 'Full mock scare sequence triggered! 🎃💀'})
    return jsonify({'error': 'Mock ScarePi not initialized'}), 500

@app.route('/api/scare/prop', methods=['POST'])
def trigger_prop():
    """Manually trigger prop only."""
    if scarepi:
        threading.Thread(target=scarepi.trigger_prop, daemon=True).start()
        return jsonify({'message': 'Mock prop triggered! 🦇'})
    return jsonify({'error': 'Mock ScarePi not initialized'}), 500

@app.route('/api/scare/sound', methods=['POST'])
def trigger_sound():
    """Manually trigger sound only."""
    if scarepi:
        threading.Thread(target=scarepi.play_scary_sound, daemon=True).start()
        return jsonify({'message': 'Mock scary sound playing! 🔊👻'})
    return jsonify({'error': 'Mock ScarePi not initialized'}), 500

@app.route('/api/scare/record', methods=['POST'])
def trigger_record():
    """Manually start recording."""
    if scarepi:
        filename = scarepi.record_scare()
        return jsonify({'message': f'Mock recording started: {filename} 📹'})
    return jsonify({'error': 'Mock ScarePi not initialized'}), 500

@app.route('/api/config', methods=['GET', 'POST'])
def config():
    """Get or update configuration."""
    if request.method == 'GET':
        config_file = 'config.json'
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                return jsonify(json.load(f))
        return jsonify({})
    
    elif request.method == 'POST':
        config_data = request.json
        with open('config.json', 'w') as f:
            json.dump(config_data, f, indent=2)
        return jsonify({'message': 'Configuration updated! ⚙️'})

if __name__ == '__main__':
    print("🎃 Starting ScarePi Web UI (Mock Mode)...")
    print("🌙 Initializing spooky systems for local testing...")
    print("💻 Running in mock mode - no hardware required!")
    
    if init_scarepi():
        print("✅ Mock ScarePi initialized successfully!")
        print("🌐 Starting web server...")
        print("🔗 Open your browser to: http://localhost:5001")
        print("🎮 All buttons will work - they just simulate hardware!")
        app.run(host='127.0.0.1', port=5001, debug=True)
    else:
        print("❌ Failed to initialize mock ScarePi.")
