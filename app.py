# app.py
import streamlit as st
import pandas as pd
import joblib

st.title("🐾 Doggy Boot Size Predictor")

@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load('boot_model.pkl')

model = load_model()

harness_size = st.slider("Harness size (cm)", 40, 70, 55)

# Prepare input and predict
df_input = pd.DataFrame({'harness_size': [harness_size]})
predicted = model.predict(df_input[['harness_size']].values)[0]
st.write(f"🔍 Estimated boot size: **{predicted:.1f}** cm")

chosen = st.number_input("Your selected boot size (cm)", value=int(round(predicted)))
if chosen < round(predicted):
    st.warning(f"The boots you chose might be TOO SMALL. We recommend size {round(predicted)}.")
elif chosen > round(predicted):
    st.warning(f"The boots you chose might be TOO BIG. We recommend size {round(predicted)}.")
else:
    st.success("Perfect match! 🎉")
