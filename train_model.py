# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# 1. Load data
df = pd.read_csv('doggy-boot-harness.csv')

# 2. Prepare X and y
X = df[['harness_size']].values   # shape (n_samples, 1)
y = df['boot_size'].values        # shape (n_samples,)

# 3. Train model
model = LinearRegression().fit(X, y)

# 4. Print metrics
print("Model R\u00b2:", model.score(X, y))
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# 5. Save the model
joblib.dump(model, 'boot_model.pkl')
print("Saved model to boot_model.pkl")
