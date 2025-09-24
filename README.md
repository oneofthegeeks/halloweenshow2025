# 🎃 ScarePi Enhanced - Digital Haunted House + Marketing Platform 🦇

A comprehensive Raspberry Pi project that creates an automated haunted house experience with motion detection, prop control, sound effects, video recording, AND a complete marketing platform for building your Halloween audience and growing your following!

## 🌙 Core Features

- **Motion Detection**: Automatically triggers scares when motion is detected
- **Web Control Panel**: Beautiful Halloween-themed web interface
- **Manual Controls**: Individual control of props, sounds, and recording
- **Video Recording**: Captures scares with the Pi Camera
- **Sound Effects**: Plays scary audio files
- **Prop Control**: Controls Halloween props via relay
- **Real-time Status**: Live system monitoring

## 🚀 Marketing & Audience Engagement Features

- **📱 QR Code System**: Generate QR codes for easy audience access
- **👥 Audience Data Collection**: Comprehensive form to build your email list
- **📊 Analytics Dashboard**: Real-time show statistics and audience insights
- **📺 YouTube Integration**: Grow your channel with subscriber opt-ins
- **📱 Social Media Sharing**: Viral content creation and cross-platform growth
- **📈 Show Analytics**: Track performance and optimize your haunted house
- **📧 Email List Building**: Direct communication with your audience
- **🎬 Show Management**: Start/stop shows with live monitoring

## 🛠️ Hardware Requirements

### Required Components
- Raspberry Pi 4 (recommended) or Pi 3B+
- PIR Motion Sensor (HC-SR501)
- Relay Module (5V)
- Halloween props (pumpkins, animatronics, etc.)
- Pi Camera Module
- Speaker or audio output
- Jumper wires
- Breadboard (optional)

### Optional Enhancements
- Multiple motion sensors
- LED strips for lighting effects
- Fog machine control
- Multiple audio outputs
- External storage for recordings

## 📋 Software Requirements

- Raspberry Pi OS (latest)
- Python 3.8+
- Internet connection (for initial setup)

## 🚀 Installation Guide

### Step 1: Update Your Raspberry Pi

```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Required Packages

```bash
# Install Python dependencies
sudo apt install python3-pip python3-venv python3-dev -y

# Install audio dependencies
sudo apt install libasound2-dev portaudio19-dev -y

# Install camera dependencies
sudo apt install python3-picamera -y
```

### Step 3: Clone and Setup Project

```bash
# Clone the repository
git clone <your-repo-url>
cd halloweenshow2025

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

### Step 4: Hardware Connections

#### Motion Sensor (PIR)
- VCC → 5V (Pin 2)
- GND → Ground (Pin 6)
- OUT → GPIO 19 (Pin 35)

#### Relay Module
- VCC → 5V (Pin 2)
- GND → Ground (Pin 6)
- IN → GPIO 26 (Pin 37)

#### Pi Camera
- Connect to the camera port on the Pi

### Step 5: Audio Setup

1. Add your scary sound files to the project directory
2. Supported formats: OGG, WAV, MP3
3. Recommended: Convert to OGG for best compatibility

```bash
# Example: Convert MP3 to OGG using ffmpeg
sudo apt install ffmpeg -y
ffmpeg -i scary_sound.mp3 scary_sound.ogg
```

### Step 6: Configure System

1. Enable camera interface:
```bash
sudo raspi-config
# Navigate to Interface Options → Camera → Enable
```

2. Enable GPIO access:
```bash
sudo usermod -a -G gpio pi
```

3. Set up audio output:
```bash
# Test audio
speaker-test -t wav -c 2
```

## 🎮 Usage

### Starting the Web Interface

```bash
# Activate virtual environment
source venv/bin/activate

# Start the web server
python app.py
```

Open your browser and navigate to: `http://your-pi-ip:5000`

### Enhanced Web Interface Features

#### 🎃 Main Control Panel
- **Motion Detection Toggle**: Enable/disable automatic motion detection
- **Full Scare Sequence**: Trigger all effects at once
- **Individual Controls**: 
  - ⚡ Trigger Prop
  - 🔊 Play Sound
  - 📹 Start Recording

#### 📱 Marketing & Audience Engagement
- **QR Code Generator**: Create QR codes for easy audience access
- **Audience Form**: Comprehensive data collection form
- **Analytics Dashboard**: Real-time show statistics and insights
- **Show Management**: Start/stop shows with live monitoring
- **Social Media Integration**: YouTube and social sharing features

#### 📊 System Status
- Real-time system monitoring
- Motion sensor status
- Show status and duration
- Audience statistics
- Connection status
- Last update timestamp

### Command Line Usage

#### Test Motion Sensor
```bash
python motion_test.py
```

#### Test Audio
```bash
python scare_audio.py
```

#### Run Full System (Legacy)
```bash
python scarepi.py
```

## 🔧 Configuration

### Customizing Pin Assignments

Edit `app.py` to change GPIO pins:

```python
# In app.py, modify the ScarePi initialization
scarepi = ScarePi(motion_pin=35, relay_pin=37)
```

### Adding Custom Sound Effects

1. Place your audio files in the project directory
2. Supported formats: OGG, WAV, MP3
3. Update the sound file name in the code if needed

### Camera Settings

Modify camera settings in `scarepi.py`:

```python
# Camera configuration
self.camera.resolution = (1920, 1080)  # Change resolution
self.camera.framerate = 30             # Change framerate
```

## 🎨 Customization

### Web Interface Theming

- Edit `static/style.css` for visual customization
- Modify `templates/index.html` for layout changes
- Update `static/script.js` for functionality changes

### Halloween Props

Connect various Halloween props to the relay:
- Animatronic figures
- LED strips
- Fog machines
- Sound-activated props
- Motorized decorations

## 🐛 Troubleshooting

### Common Issues

#### Motion Sensor Not Working
```bash
# Check GPIO permissions
sudo usermod -a -G gpio pi
# Reboot the Pi
sudo reboot
```

#### Audio Not Playing
```bash
# Check audio output
aplay /usr/share/sounds/alsa/Front_Left.wav
# Install additional audio codecs
sudo apt install gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly
```

#### Camera Not Working
```bash
# Enable camera interface
sudo raspi-config
# Test camera
raspistill -o test.jpg
```

#### Web Interface Not Loading
```bash
# Check if Flask is running
ps aux | grep python
# Check port availability
netstat -tlnp | grep 5000
```

### GPIO Troubleshooting

```bash
# Test GPIO access
python3 -c "import RPi.GPIO as GPIO; print('GPIO access OK')"
```

## 📁 Project Structure

```
halloweenshow2025/
├── app.py                 # Main Flask web application (Raspberry Pi)
├── app_enhanced.py        # Enhanced Flask app with marketing features
├── app_mock.py           # Mock version for local testing
├── scarepi.py            # Core ScarePi class
├── motion_test.py        # Motion sensor testing
├── scare_audio.py        # Audio testing
├── requirements.txt      # Python dependencies (Raspberry Pi)
├── requirements_local.txt # Dependencies for local testing
├── README.md             # This file
├── QUICKSTART.md         # Quick start guide
├── MARKETING_GUIDE.md    # Complete marketing strategy guide
├── install.sh            # Automated installation script
├── setup_local.sh        # Local testing setup
├── start_local.sh        # Local testing startup script
├── templates/
│   ├── index.html        # Basic web interface template
│   ├── enhanced_index.html # Enhanced control panel
│   ├── audience_form.html # Audience data collection form
│   ├── analytics.html    # Analytics dashboard
│   └── qr_display.html   # QR code display page
├── static/
│   ├── style.css         # Basic Halloween-themed CSS
│   ├── enhanced_style.css # Enhanced CSS with marketing features
│   ├── script.js         # Basic web interface JavaScript
│   └── enhanced_script.js # Enhanced JavaScript with marketing features
├── config.json           # Configuration file (auto-generated)
├── scarepi_audience.db   # SQLite database for audience data
└── scary_sound_placeholder.txt # Audio file instructions
```

## 🎃 Halloween Setup Ideas

### Basic Haunted House
- Place motion sensor at entrance
- Connect animatronic prop to relay
- Add scary sound effects
- Position camera for recording

### Advanced Setup
- Multiple motion sensors for different zones
- Synchronized lighting effects
- Multiple audio outputs
- Fog machine integration
- Remote monitoring via web interface

### Marketing & Audience Growth
- **QR Code Displays**: Place QR codes at entrance and key locations
- **Social Media Integration**: Share your show and grow your following
- **Audience Data Collection**: Build your email list and YouTube subscribers
- **Analytics Tracking**: Monitor show performance and audience engagement
- **Content Creation**: Use the system to create viral Halloween content

## 📱 Enhanced Marketing Features

### QR Code System
- Generate QR codes for easy audience access
- Print-ready QR codes for physical displays
- Direct link sharing to audience form
- Social media integration for viral sharing

### Audience Data Collection
- Comprehensive form with interests and preferences
- Social media integration for cross-platform growth
- YouTube subscription opt-in for channel growth
- Email list building for direct communication
- Analytics tracking for audience insights

### Analytics Dashboard
- Real-time show statistics and audience metrics
- Engagement tracking and conversion rates
- Data export for marketing analysis
- Performance insights for show optimization

### Social Media Integration
- YouTube channel promotion and subscriber growth
- Social sharing buttons for viral content
- Cross-platform engagement tools
- Content creation for building your following

## 📚 Marketing Guide

For a complete marketing strategy and audience growth guide, see `MARKETING_GUIDE.md` which includes:
- QR code marketing tactics
- Audience data collection strategies
- Social media growth techniques
- Content creation ideas
- Analytics and optimization tips

## 🤝 Contributing

Feel free to contribute to this spooky project! Some ideas:
- Additional Halloween themes
- More prop integrations
- Mobile app companion
- Voice control features
- Advanced lighting effects

## 📄 License

This project is based on Network Chuck's tutorial and is open source. Feel free to modify and share!

## 🙏 Credits

- **Network Chuck**: Original tutorial inspiration
- **Raspberry Pi Foundation**: Hardware platform
- **Python Community**: Amazing libraries and tools
- **Halloween Spirit**: For making everything spooky! 👻

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section
2. Verify all connections
3. Test individual components
4. Check system logs: `journalctl -f`

---

**Happy Haunting! 🎃👻🦇**

*Built with spooky Python magic and Halloween spirit!*
