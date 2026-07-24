"""
VishwasFund — eligibility / approval-likelihood model.

Trains a simple classifier that scores how likely a scheme application
is to be approved, given business profile features. Starts with a
synthetic dataset — swap in real scheme-outcome data as it's collected.
"""

import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

FEATURES = [
    "monthly_income",
    "has_existing_assets",
    "prior_loan_history",
    "years_in_business",
    "location_tier",  # 1 = rural, 2 = semi-urban, 3 = urban
]


def make_synthetic_dataset(n=2000, seed=42):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "monthly_income": rng.normal(12000, 6000, n).clip(1000, None),
        "has_existing_assets": rng.integers(0, 2, n),
        "prior_loan_history": rng.integers(0, 2, n),
        "years_in_business": rng.integers(0, 15, n),
        "location_tier": rng.integers(1, 4, n),
    })
    # toy approval rule: more income, assets, and business history raise approval odds
    score = (
        0.00004 * df.monthly_income
        + 0.3 * df.has_existing_assets
        + 0.2 * df.prior_loan_history
        + 0.03 * df.years_in_business
        - 0.1 * (df.location_tier == 3)  # schemes here favor rural/semi-urban
    )
    prob = 1 / (1 + np.exp(-(score - score.mean())))
    df["approved"] = (rng.random(n) < prob).astype(int)
    return df


def train():
    df = make_synthetic_dataset()
    X, y = df[FEATURES], df["approved"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=200, max_depth=6, random_state=42)
    model.fit(X_train, y_train)

    print(classification_report(y_test, model.predict(X_test)))
    joblib.dump(model, "eligibility_model.pkl")
    print("Saved eligibility_model.pkl")


if __name__ == "__main__":
    train()
