import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler, OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, roc_auc_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

from imblearn.over_sampling import SMOTENC

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

import joblib
print("✅ All libraries imported successfully")
NUM_FEATURES = [
    "person_age",
    "person_income",
    "person_emp_length",
    "loan_amnt",
    "loan_int_rate",
    "loan_percent_income",
    "cb_person_cred_hist_length"
]

BINARY_FEATURES = ["cb_person_default_on_file"]

NOMINAL_FEATURES = [
    "person_home_ownership",
    "loan_intent"
]

ORDINAL_FEATURES = ["loan_grade"]

def load_and_preprocess_data(file_path):
    df = pd.read_csv(file_path)
    print("✅ Data loaded successfully")

    if "loan_status" not in df.columns:
        raise ValueError("Target column 'loan_status' not found")

    return df

def build_preprocessor():
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", RobustScaler())
    ])

    binary_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OrdinalEncoder(categories=[["N", "Y"]]))
    ])

    nominal_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])

    ordinal_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OrdinalEncoder(
            categories=[["A", "B", "C", "D", "E", "F", "G"]]
        ))
    ])

    return ColumnTransformer([
        ("num", num_pipeline, NUM_FEATURES),
        ("bin", binary_pipeline, BINARY_FEATURES),
        ("nom", nominal_pipeline, NOMINAL_FEATURES),
        ("ord", ordinal_pipeline, ORDINAL_FEATURES)
    ])

def train_models(df):

    X = df.drop("loan_status", axis=1)
    y = df["loan_status"]
    print("✅ Features and target variable separated")
    # ---- SMOTENC ----
    categorical_cols = BINARY_FEATURES + NOMINAL_FEATURES + ORDINAL_FEATURES
    cat_indices = [X.columns.get_loc(col) for col in categorical_cols]

    smote = SMOTENC(
        categorical_features=cat_indices,
        random_state=42,
        k_neighbors=3
    )
    print("✅ SMOTENC initialized")
    X_resampled, y_resampled = smote.fit_resample(X, y)

    # ---- Preprocessing ----
    preprocessor = build_preprocessor()
    X_encoded = preprocessor.fit_transform(X_resampled)

    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y_resampled, test_size=0.2, random_state=42
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, n_jobs=-1),
        "Random Forest": RandomForestClassifier(n_estimators=200, n_jobs=-1),
        "XGBoost": XGBClassifier(
            eval_metric="logloss",
            n_estimators=200,
            learning_rate=0.05,
            max_depth=6
        ),
        "LightGBM": LGBMClassifier(
            n_estimators=200,
            learning_rate=0.05
        ),
        "SVC": SVC(probability=True)
    }

    results = {}
    best_model = None
    best_auc = 0

    # ---- Classical ML ----
    for name, model in models.items():
        model.fit(X_train, y_train)

        y_prob = model.predict_proba(X_test)[:, 1]
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_prob)

        results[name] = (acc, auc)

        if auc > best_auc:
            best_auc = auc
            best_model = model

    # ---- ANN ----
    ann = Sequential([
        Dense(32, activation="relu", input_shape=(X_train.shape[1],)),
        Dense(16, activation="relu"),
        Dense(1, activation="sigmoid")
    ])

    ann.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=[tf.keras.metrics.AUC(name="auc")]
    )

    ann.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)

    ann_auc = roc_auc_score(y_test, ann.predict(X_test))
    ann_acc = accuracy_score(y_test, (ann.predict(X_test) > 0.5).astype(int))

    results["ANN"] = (ann_acc, ann_auc)

    if ann_auc > best_auc:
        best_model = ann

    return best_model, preprocessor, results

def save_model(model, preprocessor, model_dir="model_files"):
    os.makedirs(model_dir, exist_ok=True)

    if isinstance(model, tf.keras.Model):
        model.save(os.path.join(model_dir, "best_ann_model"))
    else:
        joblib.dump(model, os.path.join(model_dir, "best_model.pkl"))

    joblib.dump(preprocessor, os.path.join(model_dir, "preprocessor.pkl"))

    print("✅ Best model & preprocessor saved")


if __name__ == "__main__":
    df = load_and_preprocess_data("./train.csv")

    best_model, preprocessor, results = train_models(df)

    save_model(best_model, preprocessor)

    print("\n📊 Model Performance:")
    for name, (acc, auc) in results.items():
        print(f"{name}: Accuracy={acc:.4f}, AUC={auc:.4f}")

