# ASD Detection Web Application

## Project Overview
This web application provides real-time image detection for potential Autism Spectrum Disorder (ASD) indicators using machine learning.

## Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Brijesh5002/dti-asd.git
cd asd-detection-app
```

### 2. Backend Setup
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install dependencies
pip install -r backend/requirements.txt

# Generate dummy model (optional)
python ml_models/model_generator.py
```

### 3. Run the Backend
```bash
python backend/main.py
```

### 4. Frontend
- Open `frontend/index.html` in your web browser

## Running Tests
```bash
# Ensure you have test dependencies
pip install selenium webdriver-manager

# Run backend tests
python -m unittest tests/test_backend.py

# Run frontend tests
python -m unittest tests/test_frontend.py
```

## Important Notes
- This is a prototype implementation
- Replace the dummy model with a professionally trained ASD detection model
- Consult medical professionals for clinical interpretations
