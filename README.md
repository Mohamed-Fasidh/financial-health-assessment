#  Financial Health Assessment Tool for SMEs

A full-stack financial health assessment platform designed for **Small and Medium Enterprises (SMEs)**. The application analyzes uploaded financial documents and business data to provide **financial health scores, risk analysis, working capital insights, GST compliance status, and loan recommendations** in a simple, non-technical interface.

---

##  Live Demo

```
https://financial-health-assessment-mohamed-fasidhs-projects.vercel.app/
```

---
Note: The backend is deployed on Render free tier. 
Due to cold start behavior, the first API request after inactivity may take up to 60 seconds. 
Subsequent requests respond instantly.


##  Problem Statement

SMEs often struggle to understand their financial health due to lack of financial expertise and fragmented data. This project solves that problem by **automating financial analysis** and presenting **actionable insights** in a clear and visual manner.

---

## Project Description

The platform evaluates SME financial health by analyzing uploaded financial documents (CSV/XLSX/PDF), computing working capital, credit risk score, and loan eligibility. Results are securely stored in PostgreSQL and presented via a simple React dashboard.

##  Features

* Upload and analyze **CSV / XLSX / PDF (text-based)** financial documents
* Financial health **score calculation**
* Cash flow and **working capital analysis**
* **Loan eligibility recommendations** (MSME / bank readiness)
* **GST compliance check** via API
* Industry-agnostic architecture
* Clean and intuitive UI for non-finance users
* Secure backend with **HTTPS & encrypted storage**

---

##  Functional Coverage Mapping

| Requirement                 | Status                          |
| --------------------------- | ------------------------------- |
| CSV / XLSX upload           |  Implemented                   |
| PDF upload (text-based)     |  Implemented                   |
| Financial health score      |  Implemented                   |
| Risk detection              |  Implemented                   |
| Working capital analysis    |  Implemented                   |
| Loan recommendations        |  Implemented                   |
| Industry-ready architecture |  Implemented                   |
| HTTPS encryption            |  Implemented                   |
| Encrypted DB volume         |  Implemented                   |

---

##  Architecture Overview

```
Frontend (React.js)
   |
   | HTTPS (NGINX Reverse Proxy)
   |
Backend (FastAPI - Python)
   |
   | Pandas Processing
   |
PostgreSQL (Encrypted Volume)
```

---

##  Tech Stack

### Frontend

* React.js
* Fetch API
* Custom CSS

### Backend

* FastAPI
* Pandas
* Uvicorn

### Database

* PostgreSQL

### Security

* NGINX reverse proxy
* HTTPS (TLS certificates)
* Encrypted database volumes


---

##  Project Structure

```
Financial_Health_Assessment_Tool/
├── frontend/
│   ├── src/
│   ├── package.json
│   └── Dockerfile
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── services/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   ├── nginx.conf
│   └── certs/
│
├── docker-compose.yml
└── README.md
```

---

##  API Endpoints

### Upload Financial File

```
POST /upload/
```

Accepts: CSV, XLSX, PDF
Returns: Revenue, Expenses, Score, Insights

---

### Analyze Financial Health (JSON)

```
POST /finance/analyze
```

---

### GST Compliance Check

```
GET /gst/{gstin}
```

---

##  Run Locally (Recommended – Docker)

### Prerequisites

* Docker Desktop
* Docker Compose

### Step 1: Clone Repository

```bash
git clone https://github.com/Mohamed-Fasidh/financial-health-assessment
cd financial-health-assessment-tool
```

### Step 2: Start All Services

```bash
docker-compose up --build
```

### Step 3: Access Application

```
Frontend: http://localhost:3000
Backend API: http://localhost:8000/docs
```

---

##  Run Locally (Without Docker)

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

##  Security Implementation

* HTTPS via NGINX reverse proxy
* TLS certificates for encrypted traffic
* PostgreSQL data stored in encrypted Docker volume
* CORS protection enabled
* Environment-based configuration

---

##  Demo Video

> *(Add after recording)*

```
https://youtu.be/your-demo-video
```

---

##  Sample Files

* `sme_financials.csv`
* `sme_financials.xlsx`
* `sme_financials.pdf`

---

##  Future Enhancements

* Real GST API integration
* Real banking API integrations (Account Aggregator)
* Multilingual UI (Hindi / Regional languages)
* Advanced forecasting (time-series)
* AI narrative via GPT / Claude
* Investor-ready PDF report generation

---
