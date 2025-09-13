---
title: Student Performance Predictor
emoji: 🎓
colorFrom: blue
colorTo: purple
sdk: docker
sdk_version: "latest"
app_file: app.py
pinned: false
license: mit
---

# 🎓 Student Performance Prediction System

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2.1-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A comprehensive machine learning solution that predicts student math performance based on demographic and academic factors using ensemble learning techniques.

## 📋 Table of Contents
- [Overview](#-overview)
- [Problem Statement](#-problem-statement)
- [Dataset](#-dataset)
- [Architecture](#-architecture)
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Performance](#-model-performance)
- [API Endpoints](#-api-endpoints)
- [Project Structure](#-project-structure)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)

## 🎯 Overview

This project implements an end-to-end machine learning pipeline to predict student mathematics performance based on various socio-economic and educational factors. The system uses advanced ensemble learning algorithms and provides a user-friendly web interface for real-time predictions.

### 🔍 Problem Statement

Understanding how student performance in mathematics is influenced by various factors such as:
- **Demographic factors**: Gender, Race/Ethnicity
- **Socio-economic factors**: Lunch type (indicator of economic status)
- **Educational background**: Parental education level, Test preparation course completion
- **Academic performance**: Reading and Writing scores

The goal is to build a robust prediction model that can help educators and institutions identify students who might need additional support.

## 📊 Dataset

**Source**: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)

### Dataset Characteristics:
- **Size**: 1,000 student records
- **Features**: 8 columns (5 categorical, 3 numerical)
- **Target Variable**: `math_score` (0-100)

### Feature Description:
| Feature | Type | Description |
|---------|------|-------------|
| `gender` | Categorical | Student's gender (male/female) |
| `race_ethnicity` | Categorical | Student's ethnic group (A, B, C, D, E) |
| `parental_level_of_education` | Categorical | Highest education level of parents |
| `lunch` | Categorical | Lunch type (standard/free or reduced) |
| `test_preparation_course` | Categorical | Test prep course completion status |
| `reading_score` | Numerical | Reading test score (0-100) |
| `writing_score` | Numerical | Writing test score (0-100) |
| `math_score` | Numerical | **Target** - Mathematics test score (0-100) |

## 🏗️ Architecture

The project follows a modular, production-ready architecture:

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Data Source   │───▶│  Data Ingestion  │───▶│ Data Transform  │
│   (CSV File)    │    │   Component      │    │   Component     │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
┌─────────────────┐    ┌──────────────────┐            │
│  Web Interface  │◀───│  Flask App       │            │
│   (HTML/CSS)    │    │  (Prediction)    │            │
└─────────────────┘    └──────────────────┘            │
                                ▲                       │
                                │                       ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Artifacts     │◀───│  Model Trainer   │◀───│  Preprocessed   │
│ (model.pkl,     │    │   Component      │    │     Data        │
│ preprocessor.pkl)│    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## ✨ Features

### 🤖 Machine Learning Pipeline
- **Data Ingestion**: Automated data loading and train-test splitting
- **Data Transformation**: 
  - Numerical features: Median imputation + Standard scaling
  - Categorical features: Mode imputation + One-hot encoding + Scaling
- **Model Training**: Multi-algorithm comparison with hyperparameter tuning
- **Model Selection**: Automated best model selection based on R² score

### 🧠 Advanced Algorithms
- **Random Forest Regressor**
- **Gradient Boosting Regressor**
- **XGBoost Regressor**
- **CatBoost Regressor**
- **AdaBoost Regressor**
- **Decision Tree Regressor**
- **Linear Regression**

### 🌐 Web Application
- **Modern UI/UX**: Responsive design with gradient styling
- **Real-time Predictions**: Instant math score predictions
- **Form Validation**: Client-side and server-side validation
- **Error Handling**: Comprehensive exception handling with custom logging

### 🔧 Production Features
- **Custom Exception Handling**: Detailed error tracking and logging
- **Logging System**: Timestamped logs for debugging and monitoring
- **Modular Design**: Reusable components for easy maintenance
- **Configuration Management**: Centralized configuration using dataclasses

## 🚀 Installation

### Prerequisites
- Python 3.11+
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yashpinjarkar10/mlproject.git
   cd mlproject
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\\Scripts\\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the project in development mode**
   ```bash
   pip install -e .
   ```

## 💻 Usage

### 🎯 Training the Model

Run the complete ML pipeline (data ingestion → transformation → model training):

```bash
python src/components/data_ingestion.py
```

This will:
- Load and split the dataset (80% train, 20% test)
- Apply data transformations
- Train multiple models with hyperparameter tuning
- Save the best model and preprocessor

### 🌐 Running the Web Application

```bash
python app.py
```

Access the application at: `http://localhost:5000`

### 📝 Making Predictions

1. Navigate to the prediction page
2. Fill in the student information:
   - Personal details (Gender, Ethnicity)
   - Educational background (Parent education, Test prep)
   - Academic scores (Reading & Writing)
3. Click \"Predict Math Score\"
4. View the predicted mathematics score

## 📈 Model Performance

The system automatically selects the best-performing model based on R² score evaluation:

- **Minimum Acceptable Performance**: R² ≥ 0.6
- **Cross-validation**: 3-fold CV during hyperparameter tuning
- **Evaluation Metrics**: R² Score on test set
- **Model Comparison**: Comprehensive evaluation of 7 different algorithms

### Hyperparameter Optimization

Each algorithm undergoes GridSearchCV with algorithm-specific parameter grids:

| Algorithm | Key Parameters Tuned |
|-----------|---------------------|
| Random Forest | `n_estimators`, `max_features` |
| Gradient Boosting | `learning_rate`, `n_estimators`, `subsample` |
| XGBoost | `learning_rate`, `n_estimators` |
| CatBoost | `depth`, `learning_rate`, `iterations` |

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Landing page with project overview |
| `/predictdata` | GET | Display prediction form |
| `/predictdata` | POST | Process prediction request and return result |

### Request Format (POST /predictdata)
```json
{
  \"gender\": \"male\",
  \"ethnicity\": \"group B\",
  \"parental_level_of_education\": \"bachelor's degree\",
  \"lunch\": \"standard\",
  \"test_preparation_course\": \"completed\",
  \"reading_score\": 85,
  \"writing_score\": 78
}
```

## 📁 Project Structure

```
mlproject/
├── 📱 app.py                          # Flask web application
├── 📋 requirements.txt                # Project dependencies  
├── ⚙️ setup.py                        # Package configuration
├── 📚 README.md                       # Project documentation
│
├── 📊 artifacts/                      # Generated model artifacts
│   ├── 📈 data.csv                   # Raw dataset
│   ├── 🔧 preprocessor.pkl           # Data transformation pipeline
│   ├── 🤖 model.pkl                  # Trained best model
│   ├── 📝 train.csv                  # Training dataset
│   └── ✅ test.csv                   # Testing dataset
│
├── 📓 notebook/                       # Jupyter notebooks
│   ├── 🔍 1. EDA STUDENT PERFORMANCE.ipynb   # Exploratory Data Analysis
│   ├── 🎯 2. MODEL TRAINING.ipynb            # Model development
│   └── 📁 data/
│       └── 📊 stud.csv               # Original dataset
│
├── 🎨 templates/                      # HTML templates
│   ├── 🏠 index.html                # Landing page
│   └── 📋 home.html                 # Prediction form
│
├── 📦 src/                           # Source code package
│   ├── 🔧 components/               # ML pipeline components
│   │   ├── 📥 data_ingestion.py     # Data loading and splitting
│   │   ├── 🔄 data_transformation.py # Feature engineering
│   │   └── 🎯 model_trainer.py      # Model training and selection
│   │
│   ├── 🔀 pipeline/                 # Prediction pipelines
│   │   ├── 🚀 predict_pipeline.py   # Inference pipeline
│   │   └── 🎓 train_pipeline.py     # Training pipeline
│   │
│   ├── 🛠️ utils.py                  # Utility functions
│   ├── ⚠️ exception.py              # Custom exception handling
│   └── 📝 logger.py                 # Logging configuration
│
└── 📋 logs/                         # Application logs
    └── 📅 [timestamp].log          # Timestamped log files
```

## 🛠️ Technologies Used

### Core Framework
- **Python 3.11+**: Main programming language
- **Flask**: Web framework for the user interface
- **scikit-learn 1.2.1**: Machine learning algorithms and preprocessing

### Data Science Stack
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib & seaborn**: Data visualization

### Machine Learning Libraries
- **XGBoost**: Gradient boosting framework
- **CatBoost**: Categorical feature boosting
- **dill**: Advanced object serialization

### Development Tools
- **setuptools**: Package management
- **Custom logging**: Application monitoring
- **Exception handling**: Error management

### Frontend
- **HTML5 & CSS3**: Modern responsive web interface
- **Jinja2**: Template engine for dynamic content

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Contribution
- 🔧 Additional ML algorithms
- 📊 Enhanced data visualization
- 🌐 API improvements
- 📱 Mobile responsiveness
- 🧪 Unit testing
- 📚 Documentation improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Yash Pinjarkar**
- 📧 Email: yashpinjarkar2003@gmail.com
- 🐙 GitHub: [@yashpinjarkar10](https://github.com/yashpinjarkar10)
- 🔗 LinkedIn: [Connect with me](https://linkedin.com/in/yashpinjarkar)

---

<div align=\"center\">
  <p><strong>⭐ If you found this project helpful, please consider giving it a star!</strong></p>
  <p>Built with ❤️ for the ML community</p>
</div>