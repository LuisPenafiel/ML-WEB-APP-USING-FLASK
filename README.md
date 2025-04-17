# Iris Flower Classification Web App

A Flask web application that predicts Iris flower species (Setosa, Versicolor, Virginica) based on sepal and petal measurements using a pre-trained machine learning model.

## Features

- User-friendly interface for flower measurements
- Real-time species prediction (Setosa, Versicolor, Virginica)
- Input validation and error handling
- Responsive design for all devices
- Pre-configured Dev Container for VS Code

## Project Structure
```markdown
ML-WEB-APP-USING-FLASK/
├── .devcontainer/ # Dev container configuration
├── .vscode/ # VS Code settings
├── data/ # Dataset files
├── src/ # Main application
│ ├── templates/ # HTML templates
│ │ └── index.html # Frontend
│ ├── hello.py # Flask app
│ ├── iris_model_LR.pkl # Pre-trained model
│ └── requirements.txt # Dependencies
├── .gitignore # Git ignore rules
└── README.md # Documentation
```

##  Quick Setup

### Using VS Code Dev Container (Recommended)
1. Open project in VS Code
2. Click "Reopen in Container" when prompted
3. The container will automatically:
   - Set up Python 3.11 environment
   - Install required extensions
   - Install all dependencies

### Manual Installation
```bash
# Clone repository
git clone https://github.com/your-username/ML-WEB-APP-USING-FLASK.git
cd ML-WEB-APP-USING-FLASK

# Install dependencies
pip install -r src/requirements.txt

# Run application
python src/hello.py

```

## 📋 Usage Guide

1. Enter flower measurements:
   - Sepal Length (4.3-7.9 cm)
   - Sepal Width (2.0-4.4 cm)
   - Petal Length (1.0-7.0 cm)
   - Petal Width (0.1-2.5 cm)

2. Click "Predict" to see the species prediction
3. Use "Reset" to clear all fields

## ℹ️ Important Notes

- The model expects input values in centimeters
- Input ranges are validated before prediction
- Model path is set to `src/iris_model_LR.pkl`
- Runs on `0.0.0.0:5000` for container compatibility
- All dependencies are listed in `src/requirements.txt`

## 📜 License
MIT License - Free to use and modify