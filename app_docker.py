#!/usr/bin/env python3
"""
ScarePi Enhanced Docker Version - Marketing Platform
Optimized for Docker containers and Unraid deployment
"""

from flask import Flask, render_template, jsonify, request, redirect, url_for, send_file
import threading
import time
import json
import os
import qrcode
import io
import base64
from datetime import datetime, timedelta
import sqlite3
import hashlib
import secrets

app = Flask(__name__)

# Docker-optimized ScarePi with marketing features
class DockerScarePi:
    def __init__(self):
        """Initialize Docker-optimized ScarePi."""
        self.running = True
        self.show_stats = {
            'total_scares': 0,
            'audience_count': 0,
            'show_start_time': None,
            'last_scare_time': None
        }
        
        # Initialize database
        self.init_database()
        
        print("🎃 Docker ScarePi initialized with marketing features!")
        print("📊 Analytics and audience engagement ready!")
        print("🌙 Ready to spook and grow your following!")
        print("🐳 Running in Docker container mode!")
    
    def init_database(self):
        """Initialize SQLite database for audience data."""
        conn = sqlite3.connect('/app/data/scarepi_audience.db')
        cursor = conn.cursor()
        
        # Create audience table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audience (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT,
                social_media TEXT,
                how_heard TEXT,
                interests TEXT,
                subscribe_youtube BOOLEAN DEFAULT 0,
                subscribe_updates BOOLEAN DEFAULT 1,
                join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ip_address TEXT,
                user_agent TEXT
            )
        ''')
        
        # Create show analytics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS show_analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                details TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def motion_detected(self):
        """Mock motion detection for Docker demo."""
        import random
        return random.choice([True, False, False, False, False])  # 20% chance
    
    def trigger_prop(self, duration=2.0):
        """Mock prop trigger for Docker demo."""
        print("🦇 BOO! Docker prop triggered!")
        self.log_analytics('prop_triggered', f'Duration: {duration}s')
        time.sleep(duration)
        print("⚡ Docker prop finished!")
    
    def play_scary_sound(self, sound_file="scary_sound.ogg"):
        """Mock sound playing for Docker demo."""
        print(f"🔊 Docker playing scary sound: {sound_file}")
        self.log_analytics('sound_played', f'Sound: {sound_file}')
        time.sleep(1)
    
    def record_scare(self, filename=None):
        """Mock video recording for Docker demo."""
        if filename is None:
            current = datetime.now()
            filename = f"docker_scare_{current.strftime('%Y%m%d_%H%M%S')}.h264"
        
        print(f"📹 Docker recording scare: {filename}")
        self.log_analytics('recording_started', f'File: {filename}')
        time.sleep(2)
        print(f"🎬 Docker scare recorded: {filename}")
        return filename
    
    def log_analytics(self, event_type, details=""):
        """Log show analytics to database."""
        conn = sqlite3.connect('/app/data/scarepi_audience.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO show_analytics (event_type, details)
            VALUES (?, ?)
        ''', (event_type, details))
        conn.commit()
        conn.close()
        
        # Update show stats
        if event_type == 'scare_sequence':
            self.show_stats['total_scares'] += 1
            self.show_stats['last_scare_time'] = datetime.now()
    
    def add_audience_member(self, data):
        """Add new audience member to database."""
        conn = sqlite3.connect('/app/data/scarepi_audience.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO audience (name, email, phone, social_media, how_heard, 
                                    interests, subscribe_youtube, subscribe_updates, 
                                    ip_address, user_agent)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                data.get('name'),
                data.get('email'),
                data.get('phone', ''),
                data.get('social_media', ''),
                data.get('how_heard', ''),
                data.get('interests', ''),
                data.get('subscribe_youtube', False),
                data.get('subscribe_updates', True),
                data.get('ip_address', ''),
                data.get('user_agent', '')
            ))
            conn.commit()
            self.show_stats['audience_count'] += 1
            self.log_analytics('audience_joined', f'Email: {data.get("email")}')
            return True
        except sqlite3.IntegrityError:
            return False  # Email already exists
        finally:
            conn.close()
    
    def get_audience_stats(self):
        """Get audience statistics."""
        conn = sqlite3.connect('/app/data/scarepi_audience.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM audience')
        total_audience = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM audience WHERE subscribe_youtube = 1')
        youtube_subscribers = cursor.fetchone()[0]
        
        cursor.execute('SELECT COUNT(*) FROM show_analytics WHERE event_type = "scare_sequence"')
        total_scares = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'total_audience': total_audience,
            'youtube_subscribers': youtube_subscribers,
            'total_scares': total_scares,
            'show_duration': self.get_show_duration()
        }
    
    def get_show_duration(self):
        """Get current show duration."""
        if self.show_stats['show_start_time']:
            return str(datetime.now() - self.show_stats['show_start_time']).split('.')[0]
        return "0:00:00"

# Global Docker ScarePi instance
scarepi = None
motion_enabled = False
motion_thread = None
show_active = False

def init_scarepi():
    """Initialize the Docker ScarePi system."""
    global scarepi
    try:
        scarepi = DockerScarePi()
        return True
    except Exception as e:
        print(f"Failed to initialize Docker ScarePi: {e}")
        return False

def motion_detection_loop():
    """Background thread for motion detection."""
    global motion_enabled, scarepi
    print("Docker motion detection thread started...")
    
    while motion_enabled and scarepi:
        try:
            motion_detected = scarepi.motion_detected()
            if motion_detected:
                print("DOCKER MOTION DETECTED! BOO!")
                trigger_full_scare()
                time.sleep(5)  # Cooldown period
            time.sleep(0.1)
        except Exception as e:
            print(f"Docker motion detection error: {e}")
            break

def trigger_full_scare():
    """Trigger the complete Docker scare sequence."""
    if scarepi:
        scarepi.record_scare()
        scarepi.trigger_prop()
        scarepi.play_scary_sound()
        scarepi.log_analytics('scare_sequence', 'Full scare sequence triggered')

def generate_qr_code(data, size=200):
    """Generate QR code for show access."""
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="orange", back_color="black")
    
    # Convert to base64 for web display
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    return base64.b64encode(buffer.getvalue()).decode()

# Routes
@app.route('/')
def index():
    """Main enhanced Halloween control panel."""
    return render_template('enhanced_index.html')

@app.route('/audience')
def audience_form():
    """Audience engagement form."""
    return render_template('audience_form.html')

@app.route('/analytics')
def analytics_dashboard():
    """Analytics dashboard."""
    if scarepi:
        stats = scarepi.get_audience_stats()
        return render_template('analytics.html', stats=stats)
    return redirect(url_for('index'))

@app.route('/qr')
def qr_code():
    """Generate QR code for show access."""
    # Get the current server URL
    base_url = request.url_root.rstrip('/')
    qr_data = f"{base_url}/audience"
    
    qr_code_b64 = generate_qr_code(qr_data)
    return render_template('qr_display.html', qr_code=qr_code_b64, qr_data=qr_data)

@app.route('/api/status')
def get_status():
    """Get current system status."""
    return jsonify({
        'motion_enabled': motion_enabled,
        'scarepi_initialized': scarepi is not None,
        'show_active': show_active,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/audience/stats')
def get_audience_stats():
    """Get audience statistics."""
    if scarepi:
        return jsonify(scarepi.get_audience_stats())
    return jsonify({'error': 'ScarePi not initialized'}), 500

@app.route('/api/audience/join', methods=['POST'])
def join_audience():
    """Add new audience member."""
    if not scarepi:
        return jsonify({'error': 'ScarePi not initialized'}), 500
    
    data = request.json
    data['ip_address'] = request.remote_addr
    data['user_agent'] = request.headers.get('User-Agent', '')
    
    success = scarepi.add_audience_member(data)
    
    if success:
        return jsonify({
            'message': 'Welcome to the show! 🎃👻',
            'success': True
        })
    else:
        return jsonify({
            'message': 'Email already registered! 👻',
            'success': False
        })

@app.route('/api/show/start', methods=['POST'])
def start_show():
    """Start the Halloween show."""
    global show_active
    if scarepi:
        show_active = True
        scarepi.show_stats['show_start_time'] = datetime.now()
        scarepi.log_analytics('show_started', 'Halloween show began')
        return jsonify({'message': '🎃 Halloween show started! 👻'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

@app.route('/api/show/stop', methods=['POST'])
def stop_show():
    """Stop the Halloween show."""
    global show_active, motion_enabled
    if scarepi:
        show_active = False
        motion_enabled = False
        scarepi.log_analytics('show_stopped', 'Halloween show ended')
        return jsonify({'message': '🛑 Halloween show stopped! 🎃'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

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
        return jsonify({'message': 'Full Docker scare sequence triggered! 🎃💀'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

@app.route('/api/scare/prop', methods=['POST'])
def trigger_prop():
    """Manually trigger prop only."""
    if scarepi:
        threading.Thread(target=scarepi.trigger_prop, daemon=True).start()
        return jsonify({'message': 'Docker prop triggered! 🦇'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

@app.route('/api/scare/sound', methods=['POST'])
def trigger_sound():
    """Manually trigger sound only."""
    if scarepi:
        threading.Thread(target=scarepi.play_scary_sound, daemon=True).start()
        return jsonify({'message': 'Docker scary sound playing! 🔊👻'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

@app.route('/api/scare/record', methods=['POST'])
def trigger_record():
    """Manually start recording."""
    if scarepi:
        filename = scarepi.record_scare()
        return jsonify({'message': f'Docker recording started: {filename} 📹'})
    return jsonify({'error': 'ScarePi not initialized'}), 500

if __name__ == '__main__':
    print("🎃 Starting Docker ScarePi Enhanced...")
    print("🌙 Initializing spooky systems for Docker...")
    print("📊 Analytics, audience engagement, and QR codes ready!")
    print("🐳 Running in Docker container mode!")
    
    if init_scarepi():
        print("✅ Docker ScarePi initialized successfully!")
        print("🌐 Starting enhanced web server...")
        print("🔗 Open your browser to: http://localhost:5001")
        print("📱 QR Code available at: http://localhost:5001/qr")
        print("👥 Audience form at: http://localhost:5001/audience")
        print("📊 Analytics at: http://localhost:5001/analytics")
        app.run(host='0.0.0.0', port=5001, debug=False)
    else:
        print("❌ Failed to initialize Docker ScarePi.")
