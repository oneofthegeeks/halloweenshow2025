#!/bin/bash
# 🐳 ScarePi Docker Hub Push Script 🎃
# Push your Halloween marketing platform to Docker Hub

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

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

print_header "🐳 ScarePi Docker Hub Deployment"
print_status "Building and pushing your Halloween marketing platform..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    print_error "Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if user is logged into Docker Hub
if ! docker info | grep -q "Username"; then
    print_warning "You need to login to Docker Hub first."
    print_status "Run: docker login"
    print_status "Enter your Docker Hub username and password"
    exit 1
fi

# Get Docker Hub username
print_status "Enter your Docker Hub username:"
read DOCKER_USERNAME

if [ -z "$DOCKER_USERNAME" ]; then
    print_error "Docker Hub username is required."
    exit 1
fi

# Set image name
IMAGE_NAME="scarepi-enhanced"
FULL_IMAGE_NAME="${DOCKER_USERNAME}/${IMAGE_NAME}"

print_status "Building Docker image: ${FULL_IMAGE_NAME}"

# Build the image
docker build -t ${FULL_IMAGE_NAME}:latest .
docker build -t ${FULL_IMAGE_NAME}:v1.0.0 .

print_success "Docker image built successfully!"

# Push to Docker Hub
print_status "Pushing to Docker Hub..."

# Push latest tag
print_status "Pushing latest tag..."
docker push ${FULL_IMAGE_NAME}:latest

# Push version tag
print_status "Pushing v1.0.0 tag..."
docker push ${FULL_IMAGE_NAME}:v1.0.0

print_success "Successfully pushed to Docker Hub!"

print_header "🎯 Unraid Deployment Instructions"
echo ""
echo "Now you can deploy in Unraid using:"
echo "Repository: ${FULL_IMAGE_NAME}:latest"
echo ""
echo "Or use the specific version:"
echo "Repository: ${FULL_IMAGE_NAME}:v1.0.0"
echo ""

print_header "🏠 Unraid Docker GUI Setup"
echo ""
echo "1. Go to Docker tab in Unraid"
echo "2. Click Add Container"
echo "3. Configure as follows:"
echo ""
echo "Basic Settings:"
echo "- Name: scarepi-enhanced"
echo "- Repository: ${FULL_IMAGE_NAME}:latest"
echo "- Network Type: Bridge"
echo ""
echo "Port Settings:"
echo "- Container Port: 5001"
echo "- Host Port: 5001"
echo ""
echo "Path Settings:"
echo "- Container Path: /app/data"
echo "- Host Path: /mnt/user/appdata/scarepi/data"
echo ""
echo "Environment Variables:"
echo "- FLASK_ENV=production"
echo "- PYTHONUNBUFFERED=1"
echo ""

print_header "🌐 Access Your Platform"
echo ""
echo "Once deployed, access your Halloween marketing platform at:"
echo "- Main Control Panel: http://your-unraid-ip:5001"
echo "- Audience Form: http://your-unraid-ip:5001/audience"
echo "- QR Code Generator: http://your-unraid-ip:5001/qr"
echo "- Analytics Dashboard: http://your-unraid-ip:5001/analytics"
echo ""

print_success "🎃 ScarePi Enhanced is ready for Docker Hub deployment!"
print_success "🐳 Your Halloween marketing platform is now available on Docker Hub!"
print_success "👻 Ready to scare and grow your following!"
print_success "📱 Marketing features: QR codes, analytics, audience engagement!"
print_success "🎬 Show management: Start/stop shows, real-time monitoring!"
print_success "📊 Data collection: Build your email list and YouTube subscribers!"

echo ""
print_header "🎯 Next Steps:"
echo "1. Deploy in Unraid using the Docker Hub image"
echo "2. Open http://your-unraid-ip:5001"
echo "3. Generate QR codes for your show"
echo "4. Collect audience data"
echo "5. Track analytics and grow your following!"
echo ""
print_success "Happy Halloween! 🎃👻🦇✨"
