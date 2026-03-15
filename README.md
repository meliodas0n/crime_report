# Database Setup
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

sudo -u postgres psql crime_report_db
CREATE SCHEMA crime_app AUTHORIZATION crime_admin;
ALTER ROLE crime_admin SET search_path TO crime_app;
\dn
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA crime_app TO crime_admin;
\q


# React Install
```bash
npm install axios react-router-dom zustand react-leaflet leaflet react-hook-form zod @tanstack/react-queryreact-hot-toast lucide-react tailwindcss @tailwindcss/vite
```