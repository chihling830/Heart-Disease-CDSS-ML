# Heart Disease Clinical Decision Support System (CDSS)
### Explainable Machine Learning for Clinical Risk Assessment

## Project Overview
This project develops an **Explainable Machine Learning–based Clinical Decision Support System (CDSS)** for heart disease risk prediction.

Beyond predictive accuracy, the core contribution lies in **feature importance analysis and SHAP-based explainability**, transforming model outputs into **actionable clinical decision-support insights**.

The project bridges **academic machine learning modeling** and **real-world healthcare decision-making**, positioning ML models as **early-warning and assistive tools**, rather than black-box predictors.

---

## Motivation & Clinical Context
Heart disease diagnosis involves multiple interacting risk factors such as blood pressure, cholesterol levels, ECG results, and exercise-induced symptoms.  
Although machine learning models can achieve high predictive performance, **lack of interpretability remains a major barrier to clinical adoption**.

This project addresses this gap by:
- Building robust ML models for heart disease prediction
- Systematically analyzing **feature importance across different model families**
- Applying **SHAP (SHapley Additive Explanations)** for global and individual-level interpretability
- Translating explanations into **CDSS-style clinical follow-up recommendations**

---

## Dataset
- **Source**: UCI Machine Learning Repository – Heart Disease Cleveland Dataset
- **Samples**: 304 records (297 after cleaning)
- **Features**: 14 clinical attributes
- **Target**: Binary classification (presence / absence of heart disease)

Key features include:
- Age, resting blood pressure, cholesterol
- Maximum heart rate (thalach)
- ST depression (oldpeak)
- Chest pain type (cp)
- Thalassemia (thal)
- Number of major vessels (ca)

---

## Methods & Pipeline

### Data Preprocessing
- Missing value removal
- One-Hot Encoding for categorical variables
- StandardScaler for numerical features
- Stratified 10-fold cross-validation

### Models Evaluated
- Logistic Regression
- Decision Tree
- Random Forest
- Support Vector Machine (Linear & RBF)
- XGBoost

### Evaluation Metrics
- Accuracy
- Precision / Recall
- F1-score
- ROC-AUC
- Confusion Matrix

---

## Feature Importance & Explainability (Core Contribution)

### Linear Models (Logistic Regression, Linear SVM)
Key positive risk contributors:
- **oldpeak** (ST depression after exercise)
- **trestbps** (resting blood pressure)
- **chol** (cholesterol)

Protective factors:
- **thalach** (maximum heart rate)
- **age**

These models provide **directional interpretability** aligned with clinical reasoning.

---

### Tree-Based Models (Random Forest, XGBoost)
Most influential features:
- **thal** (myocardial perfusion condition)
- **cp** (chest pain type)
- **ca** (number of major vessels)
- **exang** (exercise-induced angina)

These models capture **nonlinear interactions and complex risk patterns**.

---

### SHAP Analysis
SHAP was applied to:
- Analyze **global feature importance**
- Explain **individual patient predictions**
- Visualize how feature values push predictions toward higher or lower risk

This enhances model transparency and supports clinical trust.

---

## From Explainable AI to CDSS
Rather than stopping at model interpretation, this project maps explainability results into **clinical decision-support suggestions**, such as:

- Identifying high-risk patients with ambiguous traditional scores
- Highlighting dominant risk drivers for individual predictions
- Supporting prioritization of follow-up examinations


