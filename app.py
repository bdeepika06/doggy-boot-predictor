# app.py
import streamlit as st
import joblib
import pandas as pd

# Title
st.title("🐾 Doggy Boot Size Predictor")

# Load model once
@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load('boot_model.pkl')

model = load_model()

# User input: harness size (cm)
harness_size = st.slider("Harness size (cm)", 40, 70, 55)

# Predict boot size
df_input = pd.DataFrame({'harness_size': [harness_size]})
predicted = model.predict(df_input)[0]
st.write(f"🔍 Estimated boot size: **{predicted:.1f}** cm")

# Let user pick their chosen boot size
chosen = st.number_input("Your selected boot size (cm)", value=int(round(predicted)))

# Provide feedback
if chosen < round(predicted):
    st.warning(f"The boots you chose might be TOO SMALL. We recommend size {round(predicted)}.")
elif chosen > round(predicted):
    st.warning(f"The boots you chose might be TOO BIG. We recommend size {round(predicted)}.")
else:
    st.success("Perfect match! 🎉")
