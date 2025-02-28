# Laptop Price Predictor

## Overview
The **Laptop Price Predictor** is a machine learning project designed to estimate the price range of laptops based on their specifications. By analyzing key hardware and performance features, the model provides an approximate price category.

## Features
- Predicts laptop price based on specifications such as processor, RAM, CPU, GPU, and more.
- Implements multiple machine learning models and selects the best-performing one.
- Uses Exploratory Data Analysis (EDA) for insights into feature importance.
- Deployed using **Flask** for a user-friendly interface.

## Dataset
The dataset contains various attributes of laptops, including:
- **Company**
- **TypeName**
- **ScreenResolution**
- **CPU**
- **RAM**
- **GPU**
- **OpSys**
- **Weight**
- **Price(Target Variable)**

## Tech Stack
- **Programming Language**: Python
- **Libraries Used**:
  - `pandas` for data processing
  - `numpy` for numerical operations
  - `matplotlib & seaborn` for data visualization
  - `scikit-learn` for machine learning models
  - `Flask` for deployment

## Model Selection
Various classification models were evaluated, including:
- **Linear Regression**
- **Lasso**
- **Decision Tree**
- **Random Forest**

Performance metrics such as accuracy were used to determine the best model.

## Deployment
The trained model is deployed using **Flask** to allow users to input laptop specifications and receive price predictions instantly.

https://github.com/user-attachments/assets/0a51eb79-9c5c-4cdf-a73e-a918935682eb

For currency conversion, the model uses an exchange rate of **1 EUR = 309.35 LKR** as of **2025-02-28**.

## Future Improvements
- Enhance dataset with more real-world pricing data.
- Improve model accuracy with deep learning techniques.
- Optimize deployment for web and mobile accessibility.

## Author
Sashini Shayamindi - AI Researcher & Machine Learning Enthusiast











