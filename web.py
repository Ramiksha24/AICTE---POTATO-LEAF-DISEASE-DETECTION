import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="Plant Disease Detection For Sustainable Agriculture", page_icon="🌿", layout="wide")

# Sidebar Branding
st.sidebar.image("logo2.png", use_container_width=True)  # Replace with your project logo if available
st.sidebar.title("🌿 Plant Disease System")
st.sidebar.markdown("🔬 AI-powered tool for detecting plant diseases. Upload an image to get predictions.")

# Sidebar Navigation
app_mode = st.sidebar.radio("📌 Navigation", ["Home", "Disease Recognition"])

# Function for model prediction
@st.cache_resource  # Cache the model to avoid reloading it multiple times
def load_model():
    try:
        model = tf.keras.models.load_model("trained_plant_disease_model.keras")  # Ensure model exists
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        return None

model = load_model()

def model_prediction(test_image):
    try:
        image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
        input_arr = tf.keras.preprocessing.image.img_to_array(image)
        input_arr = np.expand_dims(input_arr, axis=0)
        predictions = model.predict(input_arr)
        return np.argmax(predictions)  # Returns class index
    except Exception as e:
        st.error(f"⚠ Error processing image: {e}")
        return None

# Home Page
if app_mode == "Home":
    st.markdown("<h1 style='text-align:center;'>🌱 Plant Disease Detection System</h1>", unsafe_allow_html=True)
    st.write("👋 **Welcome to the Plant Disease Detection System!**")
    st.write("This AI-powered tool helps detect plant diseases for sustainable agriculture. Use the sidebar to navigate.")

    # Display Image (Optional)
    try:
        home_img = Image.open("titleim.png")
        st.image(home_img, use_container_width=True)
    except FileNotFoundError:
        st.warning("⚠ 'titleim.png' not found. Please add it to the project folder.")

# Disease Recognition Page
elif app_mode == "Disease Recognition":
    st.header("🩺 Upload a Leaf Image for Disease Detection")
    
    uploaded_file = st.file_uploader("📤 Upload a leaf image...", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        if st.button("👀 Show Image"):
            st.image(uploaded_file, caption="📸 Uploaded Image", use_container_width=True)
        
        # Make Prediction
        if st.button("🔍 Predict"):
            st.snow()  # Fun effect
            with st.spinner("🔍 Analyzing... Please wait..."):
                prediction = model_prediction(uploaded_file)
            
            # Define class names
            class_names = ["Potato___Early_blight", "Potato___Late_blight", "Potato__Healthy"]
            disease_name = class_names[prediction] if prediction < len(class_names) else "Unknown"

            st.success(f"✅ **Detected Disease: {disease_name}**")