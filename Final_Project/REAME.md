# 📈 StockInfo - Stock Management Platform

Django web application for managing stock information with real-time data and AI insights.

## 🌟 Features

- **📊 Stock Management**: Browse and view detailed stock information
- **🔐 User Authentication**: Signup, login, logout system
- **👥 User Reviews**: Rate and review stocks (authenticated users only)
- **🤖 AI Summaries**: Google Gemini AI company insights (login required)
- **📈 Real-time Data**: Live stock prices via Alpha Vantage API
- **🎯 Admin Panel**: Full control over stocks and reviews

## 🛠️ Tech Stack

- **Backend**: Django 5.2.5, SQLite3
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **APIs**: Google Gemini (AI), Alpha Vantage (stock data)
- **Authentication**: Django built-in system


## 🎯 Usage

**Regular Users:**
- Browse stocks and view details
- Login for AI insights and reviews
- Rate and comment on stocks

**Administrators:**
- Manage stocks via `/admin/`
- Monitor user reviews
- Add/edit stock information

## 🤖 AI Features

- **Google Gemini AI** provides company summaries
- **Login required** to access AI insights
- Click "AI Summary" on stock detail pages

## 🔐 Security

- Django built-in password hashing
- CSRF protection
- Authentication-gated premium features
- Admin-only stock management
