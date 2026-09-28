[readme.md](https://github.com/user-attachments/files/32758030/readme.md)
# DevDesk: Campus IT & Lab Support Register

A lightweight, containerized helpdesk ticketing system for campus IT and computer lab support, backed by an automated CI/CD pipeline and AWS EC2 deployment.

---

## 🚀 Live Links & Access
* **Live Web Application:** [http://13.49.145.51:5000](http://13.49.145.51:5000)
* **Jenkins Automation Dashboard:** `http://13.49.145.51:8080`
* **Health Endpoint:** [http://13.49.145.51:5000/health](http://13.49.145.51:5000/health)

---

## 📌 Project Overview
DevDesk streamlines the reporting and tracking of hardware/software issues across university computer labs. Built using Python (Flask) and HTML/CSS, the application allows students and staff to submit support tickets, view active logs, and verify system status via an automated health endpoint.

---

## 🏗️ Architecture & CI/CD Pipeline Diagram

The deployment workflow integrates version control, automated testing, containerization, and cloud delivery:

```
[ Developer Commit ] 
        │
        ▼
[ Jenkins Pipeline ] ──► [ Build & Test Stage ] ──► [ Docker Image (`cloud-app`) ]
                                                              │
                                                              ▼
[ AWS EC2 Public Host (Port 5000) ] ◄──(Container Restart & Port Bind)
```

---

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Frontend:** HTML5, CSS3, Jinja Templates
* **Containerization:** Docker
* **CI/CD Automation:** Jenkins
* **Cloud Infrastructure:** AWS EC2 (Ubuntu)

---

## 🏃 Local Setup & Installation

To run this application locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/devdesk-app.git
   cd devdesk-app
   ```

2. **Run with Docker:**
   ```bash
   docker build -t cloud-app .
   docker run -d -p 5000:5000 --name cloud-app cloud-app
   ```

3. **Access the local app:**
   Open your browser and navigate to `http://localhost:5000`.

---

## 🧪 Pipeline Validation & Health Checks
The application exposes an automated health endpoint (`/health`) that returns service runtime metrics:
```json
{
  "status": "ok",
  "commit": "local"
}
```

---

## 👨‍💻 Author
* **Chirayu** 
* **Course Faculty:** Pranati Waghodekar
* **Institution:** MIT World Peace University (MIT-WPU), Pune
