import shap
import numpy as np


def compute_tree_shap(model, X_transformed):
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_transformed)

    if isinstance(shap_values, list):
        shap_values = shap_values[1]

    return shap_values
