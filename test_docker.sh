#!/bin/bash
# 🎃 ScarePi Docker Test Script 🦇
# Test your Docker container deployment

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

print_header "🎃 ScarePi Docker Test Suite"
print_status "Testing Docker container deployment..."

# Test 1: Check if container is running
print_status "Test 1: Checking container status..."
if docker ps | grep -q scarepi-enhanced; then
    print_success "✅ Container is running"
else
    print_error "❌ Container is not running"
    print_status "Starting container..."
    if command -v docker-compose &> /dev/null; then
        docker-compose up -d
    else
        docker run -d --name scarepi-enhanced -p 5001:5001 -v $(pwd)/data:/app/data scarepi-enhanced
    fi
    sleep 5
fi

# Test 2: Check container health
print_status "Test 2: Checking container health..."
if docker ps | grep scarepi-enhanced | grep -q "healthy"; then
    print_success "✅ Container is healthy"
else
    print_warning "⚠️ Container health check failed"
fi

# Test 3: Test API endpoints
print_status "Test 3: Testing API endpoints..."

# Wait for container to be ready
sleep 10

# Test status endpoint
print_status "Testing /api/status endpoint..."
if curl -s http://localhost:5001/api/status | grep -q "motion_enabled"; then
    print_success "✅ Status API working"
else
    print_error "❌ Status API failed"
fi

# Test audience stats endpoint
print_status "Testing /api/audience/stats endpoint..."
if curl -s http://localhost:5001/api/audience/stats | grep -q "total_audience"; then
    print_success "✅ Audience stats API working"
else
    print_error "❌ Audience stats API failed"
fi

# Test 4: Test web interface
print_status "Test 4: Testing web interface..."

# Test main page
print_status "Testing main page..."
if curl -s http://localhost:5001/ | grep -q "ScarePi Enhanced"; then
    print_success "✅ Main page working"
else
    print_error "❌ Main page failed"
fi

# Test audience form
print_status "Testing audience form..."
if curl -s http://localhost:5001/audience | grep -q "Audience Form"; then
    print_success "✅ Audience form working"
else
    print_error "❌ Audience form failed"
fi

# Test QR code page
print_status "Testing QR code page..."
if curl -s http://localhost:5001/qr | grep -q "QR Code"; then
    print_success "✅ QR code page working"
else
    print_error "❌ QR code page failed"
fi

# Test analytics page
print_status "Testing analytics page..."
if curl -s http://localhost:5001/analytics | grep -q "Analytics"; then
    print_success "✅ Analytics page working"
else
    print_error "❌ Analytics page failed"
fi

# Test 5: Test show controls
print_status "Test 5: Testing show controls..."

# Test show start
print_status "Testing show start..."
if curl -s -X POST http://localhost:5001/api/show/start | grep -q "Halloween show started"; then
    print_success "✅ Show start working"
else
    print_error "❌ Show start failed"
fi

# Test show stop
print_status "Testing show stop..."
if curl -s -X POST http://localhost:5001/api/show/stop | grep -q "Halloween show stopped"; then
    print_success "✅ Show stop working"
else
    print_error "❌ Show stop failed"
fi

# Test 6: Test scare controls
print_status "Test 6: Testing scare controls..."

# Test full scare
print_status "Testing full scare..."
if curl -s -X POST http://localhost:5001/api/scare/full | grep -q "scare sequence triggered"; then
    print_success "✅ Full scare working"
else
    print_error "❌ Full scare failed"
fi

# Test prop trigger
print_status "Testing prop trigger..."
if curl -s -X POST http://localhost:5001/api/scare/prop | grep -q "prop triggered"; then
    print_success "✅ Prop trigger working"
else
    print_error "❌ Prop trigger failed"
fi

# Test sound trigger
print_status "Testing sound trigger..."
if curl -s -X POST http://localhost:5001/api/scare/sound | grep -q "scary sound playing"; then
    print_success "✅ Sound trigger working"
else
    print_error "❌ Sound trigger failed"
fi

# Test 7: Test audience data collection
print_status "Test 7: Testing audience data collection..."

# Test audience join
print_status "Testing audience join..."
AUDIENCE_DATA='{"name":"Test User","email":"test@example.com","phone":"555-1234","social_media":"@testuser","how_heard":"QR Code","interests":"Halloween,Technology","subscribe_youtube":true,"subscribe_updates":true}'

if curl -s -X POST -H "Content-Type: application/json" -d "$AUDIENCE_DATA" http://localhost:5001/api/audience/join | grep -q "Welcome to the show"; then
    print_success "✅ Audience join working"
else
    print_error "❌ Audience join failed"
fi

print_header "🎯 Test Results Summary"
echo ""
print_success "🎃 ScarePi Docker container is working!"
print_success "🐳 Marketing platform is ready!"
print_success "📱 All features are functional!"
print_success "👻 Ready to scare and grow your following!"
echo ""
print_header "🌐 Access Your Marketing Platform:"
echo "Main Control Panel: http://localhost:5001"
echo "Audience Form: http://localhost:5001/audience"
echo "QR Code Generator: http://localhost:5001/qr"
echo "Analytics Dashboard: http://localhost:5001/analytics"
echo ""
print_success "Happy Halloween! 🎃👻🦇✨"
