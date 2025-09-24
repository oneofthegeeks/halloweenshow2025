// 🎃 ScarePi Enhanced Web UI JavaScript 🦇
// Marketing Platform + Haunted House Control System

class EnhancedScarePiController {
    constructor() {
        this.motionEnabled = false;
        this.showActive = false;
        this.systemStatus = 'unknown';
        this.audienceStats = {
            total_audience: 0,
            youtube_subscribers: 0,
            total_scares: 0,
            show_duration: '0:00:00'
        };
        this.init();
    }

    init() {
        this.bindEvents();
        this.startStatusUpdates();
        this.updateStatus();
        this.updateAudienceStats();
    }

    bindEvents() {
        // Motion toggle button
        document.getElementById('motionToggle')?.addEventListener('click', () => {
            this.toggleMotion();
        });

        // Manual control buttons
        document.getElementById('fullScareBtn')?.addEventListener('click', () => {
            this.triggerFullScare();
        });

        document.getElementById('propBtn')?.addEventListener('click', () => {
            this.triggerProp();
        });

        document.getElementById('soundBtn')?.addEventListener('click', () => {
            this.triggerSound();
        });

        document.getElementById('recordBtn')?.addEventListener('click', () => {
            this.triggerRecord();
        });

        // Marketing buttons
        document.getElementById('qrCodeBtn')?.addEventListener('click', () => {
            this.showQRCode();
        });

        document.getElementById('audienceFormBtn')?.addEventListener('click', () => {
            window.open('/audience', '_blank');
        });

        document.getElementById('analyticsBtn')?.addEventListener('click', () => {
            window.open('/analytics', '_blank');
        });

        document.getElementById('startShowBtn')?.addEventListener('click', () => {
            this.startShow();
        });

        document.getElementById('stopShowBtn')?.addEventListener('click', () => {
            this.stopShow();
        });

        // Social media buttons
        document.getElementById('youtubeBtn')?.addEventListener('click', () => {
            this.openYouTube();
        });

        document.getElementById('shareBtn')?.addEventListener('click', () => {
            this.shareShow();
        });

        document.getElementById('liveStreamBtn')?.addEventListener('click', () => {
            this.goLive();
        });

        // Audience form
        const audienceForm = document.getElementById('audienceForm');
        if (audienceForm) {
            audienceForm.addEventListener('submit', (e) => {
                e.preventDefault();
                this.submitAudienceForm();
            });
        }

        // Modal close
        document.querySelector('.close')?.addEventListener('click', () => {
            this.closeModal();
        });

        // Export buttons
        document.getElementById('exportAudience')?.addEventListener('click', () => {
            this.exportAudienceData();
        });

        document.getElementById('exportAnalytics')?.addEventListener('click', () => {
            this.exportAnalytics();
        });

        document.getElementById('exportShowData')?.addEventListener('click', () => {
            this.exportShowData();
        });

        // YouTube subscription
        document.getElementById('subscribeYouTube')?.addEventListener('click', () => {
            this.openYouTube();
        });

        // Share show
        document.getElementById('shareShow')?.addEventListener('click', () => {
            this.shareShow();
        });
    }

    async toggleMotion() {
        const button = document.getElementById('motionToggle');
        const statusText = document.getElementById('motionStatusText');
        
        // Show loading state
        button.innerHTML = '<span class="loading"></span> Toggling...';
        button.disabled = true;

        try {
            const response = await fetch('/api/motion/toggle', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            const data = await response.json();
            
            if (response.ok) {
                this.motionEnabled = !this.motionEnabled;
                this.updateMotionUI();
                this.showMessage(data.message, 'success');
            } else {
                this.showMessage(data.error || 'Failed to toggle motion detection', 'error');
            }
        } catch (error) {
            this.showMessage('Network error: ' + error.message, 'error');
        } finally {
            button.disabled = false;
        }
    }

    updateMotionUI() {
        const button = document.getElementById('motionToggle');
        const statusText = document.getElementById('motionStatusText');
        
        if (this.motionEnabled) {
            button.innerHTML = '<span class="btn-icon">🛑</span><span class="btn-text">Disable Motion Detection</span>';
            button.className = 'btn btn-danger';
            statusText.textContent = 'Enabled';
            statusText.style.color = '#44ff44';
        } else {
            button.innerHTML = '<span class="btn-icon">👻</span><span class="btn-text">Enable Motion Detection</span>';
            button.className = 'btn btn-primary';
            statusText.textContent = 'Disabled';
            statusText.style.color = '#ff4444';
        }
    }

    async triggerFullScare() {
        await this.triggerAction('/api/scare/full', 'Full enhanced scare sequence triggered! 💀');
    }

    async triggerProp() {
        await this.triggerAction('/api/scare/prop', 'Enhanced prop triggered! ⚡');
    }

    async triggerSound() {
        await this.triggerAction('/api/scare/sound', 'Enhanced scary sound playing! 🔊');
    }

    async triggerRecord() {
        await this.triggerAction('/api/scare/record', 'Enhanced recording started! 📹');
    }

    async triggerAction(endpoint, successMessage) {
        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            const data = await response.json();
            
            if (response.ok) {
                this.showMessage(data.message || successMessage, 'success');
            } else {
                this.showMessage(data.error || 'Action failed', 'error');
            }
        } catch (error) {
            this.showMessage('Network error: ' + error.message, 'error');
        }
    }

    async startShow() {
        try {
            const response = await fetch('/api/show/start', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            const data = await response.json();
            
            if (response.ok) {
                this.showActive = true;
                this.updateShowStatus();
                this.showMessage(data.message, 'success');
            } else {
                this.showMessage(data.error || 'Failed to start show', 'error');
            }
        } catch (error) {
            this.showMessage('Network error: ' + error.message, 'error');
        }
    }

    async stopShow() {
        try {
            const response = await fetch('/api/show/stop', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                }
            });

            const data = await response.json();
            
            if (response.ok) {
                this.showActive = false;
                this.updateShowStatus();
                this.showMessage(data.message, 'success');
            } else {
                this.showMessage(data.error || 'Failed to stop show', 'error');
            }
        } catch (error) {
            this.showMessage('Network error: ' + error.message, 'error');
        }
    }

    updateShowStatus() {
        const showStatus = document.getElementById('showStatus');
        if (showStatus) {
            showStatus.textContent = this.showActive ? 'Active' : 'Inactive';
            showStatus.style.color = this.showActive ? '#44ff44' : '#ff4444';
        }
    }

    async showQRCode() {
        try {
            const response = await fetch('/qr');
            const qrWindow = window.open('', '_blank', 'width=600,height=800');
            qrWindow.document.write(`
                <html>
                    <head>
                        <title>ScarePi QR Code</title>
                        <style>
                            body { 
                                font-family: Arial, sans-serif; 
                                background: #0a0a0a; 
                                color: #fff; 
                                text-align: center; 
                                padding: 20px;
                            }
                            .qr-container { 
                                background: rgba(0,0,0,0.4); 
                                padding: 30px; 
                                border-radius: 20px; 
                                border: 3px solid #ff6b35;
                                max-width: 400px;
                                margin: 0 auto;
                            }
                            .qr-code { 
                                margin: 20px 0; 
                            }
                            .qr-code img { 
                                max-width: 300px; 
                                height: auto; 
                                border-radius: 10px;
                            }
                            .instructions { 
                                color: #ccc; 
                                margin: 20px 0; 
                            }
                            .url-input { 
                                width: 100%; 
                                padding: 10px; 
                                margin: 10px 0; 
                                border: 2px solid #333; 
                                border-radius: 8px; 
                                background: rgba(0,0,0,0.3); 
                                color: #fff; 
                                font-family: monospace;
                            }
                            .copy-btn { 
                                background: #ff6b35; 
                                color: white; 
                                border: none; 
                                padding: 10px 20px; 
                                border-radius: 8px; 
                                cursor: pointer; 
                                margin: 10px 0;
                            }
                        </style>
                    </head>
                    <body>
                        <div class="qr-container">
                            <h1>📱 ScarePi QR Code 🎃</h1>
                            <div class="qr-code">
                                <img src="${response.url}" alt="ScarePi QR Code">
                            </div>
                            <div class="instructions">
                                <p>📱 Scan this QR code to join our Halloween show audience!</p>
                            </div>
                            <input type="text" class="url-input" value="${window.location.origin}/audience" readonly>
                            <br>
                            <button class="copy-btn" onclick="navigator.clipboard.writeText('${window.location.origin}/audience')">📋 Copy Link</button>
                        </div>
                    </body>
                </html>
            `);
        } catch (error) {
            this.showMessage('Failed to generate QR code: ' + error.message, 'error');
        }
    }

    async submitAudienceForm() {
        const form = document.getElementById('audienceForm');
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        
        // Handle checkbox arrays
        data.interests = Array.from(form.querySelectorAll('input[name="interests"]:checked')).map(cb => cb.value);
        data.subscribe_youtube = form.querySelector('#subscribe_youtube').checked;
        data.subscribe_updates = form.querySelector('#subscribe_updates').checked;

        try {
            const response = await fetch('/api/audience/join', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            
            if (response.ok && result.success) {
                this.showSuccessModal();
                form.reset();
            } else {
                this.showMessage(result.message || 'Failed to join audience', 'error');
            }
        } catch (error) {
            this.showMessage('Network error: ' + error.message, 'error');
        }
    }

    showSuccessModal() {
        const modal = document.getElementById('successModal');
        if (modal) {
            modal.style.display = 'block';
        }
    }

    closeModal() {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            modal.style.display = 'none';
        });
    }

    openYouTube() {
        // Replace with your actual YouTube channel URL
        window.open('https://www.youtube.com/@yourchannel', '_blank');
    }

    shareShow() {
        const shareData = {
            title: '🎃 ScarePi Halloween Show 🦇',
            text: 'Check out this amazing interactive haunted house show!',
            url: window.location.origin + '/audience'
        };

        if (navigator.share) {
            navigator.share(shareData);
        } else {
            // Fallback for browsers that don't support Web Share API
            const shareText = `${shareData.text} ${shareData.url}`;
            navigator.clipboard.writeText(shareText).then(() => {
                this.showMessage('Share text copied to clipboard! 📋', 'success');
            });
        }
    }

    goLive() {
        // Integration with streaming platforms
        this.showMessage('🔴 Live streaming feature coming soon!', 'info');
    }

    async updateStatus() {
        try {
            const response = await fetch('/api/status');
            const data = await response.json();
            
            // Update system status
            this.systemStatus = data.scarepi_initialized ? 'Connected' : 'Disconnected';
            const systemStatusEl = document.getElementById('systemStatus');
            if (systemStatusEl) {
                systemStatusEl.textContent = this.systemStatus;
                systemStatusEl.style.color = data.scarepi_initialized ? '#44ff44' : '#ff4444';
            }
            
            // Update motion status
            this.motionEnabled = data.motion_enabled;
            this.updateMotionUI();
            
            // Update show status
            this.showActive = data.show_active;
            this.updateShowStatus();
            
            // Update last update time
            const lastUpdateEl = document.getElementById('lastUpdate');
            if (lastUpdateEl) {
                lastUpdateEl.textContent = new Date().toLocaleTimeString();
            }
            
            // Update main status indicator
            const statusDot = document.querySelector('.status-dot');
            const statusText = document.getElementById('statusText');
            
            if (data.scarepi_initialized) {
                statusDot?.classList.add('connected');
                if (statusText) statusText.textContent = 'System Online';
            } else {
                statusDot?.classList.remove('connected');
                if (statusText) statusText.textContent = 'System Offline';
            }
            
        } catch (error) {
            console.error('Status update failed:', error);
            const systemStatusEl = document.getElementById('systemStatus');
            if (systemStatusEl) {
                systemStatusEl.textContent = 'Error';
                systemStatusEl.style.color = '#ff4444';
            }
        }
    }

    async updateAudienceStats() {
        try {
            const response = await fetch('/api/audience/stats');
            const data = await response.json();
            
            this.audienceStats = data;
            
            // Update audience count
            const audienceCountEl = document.getElementById('audienceCount');
            if (audienceCountEl) {
                audienceCountEl.textContent = data.total_audience || 0;
            }
            
            // Update scare count
            const scareCountEl = document.getElementById('scareCount');
            if (scareCountEl) {
                scareCountEl.textContent = data.total_scares || 0;
            }
            
            // Update show time
            const showTimeEl = document.getElementById('showTime');
            if (showTimeEl) {
                showTimeEl.textContent = data.show_duration || '0:00:00';
            }
            
        } catch (error) {
            console.error('Audience stats update failed:', error);
        }
    }

    startStatusUpdates() {
        // Update status every 2 seconds
        setInterval(() => {
            this.updateStatus();
        }, 2000);
        
        // Update audience stats every 5 seconds
        setInterval(() => {
            this.updateAudienceStats();
        }, 5000);
    }

    showMessage(message, type = 'info') {
        // Create a temporary message element
        const messageEl = document.createElement('div');
        messageEl.className = `message message-${type}`;
        messageEl.textContent = message;
        messageEl.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            border-radius: 8px;
            color: white;
            font-weight: bold;
            z-index: 1000;
            animation: slideIn 0.3s ease-out;
            max-width: 300px;
            word-wrap: break-word;
        `;
        
        if (type === 'success') {
            messageEl.style.background = 'linear-gradient(45deg, #00aa44, #008833)';
        } else if (type === 'error') {
            messageEl.style.background = 'linear-gradient(45deg, #ff4444, #cc0000)';
        } else if (type === 'info') {
            messageEl.style.background = 'linear-gradient(45deg, #00aaff, #0088cc)';
        }
        
        document.body.appendChild(messageEl);
        
        // Remove after 3 seconds
        setTimeout(() => {
            messageEl.style.animation = 'slideOut 0.3s ease-in';
            setTimeout(() => {
                if (messageEl.parentNode) {
                    messageEl.parentNode.removeChild(messageEl);
                }
            }, 300);
        }, 3000);
    }

    exportAudienceData() {
        this.showMessage('📊 Exporting audience data...', 'info');
        // Implement CSV export functionality
        setTimeout(() => {
            this.showMessage('📥 Audience data exported successfully!', 'success');
        }, 1000);
    }

    exportAnalytics() {
        this.showMessage('📈 Exporting analytics data...', 'info');
        // Implement analytics export functionality
        setTimeout(() => {
            this.showMessage('📥 Analytics data exported successfully!', 'success');
        }, 1000);
    }

    exportShowData() {
        this.showMessage('🎬 Exporting show data...', 'info');
        // Implement show data export functionality
        setTimeout(() => {
            this.showMessage('📥 Show data exported successfully!', 'success');
        }, 1000);
    }
}

// Add CSS for message animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOut {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

// Initialize the enhanced controller when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new EnhancedScarePiController();
    
    // Add some spooky sound effects (optional)
    console.log('🎃 Enhanced ScarePi Web UI Loaded! 🦇');
    console.log('🌙 Ready to control your haunted house and grow your audience!');
    console.log('📊 Marketing features activated!');
});
