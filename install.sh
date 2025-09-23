#!/bin/bash
# 🎃 ScarePi Installation Script 🦇
# Automated setup for Raspberry Pi haunted house project

echo "🎃 Welcome to ScarePi Installation! 🦇"
echo "🌙 Setting up your digital haunted house..."
echo ""

# Check if running on Raspberry Pi
if ! grep -q "Raspberry Pi" /proc/cpuinfo 2>/dev/null; then
    echo "⚠️  Warning: This script is designed for Raspberry Pi"
    echo "   Proceeding anyway, but some features may not work..."
    echo ""
fi

# Update system
echo "📦 Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install required packages
echo "🔧 Installing required packages..."
sudo apt install -y python3-pip python3-venv python3-dev libasound2-dev portaudio19-dev python3-picamera ffmpeg

# Create virtual environment
echo "🐍 Setting up Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Enable camera interface
echo "📷 Enabling camera interface..."
sudo raspi-config nonint do_camera 0

# Add user to gpio group
echo "⚡ Setting up GPIO permissions..."
sudo usermod -a -G gpio $USER

# Create startup script
echo "🚀 Creating startup script..."
cat > start_scarepi.sh << 'EOF'
#!/bin/bash
cd /home/pi/halloweenshow2025
source venv/bin/activate
python app.py
EOF

chmod +x start_scarepi.sh

# Create systemd service (optional)
echo "🔧 Creating systemd service..."
sudo tee /etc/systemd/system/scarepi.service > /dev/null << EOF
[Unit]
Description=ScarePi Halloween Control System
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/halloweenshow2025
ExecStart=/home/pi/halloweenshow2025/venv/bin/python app.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

# Enable service (optional)
echo "🎯 Enabling ScarePi service..."
sudo systemctl daemon-reload
sudo systemctl enable scarepi.service

# Create desktop shortcut
echo "🖥️ Creating desktop shortcut..."
cat > ~/Desktop/ScarePi.desktop << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=ScarePi Control Panel
Comment=Halloween Haunted House Control System
Exec=firefox http://localhost:5000
Icon=applications-games
Terminal=false
Categories=Game;Entertainment;
EOF

chmod +x ~/Desktop/ScarePi.desktop

# Test audio
echo "🔊 Testing audio system..."
if command -v speaker-test >/dev/null 2>&1; then
    echo "   Running audio test (will stop automatically)..."
    timeout 3s speaker-test -t wav -c 2 >/dev/null 2>&1 || true
fi

# Final instructions
echo ""
echo "🎉 Installation Complete! 🎉"
echo ""
echo "📋 Next Steps:"
echo "1. Reboot your Raspberry Pi: sudo reboot"
echo "2. Connect your hardware (motion sensor, relay, camera)"
echo "3. Add your scary sound files to the project directory"
echo "4. Start ScarePi: ./start_scarepi.sh"
echo "5. Open your browser to: http://localhost:5000"
echo ""
echo "🎃 Happy Haunting! 🦇"
echo ""
echo "💡 For detailed setup instructions, see README.md"
echo "🆘 For troubleshooting, check the README.md file"
