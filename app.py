

import streamlit as st
import numpy as np
import tensorflow as tf
import joblib

# --- 1. Page Configuration ---
st.set_page_config(page_title="AI TLE Predictor", page_icon="⏱️", layout="centered")

st.title("⏱️ Code Performance & TLE Predictor")
st.markdown("""
**Welcome to the Developer's Assistant!** This AI was custom-trained from scratch to predict how long an algorithm will take to execute based on its Big O Time Complexity and the input size ($N$). 
Use it to check if your code will hit a **Time Limit Exceeded (TLE)** error before you submit it!
""")

st.divider()

# --- 2. Load the Custom Brain ---
@st.cache_resource
def load_assets():
    # Add compile=False to fix the 'mse' deserialization error!
    model = tf.keras.models.load_model('tle_predictor.h5', compile=False)
    scaler = joblib.load('scaler.pkl')
    encoder = joblib.load('encoder.pkl')
    return model, scaler, encoder

try:
    model, scaler, encoder = load_assets()
except Exception as e:
    # This will now print the EXACT error causing the crash!
    st.error(f"Failed to load the model files. \n\n**Error Details:** {e}")
    st.stop()

# ... (Keep the rest of your UI code below this exactly the same!) ...

# --- 3. The User Interface ---
st.subheader("Enter your constraints:")

col1, col2 = st.columns(2)

with col1:
    # We ask the encoder what classes it knows, so the dropdown is exactly accurate
    complexities = encoder.classes_
    selected_complexity = st.selectbox("Select Time Complexity:", complexities)

with col2:
    # N can be anywhere from 10 to a massive 100,000
    user_n = st.number_input("Enter Input Size (N):", min_value=10, max_value=100000, value=10000, step=1000)

time_limit = st.slider("Target Time Limit (Seconds):", min_value=0.5, max_value=5.0, value=1.0, step=0.5)

# --- 4. The AI Prediction Logic ---
if st.button("🔮 Predict Execution Time", use_container_width=True):
    with st.spinner("AI is calculating the math curve..."):
        
        # 1. Translate the text (e.g., "O(N^2)") into the secret number
        encoded_c = encoder.transform([selected_complexity])[0]
        
        # 2. Package it exactly how the AI expects it
        features = np.array([[encoded_c, user_n]])
        
        # 3. Scale the numbers so they match the training data format
        scaled_features = scaler.transform(features)
        
        # 4. PREDICT!
        predicted_time = model.predict(scaled_features)[0][0]
        
        # Sometimes regression models predict tiny negative numbers for instant tasks. We cap it at 0.0001
        predicted_time = max(0.0001, predicted_time) 

        st.divider()
        st.subheader("Results:")
        
        st.markdown(f"### Estimated Time: **{predicted_time:.4f} seconds**")
        
        # --- 5. The TLE Guard Logic ---
        if predicted_time > time_limit:
            st.error(f"🚨 **WARNING: TIME LIMIT EXCEEDED!** \n\nYour {selected_complexity} algorithm will likely take longer than the {time_limit}s limit. You need to optimize your loops!")
        elif predicted_time > (time_limit * 0.75):
            st.warning(f"⚠️ **CAUTION:** \n\nYou are getting dangerously close to the {time_limit}s limit. It might pass, but it's risky.")
        else:
            st.success(f"✅ **SAFE TO SUBMIT!** \n\nYour {selected_complexity} algorithm is highly efficient for N = {user_n}.")


# Evaluate the model on the 20% hidden test data
# loss, mae = model.evaluate(X_test, y_test, verbose=0)
# print(f"\n📊 Model Accuracy Metric (MAE): The AI is off by an average of {mae:.4f} seconds!")
