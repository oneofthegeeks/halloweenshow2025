#!/usr/bin/env python3
"""
ScarePi Web UI - Halloween-themed control interface
A spooky web interface for controlling your Raspberry Pi haunted house!
"""

from flask import Flask, render_template, jsonify, request
import threading
import time
import json
import os
from datetime import datetime
from scarepi import ScarePi

app = Flask(__name__)

# Global ScarePi instance
scarepi = None
motion_enabled = False
motion_thread = None

def init_scarepi():
    """Initialize the ScarePi system."""
    global scarepi
    try:
        scarepi = ScarePi(motion_pin=35, relay_pin=37)
        return True
    except Exception as e:
        print(f"Failed to initialize ScarePi: {e}")
        return False

def motion_detection_loop():
    """Background thread for motion detection."""
    global motion_enabled, scarepi
    print("Motion detection thread started...")
    
    while motion_enabled and scarepi:
        try:
            motion_detected = scarepi.motion_detected()
            if motion_detected:
                print("MOTION DETECTED! BOO!")
                # Trigger full scare sequence
                trigger_full_scare()
                time.sleep(5)  # Cooldown period
            time.sleep(0.1)
        except Exception as e:
            print(f"Motion detection error: {e}")
            break

def trigger_full_scare():
    """Trigger the complete scare sequence."""
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
        return jsonify({'status': 'enabled', 'message': 'Motion detection activated! 👻'})
    else:
        return jsonify({'status': 'disabled', 'message': 'Motion detection deactivated 🛑'})

@app.route('/api/scare/full', methods=['POST'])
def trigger_full_scare_api():
    """Manually trigger full scare sequence."""
    if scarepi:
        threading.Thread(target=trigger_full_scare, daemon=True).start()
        return jsonify({'message': 'Full scare sequence triggered! 🎃💀'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

@app.route('/api/scare/prop', methods=['POST'])
def trigger_prop():
    """Manually trigger prop only."""
    if scarepi:
        threading.Thread(target=scarepi.trigger_prop, daemon=True).start()
        return jsonify({'message': 'Prop triggered! 🦇'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

@app.route('/api/scare/sound', methods=['POST'])
def trigger_sound():
    """Manually trigger sound only."""
    if scarepi:
        threading.Thread(target=scarepi.play_scary_sound, daemon=True).start()
        return jsonify({'message': 'Scary sound playing! 🔊👻'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

@app.route('/api/scare/record', methods=['POST'])
def trigger_record():
    """Manually start recording."""
    if scarepi:
        filename = scarepi.record_scare()
        return jsonify({'message': f'Recording started: {filename} 📹'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

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
    print("🎃 Starting ScarePi Web UI...")
    print("🌙 Initializing spooky systems...")
    
    if init_scarepi():
        print("✅ ScarePi initialized successfully!")
        print("🌐 Starting web server...")
        print("🔗 Open your browser to: http://localhost:5000")
        app.run(host='0.0.0.0', port=5000, debug=False)
    else:
        print("❌ Failed to initialize ScarePi. Check your hardware connections!")
        print("💡 Make sure you're running this on a Raspberry Pi with proper GPIO setup.")
