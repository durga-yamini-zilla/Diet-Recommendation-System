# 🥗 AI-Powered Diet Recommendation System

## Overview

The **AI-Powered Diet Recommendation System** is a Machine Learning application designed to generate personalized diet recommendations based on an individual's health profile, medical conditions, and dietary preferences.

The system leverages a **Random Forest Classifier** optimized using **GridSearchCV** to improve prediction accuracy and reliability. Users can enter their health-related information through an interactive **Streamlit dashboard** and receive real-time diet recommendations along with explainable insights powered by **SHAP (SHapley Additive Explanations)**.


## Features

- ✅ Personalized diet recommendations
- ✅ Random Forest Classification Model
- ✅ Hyperparameter Optimization using GridSearchCV
- ✅ 5-Fold Cross Validation
- ✅ SHAP Explainable AI Integration
- ✅ Interactive Streamlit Dashboard
- ✅ Real-Time Prediction System
- ✅ Model Persistence using Joblib


## Technology Stack

### Programming Language

- Python

### Machine Learning

- Scikit-Learn
- Random Forest Classifier
- GridSearchCV

### Explainable AI

- SHAP

### Data Processing

- Pandas
- NumPy

### Visualization

- Matplotlib

### Frontend

- Streamlit

### Model Storage

- Joblib


## Project Workflow

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Encoding
   ↓
Random Forest Model
   ↓
GridSearchCV Optimization
   ↓
Model Evaluation
   ↓
Model Saving (Joblib)
   ↓
Streamlit User Interface
   ↓
Diet Recommendation
   ↓
SHAP Explainability
```


## Dataset Features

| Feature | Description |
|----------|-------------|
| Age | User Age |
| Gender | Male/Female |
| Height_cm | Height in Centimeters |
| Weight_kg | Weight in Kilograms |
| BMI | Body Mass Index |
| Disease | Existing Medical Condition |
| Food_Preference | Dietary Preference |
| Calories_Intake | Daily Calorie Intake |
| Recommended_Diet | Target Variable |


## Model Evaluation Metrics

The model performance is evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Cross Validation Accuracy


## Project Structure

```text
Diet-Recommendation-System/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── diet_health_dataset.csv
```


## Installation

Create virtual environment:

```bash
python -m venv venv
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Train the model:

```bash
python train_model.py
```

Run the Streamlit application:

```bash
streamlit run app.py
```

<!-- --- -->

<!-- ## Future Improvements

- FastAPI Integration
- Cloud Deployment (AWS/GCP/Azure)
- User Authentication System
- Recommendation History Tracking
- Advanced Nutrition Analysis
- Deep Learning-Based Recommendation Models
- Mobile Application Support -->


## Learning Outcomes

This project demonstrates practical knowledge of:

- Machine Learning Fundamentals
- Classification Algorithms
- Hyperparameter Tuning
- Explainable AI (XAI)
- Streamlit Application Development
- Model Persistence and Deployment Concepts
- Data Preprocessing Techniques
- Model Evaluation and Validation
