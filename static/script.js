// 🎃 ScarePi Web UI JavaScript 🦇

class ScarePiController {
    constructor() {
        this.motionEnabled = false;
        this.systemStatus = 'unknown';
        this.init();
    }

    init() {
        this.bindEvents();
        this.startStatusUpdates();
        this.updateStatus();
    }

    bindEvents() {
        // Motion toggle button
        document.getElementById('motionToggle').addEventListener('click', () => {
            this.toggleMotion();
        });

        // Manual control buttons
        document.getElementById('fullScareBtn').addEventListener('click', () => {
            this.triggerFullScare();
        });

        document.getElementById('propBtn').addEventListener('click', () => {
            this.triggerProp();
        });

        document.getElementById('soundBtn').addEventListener('click', () => {
            this.triggerSound();
        });

        document.getElementById('recordBtn').addEventListener('click', () => {
            this.triggerRecord();
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
        await this.triggerAction('/api/scare/full', 'Full scare sequence triggered! 💀');
    }

    async triggerProp() {
        await this.triggerAction('/api/scare/prop', 'Prop triggered! ⚡');
    }

    async triggerSound() {
        await this.triggerAction('/api/scare/sound', 'Scary sound playing! 🔊');
    }

    async triggerRecord() {
        await this.triggerAction('/api/scare/record', 'Recording started! 📹');
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

    async updateStatus() {
        try {
            const response = await fetch('/api/status');
            const data = await response.json();
            
            // Update system status
            this.systemStatus = data.scarepi_initialized ? 'Connected' : 'Disconnected';
            document.getElementById('systemStatus').textContent = this.systemStatus;
            document.getElementById('systemStatus').style.color = data.scarepi_initialized ? '#44ff44' : '#ff4444';
            
            // Update motion status
            this.motionEnabled = data.motion_enabled;
            this.updateMotionUI();
            
            // Update last update time
            document.getElementById('lastUpdate').textContent = new Date().toLocaleTimeString();
            
            // Update main status indicator
            const statusDot = document.querySelector('.status-dot');
            const statusText = document.getElementById('statusText');
            
            if (data.scarepi_initialized) {
                statusDot.classList.add('connected');
                statusText.textContent = 'System Online';
            } else {
                statusDot.classList.remove('connected');
                statusText.textContent = 'System Offline';
            }
            
        } catch (error) {
            console.error('Status update failed:', error);
            document.getElementById('systemStatus').textContent = 'Error';
            document.getElementById('systemStatus').style.color = '#ff4444';
        }
    }

    startStatusUpdates() {
        // Update status every 2 seconds
        setInterval(() => {
            this.updateStatus();
        }, 2000);
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
        } else {
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

// Initialize the controller when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new ScarePiController();
    
    // Add some spooky sound effects (optional)
    console.log('🎃 ScarePi Web UI Loaded! 🦇');
    console.log('🌙 Ready to control your haunted house!');
});
