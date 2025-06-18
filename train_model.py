import pandas as pd
import statsmodels.formula.api as smf
import joblib

# 1. Load the data
df = pd.read_csv('doggy-boot-harness.csv')

# 2. Fit a linear regression: boot_size ~ harness_size
model = smf.ols('boot_size ~ harness_size', data=df).fit()

# 3. Print model metrics
print("Model R²:", model.rsquared)
print("Slope:", model.params['harness_size'])
print("Intercept:", model.params['Intercept'])

# 4. Save the trained model
joblib.dump(model, 'boot_model.pkl')
print("Saved model to boot_model.pkl")
