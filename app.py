# app.py
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="🐾 Doggy Boot Size Predictor")

@st.cache(allow_output_mutation=True)
def load_model():
    # Load the scikit-learn model you trained
    return joblib.load("boot_model.pkl")

model = load_model()

st.title("🐾 Doggy Boot Size Predictor")
st.markdown(
    """
    Use the slider below to select your dog’s harness size (cm), 
    and get a boot-size prediction—and advice if your chosen size is off.
    """
)

# **THIS** is the interactive slider whose value changes on each drag!
harness_size = st.slider("Harness size (cm)", min_value=40, max_value=70, value=55)

# Now use **that** harness_size for prediction
predicted_size = model.predict([[harness_size]])[0]
rounded = int(round(predicted_size))

st.write(f"🔍 **Estimated boot size:** {predicted_size:.1f} cm")

# Let the user pick their chosen size
chosen = st.number_input("Your selected boot size (cm)", 
                         min_value=20, max_value=60, value=rounded)

# **Re-evaluate** after each interaction
if chosen < rounded:
    st.warning(f"The boots you chose might be TOO SMALL. We recommend size {rounded}.")
elif chosen > rounded:
    st.warning(f"The boots you chose might be TOO BIG. We recommend size {rounded}.")
else:
    st.success("Perfect match! 🎉")
