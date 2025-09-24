# 🚀 GitHub Actions Docker Hub Setup 🎃

Automatically build and push ScarePi Enhanced to Docker Hub using GitHub Actions!

## 🔧 Setup Instructions

### Step 1: Create Docker Hub Access Token
1. Go to [Docker Hub](https://hub.docker.com)
2. Click your profile → **Account Settings**
3. Go to **Security** → **New Access Token**
4. Create a token with **Read, Write, Delete** permissions
5. Copy the token (you'll need it for GitHub)

### Step 2: Add GitHub Secrets
1. Go to your GitHub repository: `https://github.com/oneofthegeeks/halloweenshow2025`
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add these secrets:

**Secret 1:**
- **Name**: `DOCKERHUB_USERNAME`
- **Value**: `oneofthegeeks`

**Secret 2:**
- **Name**: `DOCKERHUB_TOKEN`
- **Value**: `your-docker-hub-access-token`

### Step 3: Trigger the Build
The GitHub Action will automatically run when you:
- Push a new tag (like `v1.0.1`)
- Manually trigger it from the Actions tab

## 🎯 Manual Trigger
1. Go to **Actions** tab in your GitHub repository
2. Click **🐳 Build and Push to Docker Hub**
3. Click **Run workflow**
4. Click **Run workflow** button

## 📦 What Gets Built
- **Image**: `oneofthegeeks/scarepi-enhanced:latest`
- **Tags**: `oneofthegeeks/scarepi-enhanced:v1.0.0`
- **Platforms**: `linux/amd64`, `linux/arm64`

## 🏠 Unraid Deployment
Once the GitHub Action completes, use in Unraid:

**Repository:** `oneofthegeeks/scarepi-enhanced:latest`

## 🌐 Access Your Platform
- **Main Control Panel**: `http://your-unraid-ip:5001`
- **Audience Form**: `http://your-unraid-ip:5001/audience`
- **QR Code Generator**: `http://your-unraid-ip:5001/qr`
- **Analytics Dashboard**: `http://your-unraid-ip:5001/analytics`

## 🎃 Features Available
- **QR Code Generation**: Create QR codes for viral sharing
- **Audience Data Collection**: Build your email list
- **Analytics Dashboard**: Track performance and engagement
- **Show Management**: Start/stop shows with live monitoring
- **Social Media Integration**: YouTube and social sharing
- **Performance Tracking**: Optimize your Halloween show

## 🔧 Troubleshooting
If the build fails:
1. Check the **Actions** tab for error logs
2. Verify your Docker Hub secrets are correct
3. Make sure your Docker Hub token has the right permissions

## 🎯 Ready to Deploy!
Your ScarePi Enhanced will be automatically built and pushed to Docker Hub!

**Start your Halloween marketing empire today!** 👻🦇✨
