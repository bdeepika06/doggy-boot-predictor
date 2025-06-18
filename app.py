import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="🐾 Doggy Boot Size Predictor")

@st.cache(allow_output_mutation=True)
def load_model():
    return joblib.load("boot_model.pkl")

model = load_model()

st.title("🐾 Doggy Boot Size Predictor")
st.markdown(
    """
    Use the slider below to select your dog’s harness size (cm), 
    and get a boot-size prediction—and advice if your chosen size is off.
    """
)

# 1) Slider
harness_size = st.slider("Harness size (cm)", min_value=40, max_value=70, value=55)

# 2) Prediction
predicted_size = model.predict([[harness_size]])[0]
rounded = int(round(predicted_size))


# 3) Display estimate
st.write(f"🔍 **Estimated boot size:** {predicted_size:.1f} cm")

# 4) User choice
chosen = st.number_input("Your selected boot size (cm)", 
                         min_value=20, max_value=60, value=rounded)



# 5) Warnings / success
if chosen < rounded:
    st.warning(f"The boots you chose might be TOO SMALL. We recommend size {rounded}.")
elif chosen > rounded:
    st.warning(f"The boots you chose might be TOO BIG. We recommend size {rounded}.")
else:
    st.success("Perfect match! 🎉")
