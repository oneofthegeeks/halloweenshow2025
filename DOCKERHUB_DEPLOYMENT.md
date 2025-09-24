# 🐳 Docker Hub Deployment Guide 🎃

Deploy ScarePi Enhanced from Docker Hub to Unraid!

## 🚀 Quick Setup

### 1. Build and Push to Docker Hub
```bash
# Run the Docker Hub push script
./push_to_dockerhub.sh

# Or manually:
docker build -t your-username/scarepi-enhanced:latest .
docker push your-username/scarepi-enhanced:latest
```

### 2. Deploy in Unraid
Use the Docker Hub image in Unraid Docker GUI:

**Repository:** `your-username/scarepi-enhanced:latest`

## 🏠 Unraid Docker GUI Setup

### Step 1: Create Container
1. Go to **Docker** tab in Unraid
2. Click **Add Container**
3. Configure as follows:

**Basic Settings:**
- **Name**: `scarepi-enhanced`
- **Repository**: `your-username/scarepi-enhanced:latest`
- **Network Type**: `Bridge`

**Port Settings:**
- **Container Port**: `5001`
- **Host Port**: `5001`

**Path Settings:**
- **Container Path**: `/app/data`
- **Host Path**: `/mnt/user/appdata/scarepi/data`

### Step 2: Environment Variables
Add these environment variables:
- `FLASK_ENV=production`
- `PYTHONUNBUFFERED=1`

### Step 3: Start Container
Click **Apply** and start the container!

## 🌐 Access Your Platform

Once deployed, access your Halloween marketing platform at:

- **Main Control Panel**: `http://your-unraid-ip:5001`
- **Audience Form**: `http://your-unraid-ip:5001/audience`
- **QR Code Generator**: `http://your-unraid-ip:5001/qr`
- **Analytics Dashboard**: `http://your-unraid-ip:5001/analytics`

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

## 🔧 Troubleshooting

### Container Won't Start
```bash
# Check logs
docker logs scarepi-enhanced

# Check container status
docker ps -a
```

### Port Conflicts
```bash
# Check port usage
netstat -tulpn | grep 5001

# Use different port in Unraid GUI
```

### Database Issues
```bash
# Access container
docker exec -it scarepi-enhanced /bin/bash

# Check database
sqlite3 /app/data/scarepi_audience.db ".tables"
```

## 📚 Additional Resources

- **GitHub Repository**: https://github.com/oneofthegeeks/halloweenshow2025
- **Docker Hub**: Your Docker Hub repository
- **Documentation**: Complete guides included
- **Support**: GitHub Issues and Community

## 🎃 Ready to Scare!

Your ScarePi Enhanced marketing platform is ready for Docker Hub deployment!

**Features:**
- 🎃 Complete haunted house control system
- 📱 Marketing and audience engagement platform
- 📊 Analytics and performance tracking
- 🐳 Docker Hub ready for easy deployment
- 🏠 Perfect for Unraid and home lab setups

**Start your Halloween empire today!** 👻🦇✨
