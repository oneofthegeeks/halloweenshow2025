#!/bin/bash
# 🎃 ScarePi Local Setup Script 🦇
# Setup for testing on Mac/Windows without Raspberry Pi

echo "🎃 Welcome to ScarePi Local Testing! 🦇"
echo "💻 Setting up for local development..."
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "   Please install Python 3 from https://python.org"
    exit 1
fi

# Create virtual environment
echo "🐍 Setting up Python virtual environment..."
python3 -m venv venv_local

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv_local/bin/activate

# Install Python dependencies
echo "📚 Installing Python dependencies for local testing..."
pip install --upgrade pip
pip install -r requirements_local.txt

# Create startup script for local testing
echo "🚀 Creating local startup script..."
cat > start_local.sh << 'EOF'
#!/bin/bash
cd /Users/taylorbrinton/Nextcloud/halloweenshow2025
source venv_local/bin/activate
python app_mock.py
EOF

chmod +x start_local.sh

# Final instructions
echo ""
echo "🎉 Local Setup Complete! 🎉"
echo ""
echo "📋 To start testing:"
echo "1. Run: ./start_local.sh"
echo "2. Open your browser to: http://localhost:5000"
echo "3. Test all the buttons and features!"
echo ""
echo "🎃 Happy Local Testing! 🦇"
echo ""
echo "💡 This is a mock version - no real hardware required!"
echo "🆘 All buttons work but simulate hardware responses"
