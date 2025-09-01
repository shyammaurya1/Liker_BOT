# 🤖 LikerBot - Social Media Automation Suite

> **Automate your social media engagement across multiple platforms with a single tool**

[![Python Version](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-2.2.6-green)](https://www.djangoproject.com/)
[![Selenium](https://img.shields.io/badge/selenium-automated-orange)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/license-Educational-yellow)](LICENSE)

## 🎯 What is LikerBot?

LikerBot is a powerful automation framework that streamlines social media engagement by automatically interacting with posts based on hashtags and keywords. Built with Python and Selenium, it provides both standalone scripts and a Django web interface for managing your automation tasks across Instagram, Facebook, Twitter, and LinkedIn.

---

## ✨ Key Features

### 🌐 **Universal Platform Support**
- **Instagram** - Engage with photos and stories based on hashtags
- **Twitter** - Auto-like tweets with specific keywords or hashtags  
- **LinkedIn** - Professional network engagement automation
- **Facebook** - Interact with posts and pages automatically

### 🎛️ **Flexible Operation Modes**
- **Standalone Scripts** - Run individual platform bots independently
- **Unified Interface** - Control all platforms from a single command center
- **Web Dashboard** - User-friendly HTML interface for non-technical users
- **Batch Processing** - Process multiple posts in intelligent cycles

### 🔧 **Smart Automation**
- Hashtag-based targeting for precision engagement
- Randomized delays to mimic human behavior
- Scroll automation for discovering new content
- Session management with auto-recovery

---

## 🚀 Quick Start

### Prerequisites

Before you begin, ensure you have the following installed:
- ✅ Python 3.x or higher
- ✅ Firefox Browser
- ✅ Git (for cloning the repository)

### Installation

#### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/likerbot.git
cd likerbot
```

#### 2️⃣ **Set Up Virtual Environment** (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```
*If requirements.txt doesn't exist, install manually:*
```bash
pip install django==2.2.6 selenium
```

#### 4️⃣ **Install Geckodriver**

**Option A: Manual Installation**
- Download from [Mozilla Geckodriver Releases](https://github.com/mozilla/geckodriver/releases)
- Extract and add to your system PATH

**Option B: Using Package Manager**
```bash
# macOS
brew install geckodriver

# Ubuntu/Debian
sudo apt-get install firefox-geckodriver

# Windows (using chocolatey)
choco install selenium-gecko-driver
```

#### 5️⃣ **Initialize Django Database**
```bash
python manage.py migrate
python manage.py createsuperuser  # Optional: for admin access
```

---

## 💻 Usage Guide

### 🌟 **Web Application Mode**

Start the Django development server:
```bash
python manage.py runserver
```

Access the application at: `http://localhost:8000`

**Available Routes:**
- `/` - Main dashboard
- `/instagram/` - Instagram automation interface
- `/admin/` - Django admin panel

### 🔧 **Command Line Mode**

**Run All Platforms (Interactive Menu):**
```bash
python main.py
```

**Platform-Specific Execution:**
```bash
# Instagram Automation
python individual\ files-without\ django/insta.py

# Twitter Automation
python individual\ files-without\ django/twitter.py

# LinkedIn Automation
python individual\ files-without\ django/Linkedin.py

# Facebook Automation
python individual\ files-without\ django/facebook.py
```

### ⚙️ **Configuration**

Create a `config.py` file (recommended):
```python
# config.py
INSTAGRAM_CONFIG = {
    'username': 'your_username',
    'password': 'your_password',
    'hashtags': ['photography', 'nature', 'travel'],
    'like_limit': 50,
    'delay_range': (2, 5)
}

TWITTER_CONFIG = {
    'username': 'your_email@example.com',
    'password': 'your_password',
    'hashtags': ['tech', 'coding', 'python'],
    'like_limit': 30
}

# Similar configs for LinkedIn and Facebook
```

---

## 📁 Project Architecture

```
likerbot/
│
├── 📂 individual files-without django/
│   ├── 🐍 insta.py                 # Instagram bot logic
│   ├── 🐍 twitter.py               # Twitter bot logic
│   ├── 🐍 Linkedin.py              # LinkedIn bot logic
│   ├── 🐍 facebook.py              # Facebook bot logic
│   ├── 🐍 main.py                  # Unified bot controller
│   ├── 🐍 myinsta.py              # Alternative Instagram implementation
│   ├── 📄 documentation            # Setup notes
│   │
│   └── 📂 frontend/
│       ├── 🎨 Basics.html         # Landing page
│       ├── 🎨 instagram.html      # Instagram interface
│       ├── 🎨 Twitter.html        # Twitter interface
│       ├── 🎨 facebook_activity.html
│       └── 🎨 style.css           # Styling
│
├── 📂 liker/                      # Django application
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   └── 🐍 views.py (not included)
│
├── 📂 likerbot/                   # Django project settings
│   ├── 🐍 settings.py
│   ├── 🐍 urls.py
│   └── 🐍 wsgi.py
│
└── 🐍 manage.py                   # Django management script
```

---

## 🛡️ Security Best Practices

### 🔐 **Credential Management**
```python
# ❌ NEVER DO THIS
username = "myusername@email.com"
password = "mypassword123"

# ✅ DO THIS INSTEAD
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('INSTAGRAM_USERNAME')
password = os.getenv('INSTAGRAM_PASSWORD')
```

### 📝 **Create .env File**
```bash
# .env
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
TWITTER_EMAIL=your_email@example.com
TWITTER_PASSWORD=your_password
```

### 🚫 **Add to .gitignore**
```bash
# .gitignore
.env
*.pyc
__pycache__/
venv/
config.py
credentials.json
```

---

## ⚖️ Legal & Ethical Considerations

### ⚠️ **Important Disclaimer**

> **This tool is developed for EDUCATIONAL PURPOSES ONLY**

Using automation tools on social media platforms may:
- 🚫 Violate Terms of Service agreements
- 🔒 Result in account suspension or permanent ban
- 📉 Affect your account's reputation and reach
- ⚖️ Have legal implications depending on your jurisdiction

### ✅ **Responsible Usage Guidelines**

1. **Respect Rate Limits** - Don't exceed platform-specific interaction limits
2. **Human-Like Behavior** - Use random delays and natural interaction patterns
3. **Quality Over Quantity** - Focus on meaningful engagement
4. **Platform Policies** - Regularly review and comply with ToS updates
5. **Ethical Engagement** - Use automation to supplement, not replace, genuine interaction

---

## 🔄 Future Enhancements

- [ ] **OAuth Integration** - Secure authentication without password storage
- [ ] **Proxy Support** - Rotate IP addresses for enhanced privacy
- [ ] **Analytics Dashboard** - Track engagement metrics and performance
- [ ] **Scheduling System** - Set up automated tasks with cron-like scheduling
- [ ] **Machine Learning** - Smart content targeting based on engagement patterns
- [ ] **Docker Support** - Containerized deployment for easy setup
- [ ] **API Mode** - RESTful API for integration with other tools
- [ ] **Multi-Account Management** - Handle multiple accounts per platform

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the Repository** - Create your own copy
2. **Create a Feature Branch** - `git checkout -b feature/AmazingFeature`
3. **Commit Changes** - `git commit -m 'Add some AmazingFeature'`
4. **Push to Branch** - `git push origin feature/AmazingFeature`
5. **Open Pull Request** - We'll review and merge your changes

### 📋 **Contribution Guidelines**
- Write clean, documented code
- Follow PEP 8 style guidelines
- Include unit tests for new features
- Update documentation as needed

---

## 🐛 Troubleshooting

### Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| **Geckodriver not found** | Ensure geckodriver is in PATH or specify path in code |
| **Login fails** | Check credentials and inspect for UI changes |
| **Elements not found** | Platform may have updated HTML structure |
| **Rate limiting** | Increase delays between actions |
| **Session timeout** | Implement session refresh logic |

### 📊 **Debug Mode**

Enable verbose logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 📚 Resources

- [Selenium Documentation](https://selenium-python.readthedocs.io/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Python Best Practices](https://docs.python-guide.org/)
- [Social Media APIs](https://developers.facebook.com/)

---

## 📜 License

This project is provided **AS-IS** for educational and research purposes only. Users are responsible for complying with all applicable laws and platform terms of service.

---

## 👥 Connect & Support

- 💬 **Questions?** Open an issue
- 🐛 **Found a bug?** Submit a bug report
- 💡 **Have an idea?** Suggest a feature
- ⭐ **Like the project?** Give it a star!

---

<div align="center">

**Made with ❤️ by developers, for developers**

*Remember: With great automation comes great responsibility*

</div>
