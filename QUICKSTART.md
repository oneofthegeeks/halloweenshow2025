# 🚀 ScarePi Enhanced Quick Start Guide 🎃

Get your haunted house AND marketing platform running in minutes!

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

### 5. Start Enhanced ScarePi
```bash
cd halloweenshow2025
python app_enhanced.py
```

### 6. Access Your Marketing Platform
- **Main Control Panel**: `http://localhost:5001`
- **Audience Form**: `http://localhost:5001/audience`
- **QR Code Generator**: `http://localhost:5001/qr`
- **Analytics Dashboard**: `http://localhost:5001/analytics`

## 🎮 Basic Usage

1. **Enable Motion Detection**: Click the motion toggle button
2. **Test Manual Controls**: Try the individual buttons
3. **Trigger Full Scare**: Use the big red button for everything at once

## 📱 Marketing Features

1. **Generate QR Code**: Click "Generate QR Code" button
2. **Collect Audience Data**: Share the audience form link
3. **Track Analytics**: Monitor show performance and audience growth
4. **Start/Stop Shows**: Use show management controls
5. **Social Media**: Share your show and grow your following

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
