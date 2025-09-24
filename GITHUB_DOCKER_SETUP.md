# 🐳 GitHub Docker Setup Guide 🎃

Deploy ScarePi Enhanced directly from GitHub repository!

## 🚀 Quick Start from GitHub

### 1. Clone the Repository
```bash
git clone https://github.com/oneofthegeeks/halloweenshow2025.git
cd halloweenshow2025
```

### 2. Build from GitHub
```bash
# Build using Docker Compose (recommended)
docker-compose up --build -d

# Or build manually from GitHub
docker build -t scarepi-enhanced https://github.com/oneofthegeeks/halloweenshow2025.git#v1.0.0
```

### 3. Run the Container
```bash
# Using Docker Compose
docker-compose up -d

# Or run directly
docker run -d \
  --name scarepi-enhanced \
  -p 5001:5001 \
  -v $(pwd)/data:/app/data \
  scarepi-enhanced
```

## 🏠 Unraid Setup from GitHub

### 1. Create Custom Docker Container
1. Go to **Docker** tab in Unraid
2. Click **Add Container**
3. Configure as follows:

**Basic Settings:**
- **Name**: `scarepi-enhanced`
- **Repository**: `scarepi-enhanced:latest`
- **Network Type**: `Bridge`

**Port Settings:**
- **Container Port**: `5001`
- **Host Port**: `5001` (or your preferred port)

**Path Settings:**
- **Container Path**: `/app/data`
- **Host Path**: `/mnt/user/appdata/scarepi/data`

### 2. Build from GitHub
```bash
# SSH into your Unraid server
ssh root@your-unraid-ip

# Clone the repository
git clone https://github.com/oneofthegeeks/halloweenshow2025.git
cd halloweenshow2025

# Build the Docker image
docker build -t scarepi-enhanced .

# Run the container
docker run -d \
  --name scarepi-enhanced \
  -p 5001:5001 \
  -v /mnt/user/appdata/scarepi/data:/app/data \
  scarepi-enhanced
```

## 🌐 Public Repository Access

### Repository Information
- **GitHub URL**: https://github.com/oneofthegeeks/halloweenshow2025
- **Latest Release**: v1.0.0
- **Docker Support**: Full containerization included
- **Documentation**: Complete guides provided

### Docker Build Contexts

**Option 1: Local Clone (Recommended)**
```bash
git clone https://github.com/oneofthegeeks/halloweenshow2025.git
cd halloweenshow2025
docker build -t scarepi-enhanced .
```

**Option 2: Direct GitHub Build**
```bash
docker build -t scarepi-enhanced https://github.com/oneofthegeeks/halloweenshow2025.git#v1.0.0
```

**Option 3: Docker Compose**
```bash
git clone https://github.com/oneofthegeeks/halloweenshow2025.git
cd halloweenshow2025
docker-compose up --build -d
```

## 📱 Access Your Platform

Once deployed, access your Halloween marketing platform at:

- **Main Control Panel**: `http://your-server:5001`
- **Audience Form**: `http://your-server:5001/audience`
- **QR Code Generator**: `http://your-server:5001/qr`
- **Analytics Dashboard**: `http://your-server:5001/analytics`

## 🔧 Environment Variables

### Production Settings
```bash
FLASK_ENV=production
PYTHONUNBUFFERED=1
```

### Development Settings
```bash
FLASK_ENV=development
PYTHONUNBUFFERED=1
DEBUG=true
```

## 📊 Volume Mounting

### Data Persistence
```bash
# Local development
-v $(pwd)/data:/app/data

# Unraid deployment
-v /mnt/user/appdata/scarepi/data:/app/data

# Docker Compose
volumes:
  - ./data:/app/data
```

## 🎯 Features Available

### 🎃 Haunted House Control
- Motion detection simulation
- Prop control triggers
- Sound effect playback
- Video recording simulation
- Web-based control panel

### 📱 Marketing Platform
- QR code generation for viral sharing
- Audience data collection and analytics
- Show management with live monitoring
- Social media integration
- YouTube subscriber growth
- Email list building

### 📊 Analytics & Monitoring
- Real-time show statistics
- Audience engagement tracking
- Performance optimization
- Data export capabilities
- Health monitoring

## 🚀 Deployment Options

### 1. Local Development
```bash
git clone https://github.com/oneofthegeeks/halloweenshow2025.git
cd halloweenshow2025
docker-compose up --build
```

### 2. Production Deployment
```bash
git clone https://github.com/oneofthegeeks/halloweenshow2025.git
cd halloweenshow2025
docker-compose -f docker-compose.yml up -d
```

### 3. Unraid Deployment
1. Clone repository to Unraid server
2. Build Docker image
3. Create container with proper volume mounts
4. Start and enjoy!

## 🔧 Troubleshooting

### Container Won't Start
```bash
# Check logs
docker logs scarepi-enhanced

# Check container status
docker ps -a

# Rebuild if needed
docker-compose down
docker-compose up --build -d
```

### Port Conflicts
```bash
# Check port usage
netstat -tulpn | grep 5001

# Use different port
docker run -p 5002:5001 scarepi-enhanced
```

### Database Issues
```bash
# Access container
docker exec -it scarepi-enhanced /bin/bash

# Check database
sqlite3 /app/data/scarepi_audience.db ".tables"
```

## 📚 Additional Resources

- **Repository**: https://github.com/oneofthegeeks/halloweenshow2025
- **Releases**: https://github.com/oneofthegeeks/halloweenshow2025/releases
- **Issues**: https://github.com/oneofthegeeks/halloweenshow2025/issues
- **Documentation**: Complete guides included in repository

## 🎃 Ready to Scare!

Your ScarePi Enhanced marketing platform is ready for deployment from GitHub!

**Features:**
- 🎃 Complete haunted house control system
- 📱 Marketing and audience engagement platform
- 📊 Analytics and performance tracking
- 🐳 Docker-optimized for easy deployment
- 🏠 Perfect for Unraid and home lab setups

**Start your Halloween empire today!** 👻🦇✨
