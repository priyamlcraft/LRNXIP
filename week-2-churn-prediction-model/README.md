# Customer Churn Prediction Model

## Learnix Machine Learning Internship – Week 2

### Project Overview
This project focuses on predicting customer churn using Machine Learning techniques. The Telco Customer Churn dataset is used to analyze customer behavior and identify customers who are likely to discontinue a service.

Two classification algorithms, Logistic Regression and Random Forest, are implemented and evaluated.

### Objectives
- Understand and inspect the customer churn dataset.
- Perform data cleaning and exploratory data analysis (EDA).
- Handle missing values and categorical features.
- Apply feature scaling and encoding.
- Train Logistic Regression and Random Forest models.
- Evaluate and compare model performance.
- Visualize results using graphs and evaluation metrics.

### Dataset
**Dataset Name:** Telco Customer Churn Dataset

**Source:** [Kaggle – Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

**Dataset File:** `WA_Fn-UseC_-Telco-Customer-Churn.csv`

- Total Records: 7,043
- Total Original Features: 21
- Target Variable: Churn

### Technologies Used
- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

### Machine Learning Algorithms
1. Logistic Regression
2. Random Forest Classifier

### Project Workflow
1. Import required libraries.
2. Load and inspect the dataset.
3. Clean the data and handle missing values.
4. Perform Exploratory Data Analysis.
5. Separate features and target variables.
6. Split data into training and testing sets.
7. Apply encoding and feature scaling.
8. Train Logistic Regression and Random Forest models.
9. Evaluate model performance.
10. Visualize model results.

### Model Performance

| Evaluation Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 73.81% | 77.86% |
| Precision | 50.43% | 57.21% |
| Recall | 78.34% | 65.78% |
| ROC-AUC | 0.8413 | 0.8346 |

### Visualizations
The project includes:
- Customer Churn Distribution
- Customer Tenure Distribution
- Monthly Charges Distribution
- Model Performance Comparison
- Confusion Matrix
- ROC Curve Comparison

### Project Structure
```text
week-2-churn-prediction-model/
│
├── README.md
├── requirements.txt
├── customer_churn_prediction.ipynb
│
└── week2_outputs/
    ├── customer_churn_distribution.png
    ├── customer_tenure_distribution.png
    ├── monthly_charges_distribution.png
    ├── model_performance_comparison.png
    ├── confusion_matrices.png
    └── roc_curve_comparison.png
```

### Conclusion
Both machine learning models were successfully trained and evaluated. Random Forest achieved higher accuracy, while Logistic Regression achieved better recall and ROC-AUC scores.

This project provided practical experience in data preprocessing, exploratory data analysis, classification algorithms, model evaluation, and data visualization.

### Internship
**Organization:** Learnix  
**Domain:** Machine Learning  
**Project:** Week 2 – Customer Churn Prediction Model
