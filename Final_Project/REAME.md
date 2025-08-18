# 📈 StockInfo - Stock Management Platform

Django web application for managing stock information with real-time data and AI insights.

## 🌟 Features

- **📊 Stock Management**: Browse and view detailed stock information
- **🔐 User Authentication**: Signup, login, logout system
- **👥 User Reviews**: Rate and review stocks (authenticated users only)
- **🤖 Advanced AI Features**: Company summaries, news analysis, market insights, price predictions (login required)
- **📈 Real-time Data**: Live stock prices via Alpha Vantage API
- **🎯 Admin Panel**: Full control over stocks and reviews

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5, SQLite3
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **APIs**: Google Gemini (AI), Alpha Vantage (stock data)
- **Authentication**: Django built-in system

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+ installed
- pip package manager
- Git (optional)

### Step 1: Clone/Download Project
```bash
# If using Git:
git clone <repository-url>
cd Final_Project

# Or download ZIP and extract
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Variables Setup
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

**Get API Keys:**
- **Gemini AI**: https://makersuite.google.com/app/apikey
- **Alpha Vantage**: https://www.alphavantage.co/support/#api-key
- **NewsAPI**: https://newsapi.org/register (Free: 1000 requests/day)

### Step 5: Database Setup
```bash
# Apply migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Load initial stock data (optional)
python manage.py shell
>>> exec(open('stocks/manage_stocks_update_db.py').read())
>>> exit()
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## 🎯 Usage

**Regular Users:**
- Browse stocks and view details
- Login for AI insights and reviews
- Rate and comment on stocks

**Administrators:**
- Manage stocks via `/admin/`
- Monitor user reviews
- Add/edit stock information

## 🤖 Advanced AI Features

**Four Powerful AI Analysis Tools** (Login Required):

1. **📝 Company Summary** - What the company does in simple terms
2. **📰 News Analysis** - Recent news + AI investment insights
3. **📊 Market Analysis** - Industry position, growth potential, investment recommendation
4. **🔮 Price Prediction** - Technical analysis & future outlook

**Powered by:**
- **Google Gemini AI** for intelligent analysis
- **NewsAPI** for real-time financial news
- **Alpha Vantage** for live market data

**Features:**
- Multi-language support (Hebrew/English)
- Real-time news aggregation
- Professional investment insights
- Educational disclaimers for responsible investing

## 🔐 Security

- Django built-in password hashing
- CSRF protection
- Authentication-gated premium features
- Admin-only stock management

## 🔧 Troubleshooting

### Common Issues:

**1. ModuleNotFoundError**
```bash
# Make sure virtual environment is activated
venv\Scripts\activate  # Windows
# Then reinstall requirements
pip install -r requirements.txt
```

**2. API Key Errors**
- Check `.env` file exists in project root
- Verify API keys are valid and active
- Ensure no extra spaces in `.env` file

**3. Database Errors**
```bash
# Reset database (WARNING: deletes all data)
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

**4. Static Files Not Loading**
```bash
python manage.py collectstatic
```

## 📂 Project Structure
```
Final_Project/
├── db.sqlite3              # Database file
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create this)
├── media/logos/           # Stock company logos
├── stockinfo/             # Main Django project
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL routing
│   └── ...
└── stocks/                # Stocks app
    ├── models.py          # Database models
    ├── views.py           # View logic
    ├── urls.py           # App URL routing
    ├── templates/         # HTML templates
    ├── static/           # CSS/JS files
    └── ...
```

## 🚀 Production Deployment

For production deployment:

1. **Environment Variables:**
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

2. **Database:** Consider PostgreSQL for production
3. **Static Files:** Configure proper static file serving
4. **Security:** Enable HTTPS and review security settings

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License.
