# Crime Report System

A comprehensive online crime reporting and management system that allows citizens to file complaints, track status, view crime statistics, and access location-based crime information.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Current Technology Stack](#current-technology-stack)
- [Recommended Technology Stack](#recommended-technology-stack)
- [Features](#features)
- [Installation Guide](#installation-guide)
- [Migration Plan](#migration-plan)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Contributing](#contributing)

---

## 🎯 Overview

The Crime Report System is a web application designed to modernize crime reporting by replacing traditional manual complaint registration systems. Citizens can file complaints online, attach evidence, track case status, and access crime-related information in their area.

**Key Objectives:**
- Simplify crime reporting for citizens
- Improve response time for law enforcement
- Provide transparency in complaint handling
- Enable data-driven crime prevention

---

## 🛠️ Current Technology Stack

### Backend
- **Framework:** Django 3.2.4
- **Language:** Python 3.x
- **Database:** SQLite3
- **Authentication:** Django Auth System
- **Email:** Django SMTP Backend

### Frontend
- **Template Engine:** Django Templates
- **CSS Framework:** Bootstrap 5.0.2
- **JavaScript:** Vanilla JS
- **Icons:** Font Awesome 4.7.0
- **Fonts:** Google Fonts (Poppins)

### Third-Party Libraries
- **newsapi-python:** News feed integration
- **folium:** Interactive maps
- **geocoder:** Location geocoding
- **django-crispy-forms:** Form rendering
- **crispy-bootstrap4:** Bootstrap 4 template pack

### Current Features
1. User Registration & Authentication
2. Crime Complaint Filing
3. Complaint Status Checking
4. Location-based Crime Search
5. News Feed Integration
6. Email Notifications

---

## 🚀 Recommended Technology Stack (Modernized)

### Backend
- **Framework:** Django 5.1 (latest stable)
- **Language:** Python 3.11+
- **Database:** PostgreSQL 15+ with PostGIS extension
- **API Framework:** Django REST Framework 3.14+
- **Task Queue:** Celery 5.3+ with Redis broker
- **Caching:** Redis 7.x
- **Authentication:** Django REST Framework JWT / Simple JWT
- **Email:** Celery async tasks with SMTP backend
- **File Storage:** AWS S3 / MinIO for evidence files
- **API Documentation:** drf-spectacular (OpenAPI/Swagger)

### Frontend (New React Application)
- **Framework:** React 18+
- **Language:** TypeScript 5+
- **Build Tool:** Vite 5+
- **CSS Framework:** Tailwind CSS 3+
- **Component Library:** shadcn/ui
- **State Management:** 
  - Zustand (global state)
  - React Query / TanStack Query (server state)
- **Routing:** React Router 6+
- **Maps:** React Leaflet / Google Maps React
- **Forms:** React Hook Form + Zod validation
- **HTTP Client:** Axios
- **Charts:** Recharts / Chart.js
- **Notifications:** React Hot Toast

### DevOps & Infrastructure
- **Containerization:** Docker + Docker Compose
- **Reverse Proxy:** Nginx
- **WSGI Server:** Gunicorn
- **Process Manager:** Supervisor / systemd
- **CI/CD:** GitHub Actions / GitLab CI
- **Monitoring:** Sentry (error tracking)
- **Logging:** ELK Stack or Grafana Loki

### Security Enhancements
- Environment variables for secrets (.env files)
- HTTPS/SSL certificates (Let's Encrypt)
- CORS configuration
- Rate limiting (Django Ratelimit)
- Two-Factor Authentication (django-otp)
- Content Security Policy headers
- SQL injection prevention (Django ORM)
- XSS protection

---

## ✨ Features

### Current Features

#### 1. User Management
- **Registration:** New user account creation
- **Login/Logout:** Secure authentication
- **Session Management:** Django sessions

#### 2. Complaint System
- **File Complaint:** Submit crime reports with details
- **Email Notification:** Auto-send complaint details to admin
- **Fields:**
  - Full Name
  - Email Address
  - Phone Number
  - Subject
  - Description/Message

#### 3. Status Tracking
- Check complaint status (planned feature)
- Search by phone number

#### 4. Location Services
- Search locations by address
- Interactive map display using Folium
- Geocoding with OpenStreetMap
- Marker placement on maps

#### 5. News Feed
- Real-time news from BBC News & The Verge
- Display news title, description, and image
- Powered by NewsAPI

#### 6. User Interface
- Responsive design
- Mobile-friendly navigation
- Bootstrap styling
- Font Awesome icons

---

### 🎯 Planned Feature Expansions

#### Phase 1: Core Improvements (Priority: High)

##### 1.1 Advanced Complaint Management
- **Evidence Upload System**
  - Support for images (JPG, PNG, HEIC)
  - Video files (MP4, MOV) up to 100MB
  - Documents (PDF, DOCX)
  - Multiple file attachments per complaint
  - Thumbnail generation for media files
  - Secure cloud storage (S3/MinIO)

- **Complaint Types & Categories**
  - Theft/Burglary
  - Assault/Violence
  - Cybercrime
  - Fraud/Scam
  - Domestic Violence
  - Missing Person
  - Traffic Violations
  - Other

- **Severity Levels**
  - Emergency (immediate response)
  - High Priority
  - Medium Priority
  - Low Priority

- **Anonymous Reporting**
  - Optional anonymous mode
  - Protected identity for sensitive cases
  - Secure communication channel

- **Multi-step Form Wizard**
  - Step 1: Basic Information
  - Step 2: Incident Details
  - Step 3: Location & Time
  - Step 4: Evidence Upload
  - Step 5: Review & Submit
  - Progress indicator
  - Save as draft functionality

##### 1.2 Enhanced Status Tracking
- **Real-time Updates**
  - WebSocket integration for live updates
  - Status change timeline view
  - Detailed action history

- **Status Types**
  - Submitted
  - Under Review
  - Assigned to Officer
  - Investigation in Progress
  - Resolved
  - Closed
  - Rejected (with reason)

- **Notification System**
  - Email notifications on status change
  - SMS alerts (Twilio integration)
  - Push notifications (web & mobile)
  - In-app notification center

- **Complaint Receipt**
  - Auto-generated complaint number
  - QR code for quick tracking
  - PDF receipt download
  - Digital signature

##### 1.3 Interactive Crime Map Dashboard
- **Heatmap Visualization**
  - Color-coded crime density
  - Real-time data updates
  - Cluster markers for performance
  - PostGIS spatial queries

- **Advanced Filters**
  - Date range picker
  - Crime type selection
  - Severity level filter
  - Time of day filter
  - Area/neighborhood selection

- **Crime Statistics Overlay**
  - Total crimes in area
  - Trend indicators (increasing/decreasing)
  - Comparison with previous periods
  - Safety score for neighborhoods

- **Map Features**
  - Police station locations
  - Hospital locations
  - Safe zones
  - High-risk areas
  - Street view integration

##### 1.4 User Dashboard
- **My Complaints**
  - List all filed complaints
  - Filter by status/date
  - Sort by priority
  - Search functionality
  - Bulk actions

- **Profile Management**
  - Update personal information
  - Change password
  - Email preferences
  - Phone number verification
  - Address management

- **Analytics & Insights**
  - Total complaints filed
  - Resolution rate
  - Average response time
  - Personal crime safety score
  - Area crime trends

- **Document Center**
  - Download complaint receipts
  - View uploaded evidence
  - Access official responses
  - Export data (CSV, PDF)

##### 1.5 Admin Panel (Officers & Authorities)
- **Complaint Management Dashboard**
  - Queue view (pending, assigned, resolved)
  - Priority sorting
  - Search and filter
  - Bulk assignment
  - Quick actions (approve, reject, close)

- **Officer Assignment System**
  - Assign complaints to officers
  - Workload balancing
  - Officer availability status
  - Performance tracking

- **Case Management**
  - Add investigation notes
  - Update status with comments
  - Upload additional evidence
  - Request more information from complainant
  - Close case with resolution report

- **Analytics Dashboard**
  - Real-time statistics
  - Crime trends (charts & graphs)
  - Response time metrics
  - Resolution rate by category
  - Geographic crime distribution
  - Officer performance metrics
  - Export reports (Excel, PDF)

- **User Management**
  - View all registered users
  - Suspend/activate accounts
  - Role management (admin, officer, citizen)
  - Activity logs

#### Phase 2: Advanced Features (Priority: Medium)

##### 2.1 Multi-language Support
- **Languages**
  - English (default)
  - Hindi
  - Regional languages (Tamil, Telugu, Bengali, etc.)
  - Auto-detection based on browser locale

- **Implementation**
  - Django i18n framework
  - Translation files (.po, .mo)
  - React i18next for frontend
  - RTL support for certain languages

##### 2.2 Two-Factor Authentication (2FA)
- **Methods**
  - SMS OTP (Twilio)
  - Email OTP
  - Google Authenticator (TOTP)
  - Backup codes

- **Security**
  - Mandatory 2FA for officers/admins
  - Optional for citizens
  - Remember device option (30 days)

##### 2.3 Crime Analytics & Insights
- **Public Dashboard**
  - Crime statistics by area
  - Monthly/yearly trends
  - Crime type distribution
  - Peak crime hours/days
  - Safety index by neighborhood

- **Predictive Analytics**
  - Crime hotspot prediction
  - Seasonal pattern analysis
  - Risk assessment for areas
  - AI/ML-based forecasting

- **Data Visualization**
  - Interactive charts (line, bar, pie)
  - Time series analysis
  - Geographic distribution maps
  - Comparison tools

##### 2.4 Advanced Search & Filtering
- **Global Search**
  - Search complaints by keyword
  - Filter by multiple criteria
  - Saved search queries
  - Search history

- **Smart Filters**
  - Faceted search
  - Auto-suggestions
  - Related complaints
  - Similar incidents in area

##### 2.5 Document Management
- **Evidence Repository**
  - Organized folder structure
  - Version control for files
  - Access permissions
  - Audit trail (who accessed when)
  - Watermarking for sensitive files

- **OCR Integration**
  - Extract text from images
  - Search within uploaded documents
  - Auto-categorization

#### Phase 3: Extended Features (Priority: Nice to Have)

##### 3.1 Mobile Application
- **Platform:** React Native
- **Features:**
  - All web features
  - Camera integration for evidence
  - GPS auto-location
  - Push notifications
  - Offline mode (sync when online)
  - Biometric authentication

##### 3.2 AI Chatbot Support
- **Capabilities:**
  - Answer FAQs
  - Guide through complaint filing
  - Check complaint status
  - Provide safety tips
  - Multi-language support

- **Integration:**
  - Dialogflow / Rasa
  - WhatsApp Business API
  - Telegram Bot API
  - Web chat widget

##### 3.3 Community Features
- **Neighborhood Watch**
  - Create/join local groups
  - Share safety alerts
  - Discussion forums
  - Community moderators

- **Safety Alerts**
  - Real-time crime alerts in area
  - Push notifications
  - Alert radius configuration
  - Alert categories

- **Verified Witnesses**
  - Request witness testimonials
  - Identity verification
  - Anonymous witness option
  - Testimony recording

##### 3.4 Integration with Government Systems
- **Police Database API**
  - Auto-sync with official records
  - Case number mapping
  - Status synchronization

- **E-FIR Generation**
  - Convert complaint to official FIR
  - Digital signature
  - Legal validity
  - Court-ready format

- **Court Case Tracking**
  - Link to court proceedings
  - Hearing dates
  - Case status updates

##### 3.5 Video Features
- **Live Video Filing**
  - Video call with officer
  - Record statement
  - Screen sharing for evidence
  - WebRTC integration

- **Video Evidence Upload**
  - Direct video recording
  - Video compression
  - Timestamp verification
  - Secure streaming

##### 3.6 Blockchain Integration
- **Evidence Chain of Custody**
  - Immutable evidence log
  - Timestamp proof
  - Tamper detection
  - Cryptographic signatures

- **Implementation:**
  - Ethereum or Hyperledger
  - Smart contracts for workflow
  - Decentralized storage (IPFS)

##### 3.7 Advanced Geospatial Features
- **Route Tracking**
  - Track suspect movement patterns
  - Vehicle tracking
  - Historical location data

- **Geofencing**
  - Alert when entering high-crime zones
  - Automatic location tagging
  - Area-based notifications

- **3D Mapping**
  - Building-level crime data
  - Floor-wise incidents
  - 3D visualization

##### 3.8 Reporting & Export
- **Custom Reports**
  - Report builder
  - Scheduled reports
  - Email delivery
  - Template library

- **Data Export Formats**
  - Excel (XLSX)
  - PDF with charts
  - CSV for data analysis
  - JSON for API integration

- **Compliance Reports**
  - Government mandated formats
  - Audit reports
  - Legal documentation

---

## 📦 Installation Guide

### Prerequisites

Before starting, ensure you have the following installed:

```bash
# Check Python version (should be 3.8+)
python3 --version

# Check pip
pip --version

# Check git
git --version
```

### Step 1: Clone the Repository

```bash
# Navigate to your desired directory
cd ~/projects

# Clone the repository
git clone <repository-url>
cd crime_report

# Or if already cloned
cd /home/meliodas/crime_report
```

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate

# Verify activation (should show venv in prompt)
which python
```

### Step 3: Install Python Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install all dependencies from requirements.txt
pip install -r requirements.txt

# Or install manually:
pip install django
pip install django-crispy-forms
pip install crispy-bootstrap4
pip install newsapi-python
pip install folium
pip install geocoder
```

### Step 4: Configure Environment Variables

```bash
# Create .env file
touch .env

# Add the following variables (edit with your values)
cat > .env << EOF
# Django Settings
SECRET_KEY='your-secret-key-here'
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings (for SQLite, no config needed)
# For PostgreSQL (future):
# DATABASE_URL=postgresql://user:password@localhost:5432/crime_report_db

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
EMAIL_PORT=587
EMAIL_USE_TLS=True

# NewsAPI Key
NEWS_API_KEY=your-newsapi-key-here

# Other Settings
TIME_ZONE=UTC
LANGUAGE_CODE=en-us
EOF
```

### Step 5: Update Settings to Use Environment Variables

```bash
# Install python-decouple for environment variables
pip install python-decouple

# Update crime_report/settings.py to use environment variables
# (This step requires code modification - see Migration Plan section)
```

### Step 6: Database Setup

```bash
# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser
# Follow prompts to create admin account
```

### Step 7: Collect Static Files

```bash
# Collect all static files
python manage.py collectstatic --noinput
```

### Step 8: Run Development Server

```bash
# Start Django development server
python manage.py runserver

# Server will start at http://127.0.0.1:8000/
# Admin panel: http://127.0.0.1:8000/admin/
```

### Step 9: Verify Installation

Open your browser and test:

1. **Homepage:** http://127.0.0.1:8000/
2. **Admin:** http://127.0.0.1:8000/admin/ (login with superuser)
3. **Register:** http://127.0.0.1:8000/register/
4. **Login:** http://127.0.0.1:8000/login/
5. **Complaint:** http://127.0.0.1:8000/complaint/ (requires login)
6. **News:** http://127.0.0.1:8000/news/
7. **Location:** http://127.0.0.1:8000/location_search/

### Step 10: Load Sample Data (Optional)

```bash
# Create sample data fixtures
python manage.py dumpdata > initial_data.json

# Load sample data
python manage.py loaddata initial_data.json
```

---

## 🔄 Migration Plan (Current to Recommended Stack)

### Phase 1: Backend Modernization

#### Step 1.1: Upgrade Django (3.2.4 → 5.1)

```bash
# Update requirements.txt
cat > requirements.txt << EOF
# Core
Django==5.1.0
python-decouple==3.8

# Django Extensions
django-crispy-forms==2.1
crispy-bootstrap5==0.7
django-cors-headers==4.3.1
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.1
drf-spectacular==0.27.0

# Database
psycopg2-binary==2.9.9  # PostgreSQL adapter
dj-database-url==2.1.0

# Async Tasks
celery==5.3.4
redis==5.0.1
django-celery-beat==2.5.0
django-celery-results==2.5.1

# File Storage
boto3==1.34.0  # AWS S3
django-storages==1.14.2

# Security
django-otp==1.3.0
qrcode==7.4.2

# APIs & External Services
newsapi-python==0.2.7
folium==0.15.1
geocoder==1.38.1

# Utilities
Pillow==10.2.0  # Image processing
python-dotenv==1.0.0

# Production
gunicorn==21.2.0
whitenoise==6.6.0  # Static files

# Development
django-debug-toolbar==4.2.0
EOF

# Install updated dependencies
pip install -r requirements.txt
```

#### Step 1.2: Update Django Settings

```python
# crime_report/settings.py - Updated version
from pathlib import Path
from decouple import config
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1').split(',')

# Application definition
INSTALLED_APPS = [
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'crispy_forms',
    'crispy_bootstrap5',
    'drf_spectacular',
    'django_celery_beat',
    'django_celery_results',
    
    # Local apps
    'complaint.apps.ComplaintConfig',
    'location.apps.LocationConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Static files
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React dev server
    "http://127.0.0.1:3000",
]

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default=f'sqlite:///{BASE_DIR}/db.sqlite3')
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Celery Configuration
CELERY_BROKER_URL = config('REDIS_URL', default='redis://localhost:6379/0')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = config('TIME_ZONE', default='UTC')

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
```

#### Step 1.3: Create Django REST API

```bash
# Create API app
python manage.py startapp api

# Create API views, serializers, urls
# (See detailed code in Migration Plan section)
```

#### Step 1.4: Migrate to PostgreSQL

```bash
# Install PostgreSQL
# Ubuntu/Debian:
sudo apt update
sudo apt install postgresql postgresql-contrib postgis

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Create database
sudo -u postgres psql
CREATE DATABASE crime_report_db;
CREATE USER crime_admin WITH PASSWORD 'secure_password';
ALTER ROLE crime_admin SET client_encoding TO 'utf8';
ALTER ROLE crime_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE crime_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE crime_report_db TO crime_admin;
\q

# Update .env
DATABASE_URL=postgresql://crime_admin:secure_password@localhost:5432/crime_report_db

# Migrate data from SQLite to PostgreSQL
python manage.py dumpdata > data_backup.json
python manage.py migrate
python manage.py loaddata data_backup.json
```

### Phase 2: Frontend Migration to React

#### Step 2.1: Create React App

```bash
# Navigate to project root
cd /home/meliodas/crime_report

# Create React app with Vite
npm create vite@latest frontend -- --template react-ts

# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Install additional packages
npm install axios react-router-dom react-query zustand
npm install react-leaflet leaflet react-hook-form zod
npm install @tanstack/react-query tailwindcss postcss autoprefixer
npm install react-hot-toast lucide-react

# Initialize Tailwind CSS
npx tailwindcss init -p
```

#### Step 2.2: Setup Tailwind CSS

```javascript
// tailwind.config.js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

```css
/* src/index.css */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

#### Step 2.3: Project Structure

```
frontend/
├── public/
├── src/
│   ├── api/               # API calls
│   ├── components/        # Reusable components
│   │   ├── common/        # Common UI components
│   │   ├── layout/        # Layout components
│   │   └── features/      # Feature-specific components
│   ├── pages/             # Page components
│   │   ├── Home.tsx
│   │   ├── Login.tsx
│   │   ├── Register.tsx
│   │   ├── Complaint.tsx
│   │   ├── Dashboard.tsx
│   │   ├── Status.tsx
│   │   ├── LocationSearch.tsx
│   │   └── News.tsx
│   ├── hooks/             # Custom hooks
│   ├── store/             # Zustand store
│   ├── types/             # TypeScript types
│   ├── utils/             # Utility functions
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css
├── package.json
└── vite.config.ts
```

#### Step 2.4: Configure API Integration

```typescript
// src/api/client.ts
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for auth token
apiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor for token refresh
apiClient.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      try {
        const refreshToken = localStorage.getItem('refresh_token');
        const { data } = await axios.post(`${API_BASE_URL}/token/refresh/`, {
          refresh: refreshToken,
        });
        
        localStorage.setItem('access_token', data.access);
        originalRequest.headers.Authorization = `Bearer ${data.access}`;
        
        return apiClient(originalRequest);
      } catch (err) {
        localStorage.clear();
        window.location.href = '/login';
      }
    }
    
    return Promise.reject(error);
  }
);
```

### Phase 3: Docker Setup

#### Step 3.1: Create Docker Configuration

```dockerfile
# Dockerfile (Backend)
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Create media and static directories
RUN mkdir -p /app/media /app/staticfiles

# Run migrations and collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "crime_report.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
```

```dockerfile
# Dockerfile.frontend
FROM node:18-alpine AS builder

WORKDIR /app
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  db:
    image: postgis/postgis:15-3.3
    environment:
      POSTGRES_DB: crime_report_db
      POSTGRES_USER: crime_admin
      POSTGRES_PASSWORD: secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

  backend:
    build: .
    command: gunicorn crime_report.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db
      - redis

  celery:
    build: .
    command: celery -A crime_report worker -l info
    volumes:
      - .:/app
    env_file:
      - .env
    depends_on:
      - db
      - redis

  celery-beat:
    build: .
    command: celery -A crime_report beat -l info
    volumes:
      - .:/app
    env_file:
      - .env
    depends_on:
      - db
      - redis

  frontend:
    build:
      context: .
      dockerfile: Dockerfile.frontend
    ports:
      - "3000:80"
    depends_on:
      - backend

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

#### Step 3.2: Run with Docker

```bash
# Build and start all services
docker-compose up -d --build

# Run migrations
docker-compose exec backend python manage.py migrate

# Create superuser
docker-compose exec backend python manage.py createsuperuser

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes (WARNING: deletes data)
docker-compose down -v
```

---

## 📚 API Documentation

### Authentication Endpoints

#### Register User
```http
POST /api/auth/register/
Content-Type: application/json

{
  "username": "john_doe",
  "email": "john@example.com",
  "password": "SecurePass123!",
  "password2": "SecurePass123!"
}

Response: 201 Created
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "message": "User registered successfully"
}
```

#### Login (Get JWT Token)
```http
POST /api/auth/login/
Content-Type: application/json

{
  "username": "john_doe",
  "password": "SecurePass123!"
}

Response: 200 OK
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "user": {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
  }
}
```

#### Refresh Token
```http
POST /api/auth/token/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}

Response: 200 OK
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Complaint Endpoints

#### Create Complaint
```http
POST /api/complaints/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "phonenumber": "1234567890",
  "subject": "Theft reported",
  "description": "My bike was stolen from parking lot..."
}

Response: 201 Created
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phonenumber": "1234567890",
  "subject": "Theft reported",
  "description": "My bike was stolen...",
  "created_at": "2024-03-20T10:30:00Z",
  "status": "submitted"
}
```

#### List Complaints
```http
GET /api/complaints/
Authorization: Bearer {access_token}

Response: 200 OK
{
  "count": 25,
  "next": "http://localhost:8000/api/complaints/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "John Doe",
      "subject": "Theft reported",
      "status": "submitted",
      "created_at": "2024-03-20T10:30:00Z"
    },
    ...
  ]
}
```

#### Get Complaint Detail
```http
GET /api/complaints/{id}/
Authorization: Bearer {access_token}

Response: 200 OK
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "phonenumber": "1234567890",
  "subject": "Theft reported",
  "description": "My bike was stolen...",
  "created_at": "2024-03-20T10:30:00Z",
  "updated_at": "2024-03-20T10:30:00Z",
  "status": "submitted"
}
```

### Location Endpoints

#### Search Location
```http
POST /api/locations/search/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "address": "Times Square, New York"
}

Response: 200 OK
{
  "address": "Times Square, New York",
  "latitude": 40.7580,
  "longitude": -73.9855,
  "country": "United States",
  "map_url": "/api/locations/map/Times%20Square,%20New%20York/"
}
```

### News Endpoints

#### Get News Feed
```http
GET /api/news/
Authorization: Bearer {access_token}

Response: 200 OK
{
  "articles": [
    {
      "title": "Breaking News...",
      "description": "News description...",
      "url": "https://...",
      "urlToImage": "https://...",
      "publishedAt": "2024-03-20T10:00:00Z",
      "source": {
        "name": "BBC News"
      }
    },
    ...
  ]
}
```

### Full API Documentation

Once the backend is running with DRF Spectacular:

- **Swagger UI:** http://localhost:8000/api/schema/swagger-ui/
- **ReDoc:** http://localhost:8000/api/schema/redoc/
- **OpenAPI Schema:** http://localhost:8000/api/schema/

---

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Use strong `SECRET_KEY`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use PostgreSQL (not SQLite)
- [ ] Set up HTTPS/SSL certificates
- [ ] Configure static file serving (WhiteNoise or CDN)
- [ ] Set up email service (SendGrid, AWS SES)
- [ ] Configure Redis for caching
- [ ] Set up Celery for async tasks
- [ ] Enable logging and monitoring (Sentry)
- [ ] Set up automated backups
- [ ] Configure firewall and security groups
- [ ] Use environment variables for all secrets
- [ ] Set up CI/CD pipeline
- [ ] Configure rate limiting
- [ ] Enable CORS properly
- [ ] Set up domain and DNS

### Deployment Options

#### Option 1: Traditional VPS (DigitalOcean, Linode, AWS EC2)

```bash
# 1. Update system
sudo apt update && sudo apt upgrade -y

# 2. Install dependencies
sudo apt install python3-pip python3-venv postgresql nginx redis-server

# 3. Clone repository
git clone <repo-url> /var/www/crime_report
cd /var/www/crime_report

# 4. Set up virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 5. Set up PostgreSQL database
sudo -u postgres psql
CREATE DATABASE crime_report_db;
CREATE USER crime_admin WITH PASSWORD 'strong_password';
GRANT ALL PRIVILEGES ON DATABASE crime_report_db TO crime_admin;

# 6. Configure environment variables
cp .env.example .env
nano .env  # Edit with production values

# 7. Run migrations
python manage.py migrate
python manage.py collectstatic

# 8. Set up Gunicorn systemd service
sudo nano /etc/systemd/system/gunicorn.service

# 9. Set up Nginx
sudo nano /etc/nginx/sites-available/crime_report

# 10. Enable and start services
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl enable nginx
sudo systemctl restart nginx

# 11. Set up SSL with Let's Encrypt
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

#### Option 2: Docker Deployment

```bash
# Use docker-compose.prod.yml
docker-compose -f docker-compose.prod.yml up -d
```

#### Option 3: Platform as a Service (Heroku, Railway, Render)

```bash
# Example for Heroku
heroku login
heroku create crime-report-app
heroku addons:create heroku-postgresql:hobby-dev
heroku addons:create heroku-redis:hobby-dev
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

#### Option 4: Serverless (AWS Lambda, Google Cloud Functions)

- Use Zappa for Django on AWS Lambda
- Configure API Gateway
- Use RDS for database
- Use S3 for static/media files

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test complaint

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Generate HTML report
```

### Frontend Tests

```bash
cd frontend
npm run test
npm run test:coverage
```

---

## 🤝 Contributing

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/AmazingFeature`
3. **Commit your changes:** `git commit -m 'Add some AmazingFeature'`
4. **Push to the branch:** `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Coding Standards

- Follow PEP 8 for Python code
- Use ESLint and Prettier for JavaScript/TypeScript
- Write meaningful commit messages
- Add tests for new features
- Update documentation
- Keep PRs focused and small

### Git Workflow

```bash
# 1. Sync with main branch
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/new-feature

# 3. Make changes and commit
git add .
git commit -m "feat: add new feature"

# 4. Push to remote
git push origin feature/new-feature

# 5. Create Pull Request on GitHub

# 6. After merge, delete branch
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Authors & Contributors

- **Original Developer:** [Your Name]
- **Contributors:** [List contributors]

---

## 🆘 Support

For support and questions:

- **Email:** support@crimereport.com
- **Documentation:** https://docs.crimereport.com
- **Issues:** https://github.com/yourrepo/crime_report/issues

---

## 📝 Changelog

### Version 2.0.0 (Planned)
- React frontend
- Django 5.1 upgrade
- PostgreSQL database
- REST API
- Docker support

### Version 1.0.0 (Current)
- Basic complaint system
- User authentication
- Location search
- News feed
- Email notifications

---

## 🔐 Security

### Reporting Security Issues

If you discover a security vulnerability, please email security@crimereport.com instead of using the issue tracker.

### Security Best Practices

1. Never commit secrets or API keys
2. Use environment variables for sensitive data
3. Keep dependencies updated
4. Enable HTTPS in production
5. Use strong passwords
6. Enable 2FA for admin accounts
7. Regular security audits
8. Monitor application logs
9. Implement rate limiting
10. Use Content Security Policy headers

---

## 🎓 Resources

### Documentation
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

### Tutorials
- [Django for Beginners](https://djangoforbeginners.com/)
- [React Tutorial](https://react.dev/learn)
- [REST API Design](https://restfulapi.net/)

### Community
- [Django Forum](https://forum.djangoproject.com/)
- [React Community](https://react.dev/community)
- [Stack Overflow](https://stackoverflow.com/)

---

## 🙏 Acknowledgments

- Django Software Foundation
- React team
- Bootstrap team
- All open-source contributors
- NewsAPI for news integration
- OpenStreetMap for mapping services

---

**Built with ❤️ for safer communities**
