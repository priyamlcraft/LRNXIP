# Customer Churn Prediction App

### Customer Churn Prediction & Retention Analytics System

## Project Overview

The **Customer Churn Prediction App** is a Machine Learning-based web application developed as part of Week 3 of the Learnix Machine Learning Internship.

This application uses a pre-trained Machine Learning model to predict whether a customer is likely to leave a service based on their information. It provides an interactive interface built with Streamlit, allowing users to enter customer details and obtain churn predictions.

## Project Objectives

- Develop an interactive web application using Streamlit.
- Integrate a pre-trained Machine Learning model.
- Predict customer churn based on customer information.
- Demonstrate the practical application of Machine Learning in customer retention analysis.

## Key Features

- Interactive and user-friendly interface.
- Customer information input form.
- Machine Learning-based churn prediction.
- Real-time prediction through the Streamlit application.
- Clear presentation of prediction results.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Pandas | Data handling and processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning model |
| Joblib | Model loading |
| Streamlit | Web application development |

## Project Structure

```text
week-3-churn-prediction-app/
│
├── app.py
├── churn_model.pkl
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/priyamlcraft/LRNXIP.git
```

### 2. Navigate to the Project Directory

```bash
cd LRNXIP/week-3-churn-prediction-app
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

The application will open in your default web browser.

## Machine Learning Model

The application integrates a pre-trained classification model stored in `churn_model.pkl`. The model processes customer information and generates a prediction indicating whether a customer is likely to churn.

## Learning Outcomes

Through this project, I gained practical experience in:

- Integrating a trained Machine Learning model into a web application.
- Building interactive applications using Streamlit.
- Managing Python libraries and project dependencies.
- Loading and using a saved Machine Learning model with Joblib.
- Understanding the real-world applications of Machine Learning in customer churn prediction.

## Internship Details

**Organization:** Learnix  
**Internship Domain:** Machine Learning  
**Project:** Customer Churn Prediction App  
**Project Theme:** Customer Churn Prediction & Retention Analytics System  
**Task:** Week 3 – Streamlit Application Development

## Author

**Priya Mandal**  
B.Tech – Information Technology  
Bankura Unnayani Institute of Engineering

**GitHub:** [priyamlcraft](https://github.com/priyamlcraft)

## Conclusion

The Week 3 project provided practical experience in developing a Machine Learning-based web application using Streamlit. By integrating a pre-trained classification model, the application demonstrates how customer information can be used to predict potential churn.

This project strengthened my understanding of Machine Learning model integration, Python libraries, and interactive application development. It also provided valuable insight into how Machine Learning can support data-driven decision-making and customer retention strategies.

---

*Developed as part of the Learnix Machine Learning Internship to apply Machine Learning concepts in a practical web application.*
