# 🎃 ScarePi - Digital Haunted House Control System 🦇

A spooky Raspberry Pi project that creates an automated haunted house experience with motion detection, prop control, sound effects, and video recording. Based on Network Chuck's tutorial with added web UI and Halloween theming!

## 🌙 Features

- **Motion Detection**: Automatically triggers scares when motion is detected
- **Web Control Panel**: Beautiful Halloween-themed web interface
- **Manual Controls**: Individual control of props, sounds, and recording
- **Video Recording**: Captures scares with the Pi Camera
- **Sound Effects**: Plays scary audio files
- **Prop Control**: Controls Halloween props via relay
- **Real-time Status**: Live system monitoring

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

### Web Interface Features

#### 🎃 Main Control Panel
- **Motion Detection Toggle**: Enable/disable automatic motion detection
- **Full Scare Sequence**: Trigger all effects at once
- **Individual Controls**: 
  - ⚡ Trigger Prop
  - 🔊 Play Sound
  - 📹 Start Recording

#### 📊 System Status
- Real-time system monitoring
- Motion sensor status
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
├── app.py                 # Main Flask web application
├── scarepi.py            # Core ScarePi class
├── motion_test.py        # Motion sensor testing
├── scare_audio.py        # Audio testing
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── templates/
│   └── index.html       # Web interface template
├── static/
│   ├── style.css        # Halloween-themed CSS
│   └── script.js        # Web interface JavaScript
└── config.json          # Configuration file (auto-generated)
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
