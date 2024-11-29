# ASD Detection Web Application

## Project Overview
An advanced web application designed to assist in preliminary screening for Autism Spectrum Disorder (ASD) through machine learning-powered image analysis.

## Project Structure Breakdown

### 1. Backend (Python Flask)
- **Location**: `backend/main.py`
- **Functionality**: 
  - Handles API endpoint for image detection
  - Loads machine learning model
  - Processes image input
  - Returns ASD detection probability
- **Key Technologies**: 
  - Flask for web server
  - TensorFlow for ML model handling
  - OpenCV for image processing

### 2. Frontend (Web Interface)
- **Location**: `frontend/` directory
- **Components**:
  - `index.html`: User interface structure
  - `app.js`: Client-side interaction logic
  - `styles.css`: Responsive design styling
- **Features**:
  - Image upload functionality
  - Real-time preview
  - Detection result visualization
  - Interactive user experience

### 3. Machine Learning Model
- **Location**: `ml_models/model.h5`
- **Current State**: Dummy placeholder model
- **Requirements**:
  - Professional, trained ASD detection model
  - Binary classification output
  - Trained on validated medical image datasets

### 4. Testing
- **Backend Tests**: `tests/test_backend.py`
  - Validates API endpoints
  - Checks model loading
  - Ensures basic functionality
- **Frontend Tests**: `tests/test_frontend.py`
  - Validates UI components
  - Checks user interaction flows
  - Selenium-based UI testing

## Prerequisites
- Python 3.8+
- Modern web browser
- Stable internet connection

## Technical Dependencies
- Web Frameworks: Flask
- Machine Learning: TensorFlow, NumPy
- Image Processing: OpenCV
- Frontend: Vanilla JavaScript
- Testing: Selenium WebDriver

## Installation Steps

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/asd-detection-app.git
cd asd-detection-app
```

### 2. Setup Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Unix/macOS
# OR
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Generate Dummy Model (Optional)
```bash
python ml_models/model_generator.py
```

### 5. Run Backend Server
```bash
python backend/main.py
```

## Running Tests
```bash
# Run all tests
python -m unittest discover tests
```

## Important Ethical Considerations
- This application is a SCREENING tool, NOT a diagnostic instrument
- Always consult healthcare professionals for definitive diagnosis
- Respect patient privacy and data protection guidelines
- Continuous model improvement required

## Future Enhancements
- Integrate professional medical datasets
- Improve ML model accuracy
- Add more comprehensive detection metrics
- Implement secure data handling
- Create more intuitive UI/UX

## Contribution Guidelines
1. Fork the repository
2. Create feature branches
3. Submit pull requests
4. Follow coding standards
5. Update documentation

## Licensing
[Specify your licensing terms]

## Acknowledgments
- Medical professionals involved in dataset creation
- Open-source community
- Machine learning researchers in ASD detection
