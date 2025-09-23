# 🚀 ScarePi Quick Start Guide 🎃

Get your haunted house running in minutes!

## ⚡ Super Quick Setup

### 1. Run the Installer
```bash
chmod +x install.sh
./install.sh
```

### 2. Reboot Your Pi
```bash
sudo reboot
```

### 3. Connect Hardware
- **Motion Sensor**: VCC→5V, GND→Ground, OUT→GPIO19 (Pin 35)
- **Relay**: VCC→5V, GND→Ground, IN→GPIO26 (Pin 37)
- **Camera**: Connect to camera port
- **Speaker**: Connect to audio jack

### 4. Add Scary Sounds
```bash
# Convert your scary audio to OGG format
ffmpeg -i your_scary_sound.mp3 scary_sound.ogg
```

### 5. Start ScarePi
```bash
cd halloweenshow2025
./start_scarepi.sh
```

### 6. Open Web Interface
Open your browser to: `http://localhost:5000`

## 🎮 Basic Usage

1. **Enable Motion Detection**: Click the motion toggle button
2. **Test Manual Controls**: Try the individual buttons
3. **Trigger Full Scare**: Use the big red button for everything at once

## 🔧 Quick Troubleshooting

### No Audio?
```bash
# Test audio
speaker-test -t wav -c 2
```

### Motion Sensor Not Working?
```bash
# Test motion sensor
python motion_test.py
```

### Web Interface Not Loading?
```bash
# Check if running
ps aux | grep python
# Check port
netstat -tlnp | grep 5000
```

## 🎃 Halloween Setup Tips

- Place motion sensor at entrance
- Connect animatronic prop to relay
- Position camera for best scare angle
- Test everything before Halloween night!

## 📚 Full Documentation

For detailed setup, customization, and troubleshooting, see `README.md`.

---

**Happy Haunting! 👻🦇🎃**
