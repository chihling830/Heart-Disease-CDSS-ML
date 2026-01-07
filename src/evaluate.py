import numpy as np
from sklearn.model_selection import cross_validate, cross_val_predict
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, auc
)


SCORERS = {
    "accuracy": accuracy_score,
    "precision": precision_score,
    "recall": recall_score,
    "f1": f1_score,
}


def evaluate_pipeline(pipeline, X, y, cv):
    scores = cross_validate(
        pipeline, X, y, cv=cv,
        scoring=SCORERS, n_jobs=-1
    )
    return {k: np.mean(v) for k, v in scores.items() if k.startswith("test_")}


def get_confusion_matrix(pipeline, X, y, cv):
    y_pred = cross_val_predict(pipeline, X, y, cv=cv, n_jobs=-1)
    return confusion_matrix(y, y_pred)


def get_roc(pipeline, X, y, cv):
    y_score = cross_val_predict(
        pipeline, X, y, cv=cv,
        method="predict_proba", n_jobs=-1
    )[:, 1]

    fpr, tpr, _ = roc_curve(y, y_score)
    return fpr, tpr, auc(fpr, tpr)
