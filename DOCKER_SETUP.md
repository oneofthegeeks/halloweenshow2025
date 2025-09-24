# 🐳 ScarePi Enhanced Docker Setup Guide 🎃

Deploy your Halloween marketing platform in Docker containers for Unraid, demos, and testing!

## 🚀 Quick Docker Setup

### 1. Build the Container
```bash
# Build the ScarePi Docker image
docker build -t scarepi-enhanced .

# Or use docker-compose
docker-compose up --build
```

### 2. Run the Container
```bash
# Run with docker-compose (recommended)
docker-compose up -d

# Or run directly
docker run -d \
  --name scarepi-enhanced \
  -p 5001:5001 \
  -v $(pwd)/data:/app/data \
  scarepi-enhanced
```

### 3. Access Your Marketing Platform
- **Main Control Panel**: `http://localhost:5001`
- **Audience Form**: `http://localhost:5001/audience`
- **QR Code Generator**: `http://localhost:5001/qr`
- **Analytics Dashboard**: `http://localhost:5001/analytics`

## 🏠 Unraid Setup

### 1. Create Custom Docker Container
1. Go to **Docker** tab in Unraid
2. Click **Add Container**
3. Configure as follows:

**Basic Settings:**
- **Name**: `scarepi-enhanced`
- **Repository**: `scarepi-enhanced:latest` (or your custom image)
- **Network Type**: `Bridge`

**Port Settings:**
- **Container Port**: `5001`
- **Host Port**: `5001` (or your preferred port)

**Path Settings:**
- **Container Path**: `/app/data`
- **Host Path**: `/mnt/user/appdata/scarepi/data`

### 2. Environment Variables
Add these environment variables:
- `FLASK_ENV=production`
- `PYTHONUNBUFFERED=1`

### 3. Start the Container
Click **Apply** and start the container!

## 🎯 Docker Features

### 🎃 Core Haunted House Features
- **Motion Detection Simulation**: Mock motion sensor for demos
- **Prop Control**: Simulated Halloween prop triggers
- **Sound Effects**: Mock scary sound playback
- **Video Recording**: Simulated scare recording
- **Web Control Panel**: Full Halloween-themed interface

### 📱 Marketing Platform Features
- **QR Code Generation**: Create QR codes for audience access
- **Audience Data Collection**: Comprehensive form system
- **Analytics Dashboard**: Real-time show statistics
- **Show Management**: Start/stop shows with monitoring
- **Social Media Integration**: YouTube and social sharing
- **Data Export**: Export audience data for marketing

### 🐳 Docker Optimizations
- **Health Checks**: Automatic container health monitoring
- **Data Persistence**: SQLite database with volume mounting
- **Resource Efficient**: Optimized for container environments
- **Security**: Non-root user and minimal attack surface
- **Logging**: Comprehensive logging for debugging

## 📊 Container Management

### View Logs
```bash
# Docker logs
docker logs scarepi-enhanced

# Follow logs
docker logs -f scarepi-enhanced
```

### Access Container Shell
```bash
# Execute shell in container
docker exec -it scarepi-enhanced /bin/bash

# Or with docker-compose
docker-compose exec scarepi /bin/bash
```

### Backup Data
```bash
# Backup audience database
docker cp scarepi-enhanced:/app/data/scarepi_audience.db ./backup/

# Backup all data
docker cp scarepi-enhanced:/app/data ./backup/
```

## 🔧 Configuration

### Environment Variables
- `FLASK_ENV`: Set to `production` for production use
- `PYTHONUNBUFFERED`: Set to `1` for proper logging
- `PORT`: Override default port (default: 5001)

### Volume Mounts
- `/app/data`: Persistent data storage
- `/app/scarepi_audience.db`: Database file
- `/app/static`: Static web assets
- `/app/templates`: HTML templates

## 🌐 Network Configuration

### Default Ports
- **Container Port**: 5001
- **Host Port**: 5001 (configurable)

### Reverse Proxy (Optional)
If using Traefik or Nginx:
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.scarepi.rule=Host(`scarepi.local`)"
  - "traefik.http.routers.scarepi.entrypoints=web"
  - "traefik.http.services.scarepi.loadbalancer.server.port=5001"
```

## 📱 Demo Features

### QR Code Marketing
1. Generate QR codes for your show
2. Print and display at your haunted house
3. Visitors scan to access audience form
4. Collect data and grow your following

### Audience Engagement
1. Comprehensive data collection form
2. Social media integration
3. YouTube subscription opt-ins
4. Email list building
5. Analytics tracking

### Show Management
1. Start/stop shows with live monitoring
2. Real-time statistics and analytics
3. Audience growth tracking
4. Performance optimization

## 🎃 Halloween Demo Ideas

### 1. Haunted House Demo
- Set up the container in your haunted house
- Generate QR codes for visitors
- Collect audience data during the show
- Track analytics and engagement

### 2. Marketing Demo
- Show the analytics dashboard
- Demonstrate QR code generation
- Collect demo audience data
- Export data for analysis

### 3. Social Media Demo
- Create viral content with the system
- Share QR codes on social media
- Grow your YouTube following
- Build your email list

## 🚀 Production Deployment

### 1. Build Production Image
```bash
# Build optimized production image
docker build -t scarepi-enhanced:latest .

# Tag for registry
docker tag scarepi-enhanced:latest your-registry/scarepi-enhanced:latest
```

### 2. Deploy to Unraid
1. Use the Unraid setup instructions above
2. Configure persistent volumes
3. Set up monitoring and logging
4. Configure reverse proxy if needed

### 3. Monitor and Maintain
- Check container health regularly
- Monitor resource usage
- Backup data periodically
- Update container as needed

## 🔧 Troubleshooting

### Container Won't Start
```bash
# Check logs
docker logs scarepi-enhanced

# Check container status
docker ps -a
```

### Database Issues
```bash
# Access container
docker exec -it scarepi-enhanced /bin/bash

# Check database
sqlite3 /app/data/scarepi_audience.db ".tables"
```

### Port Conflicts
```bash
# Check port usage
netstat -tulpn | grep 5001

# Use different port
docker run -p 5002:5001 scarepi-enhanced
```

## 📚 Additional Resources

- **README.md**: Complete project documentation
- **QUICKSTART.md**: Quick start guide
- **MARKETING_GUIDE.md**: Marketing strategies
- **Docker Hub**: Container registry
- **Unraid Community**: Support and tips

## 🎯 Ready to Scare and Grow!

Your ScarePi marketing platform is now ready for Docker deployment! 

**Features:**
- 🎃 Complete haunted house control system
- 📱 Marketing and audience engagement platform
- 📊 Analytics and performance tracking
- 🐳 Docker-optimized for easy deployment
- 🏠 Perfect for Unraid and home lab setups

**Start your Halloween empire today!** 👻🦇✨
