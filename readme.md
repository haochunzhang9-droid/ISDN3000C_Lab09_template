Here’s a **complete English README.md** tailored for your project setup. It includes overview, structure, setup instructions, configuration, and troubleshooting so that tutors/graders can easily understand and run your work:

---

# Flask + Nginx + Docker Compose Project

## Overview
This project demonstrates how to deploy a simple **Flask** web application using **Gunicorn** inside a Docker container, with **Nginx** acting as a reverse proxy for production-level performance.  
The setup is orchestrated with **Docker Compose**, which manages multiple services (Flask app container + Nginx container) and ensures smooth networking between them.  
Static files (CSS, JavaScript, images) are served directly by Nginx for efficiency.

---

## Project Structure
```
ISDN3000C_Lab09_template/
├── .gitignore            # Ignore rules (exclude venv, cache, etc.)
├── Dockerfile            # Build instructions for Flask app container
├── docker-compose.yml    # Multi-container orchestration (Flask + Nginx)
├── questions.md          # Answers to lab questions
├── readme.md             # Project documentation
├── requirements.txt      # Python dependencies
├── default.conf          # Nginx site configuration
├── nginx/
│   └── nginx.conf        # Main Nginx configuration file
└── FlaskApp/
    ├── app.py            # Flask application entry point
    ├── init_db.py        # Database initialization script
    ├── schema.sql        # SQL schema for database setup
    ├── database.db       # SQLite database file
    ├── guestbook.db      # Guestbook database file
    └── templates/
        └── index.html    # HTML template for the web interface
```

---

## Requirements
- Docker (>= 20.x)
- Docker Compose (>= v2.x)
- Python 3.11 (optional, for local development)

---

## Setup Instructions

### 1. Build and start containers
```bash
docker-compose up --build
```

### 2. Access the application
- Flask app via Nginx:
  ```
  http://localhost:8080
  ```
- Static files served directly by Nginx:
  ```
  http://localhost:8080/static/style.css
  ```

---

## Nginx Configuration
Example `default.conf`:
```nginx
server {
    listen 80;

    # Serve static files directly
    location /static {
        alias /app/static;
        expires 30d;
        access_log off;
    }

    # Proxy all other requests to Flask
    location / {
        proxy_pass http://flask:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## Common Issues

- **Port conflict**  
  If `8080` is already in use, change the port mapping in `docker-compose.yml`:
  ```yaml
  ports:
    - "8081:80"
  ```
  Then access the app at `http://localhost:8081`.

- **Configuration file mount error**  
  Ensure `default.conf` exists in the project directory and is mounted correctly:
  ```yaml
  - ./default.conf:/etc/nginx/conf.d/default.conf
  ```

- **Do not commit virtual environments**  
  Make sure `.gitignore` excludes `venv/` or `FlaskVenv/` directories.

---

## Summary
This project illustrates a production-ready deployment workflow:
- Flask app container runs application logic with Gunicorn.  
- Nginx container acts as reverse proxy and static file server.  
- Docker Compose manages multi-container orchestration.  

---

SHEN Yuming 20945165

ZHANG Haochun 21147459
