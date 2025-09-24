#!/bin/bash
# 🎃 ScarePi Docker Build Script 🦇
# Build and deploy your Halloween marketing platform

set -e

echo "🎃 Building ScarePi Enhanced Docker Container..."
echo "🐳 Marketing Platform + Haunted House Control System"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${PURPLE}$1${NC}"
}

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is available
if ! command -v docker-compose &> /dev/null; then
    print_warning "Docker Compose not found. Using docker build instead."
    USE_COMPOSE=false
else
    USE_COMPOSE=true
fi

print_header "🎃 ScarePi Enhanced Docker Build"
print_status "Building marketing platform container..."

# Create data directory if it doesn't exist
mkdir -p data

# Build the Docker image
print_status "Building Docker image..."
if [ "$USE_COMPOSE" = true ]; then
    print_status "Using Docker Compose..."
    docker-compose build
    print_success "Docker Compose build completed!"
else
    print_status "Using Docker build..."
    docker build -t scarepi-enhanced .
    print_success "Docker build completed!"
fi

print_header "🚀 Deployment Options"
echo ""
echo "1. Run with Docker Compose (recommended):"
echo "   docker-compose up -d"
echo ""
echo "2. Run with Docker directly:"
echo "   docker run -d --name scarepi-enhanced -p 5001:5001 -v \$(pwd)/data:/app/data scarepi-enhanced"
echo ""
echo "3. Access your marketing platform:"
echo "   🌐 Main Control Panel: http://localhost:5001"
echo "   📱 Audience Form: http://localhost:5001/audience"
echo "   📊 QR Code Generator: http://localhost:5001/qr"
echo "   📈 Analytics Dashboard: http://localhost:5001/analytics"
echo ""

print_header "🎯 Quick Start Commands"
echo ""
echo "Start the container:"
if [ "$USE_COMPOSE" = true ]; then
    echo "   docker-compose up -d"
else
    echo "   docker run -d --name scarepi-enhanced -p 5001:5001 -v \$(pwd)/data:/app/data scarepi-enhanced"
fi
echo ""
echo "View logs:"
echo "   docker logs scarepi-enhanced"
echo ""
echo "Stop the container:"
if [ "$USE_COMPOSE" = true ]; then
    echo "   docker-compose down"
else
    echo "   docker stop scarepi-enhanced && docker rm scarepi-enhanced"
fi
echo ""

print_header "🏠 Unraid Setup"
echo ""
echo "For Unraid deployment:"
echo "1. Copy the built image to your Unraid server"
echo "2. Create a new Docker container"
echo "3. Set port mapping: 5001:5001"
echo "4. Mount data volume: /mnt/user/appdata/scarepi/data"
echo "5. Start the container"
echo ""

print_success "🎃 ScarePi Enhanced Docker build completed!"
print_success "🐳 Your Halloween marketing platform is ready!"
print_success "👻 Ready to scare and grow your following!"
print_success "📱 Marketing features: QR codes, analytics, audience engagement!"
print_success "🎬 Show management: Start/stop shows, real-time monitoring!"
print_success "📊 Data collection: Build your email list and YouTube subscribers!"

echo ""
print_header "🎯 Next Steps:"
echo "1. Start your container"
echo "2. Open http://localhost:5001"
echo "3. Generate QR codes for your show"
echo "4. Collect audience data"
echo "5. Track analytics and grow your following!"
echo ""
print_success "Happy Halloween! 🎃👻🦇✨"
