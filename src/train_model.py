from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier


def build_model_pipeline(model, preprocessor):
    return Pipeline([
        ("preprocess", preprocessor),
        ("model", model)
    ])


def get_models(best_k=5):
    return {
        "KNN": KNeighborsClassifier(n_neighbors=best_k),
        "DecisionTree": DecisionTreeClassifier(random_state=42),
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
        "LogisticRegression": LogisticRegression(max_iter=1000),
        "SVM_Linear": SVC(kernel="linear", probability=True),
        "SVM_RBF": SVC(kernel="rbf", probability=True),
        "XGBoost": XGBClassifier(
            n_estimators=200,
            max_depth=3,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            eval_metric="logloss"
        )
    }
