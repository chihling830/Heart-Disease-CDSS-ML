# Heart Disease Clinical Decision Support System (CDSS) with Explainable Machine Learning

## Project Overview
This project develops an **Explainable Machine Learning–based Clinical Decision Support System (CDSS)** for heart disease risk prediction.  
Beyond predictive performance, the focus is on **model interpretability (SHAP)** and **translating model outputs into actionable clinical insights**, bridging the gap between academic modeling and real-world medical decision-making.

The project was completed as a team-based applied machine learning study and later reorganized into a production-style repository structure for reproducibility and clarity.

---

## Motivation & Clinical Context
Heart disease diagnosis often involves multiple risk factors and subjective clinical judgment.  
While machine learning models can achieve high predictive accuracy, **lack of interpretability limits their adoption in healthcare**.

This project addresses that gap by:
- Building robust ML models for heart disease prediction
- Applying **SHAP (SHapley Additive exPlanations)** for explainability
- Mapping model explanations into **practical decision-support insights** suitable for CDSS scenarios

---

## Dataset
- Public heart disease dataset (clinical and demographic variables)
- Features include age, sex, chest pain type, blood pressure, cholesterol, ECG results, etc.
- Binary classification target: presence or absence of heart disease

> Note: Due to privacy considerations, raw data are not included in this repository.

---

##  Methods & Pipeline

### 1.Data Preprocessing
- Missing value handling
- Feature scaling
- Categorical encoding
- Train-test split

### 2.Models Evaluated
- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- Gradient Boosting–based models

### 3.Model Evaluation
- Accuracy
- Precision / Recall
- F1-score
- ROC-AUC

### 4.Explainability (Core Contribution)
- **SHAP values** used to analyze:
  - Global feature importance
  - Individual-level prediction explanations
- Identification of clinically meaningful risk drivers

---

## Explainable AI → Clinical Insights
Rather than stopping at feature importance, this project **translates SHAP outputs into CDSS-style recommendations**, such as:

- Identifying high-risk patients even when traditional risk scores are ambiguous
- Highlighting which physiological factors most strongly contribute to a specific prediction
- Supporting clinicians in prioritizing follow-up tests or interventions

This design reflects **real-world clinical workflows**, not just academic evaluation metrics.

---

## Repository Structure

```text
Heart-Disease-CDSS-ML/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_model_training.ipynb
│   ├── 03_model_evaluation.ipynb
│   └── 04_shap_analysis.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   └── shap_utils.py
│
└── reports/
    ├── figures/
    └── final_report.pdf
