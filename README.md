# AICTE---POTATO-LEAF-DISEASE-DETECTION

🍂 Potato Leaf Disease Detection using CNN


🔍 Overview


This project is a Deep Learning-based web application built using TensorFlow, Streamlit, and OpenCV to detect potato leaf diseases. The system helps farmers and agricultural experts identify diseases early, ensuring sustainable farming practices.

🛠 Features
✅ Upload a leaf image for disease detection.
✅ Uses a pre-trained CNN model for accurate predictions.
✅ Supports Potato Early Blight, Late Blight, and Healthy Leaf classification.
✅ Interactive Streamlit web interface.
✅ Real-time image preview & prediction results.

📌 Technologies Used
Python 🐍
TensorFlow & Keras 🧠
Streamlit 🌐
NumPy & OpenCV 🖼
PIL (Pillow) for image handling
📂 Project Structure
bash
Copy
Edit
📦 Potato-Disease-Detection
│-- 📂 datasets/           # Training and testing datasets
│-- 📂 models/             # Trained deep learning model
│-- 📂 images/             # Sample test images
│-- 📝 app.py              # Streamlit app file
│-- 📝 trained_model.keras # Pre-trained model
│-- 📝 requirements.txt    # Dependencies list
│-- 📝 README.md           # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/Potato-Disease-Detection.git
cd Potato-Disease-Detection
2️⃣ Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows
3️⃣ Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the application

bash
Copy
Edit
streamlit run app.py
🖼 How to Use
1️⃣ Upload an image of a potato leaf 🍂.
2️⃣ Click "Show Image" to preview it.
3️⃣ Click "🔍 Predict" to detect disease.
4️⃣ The model will predict one of the following:

Potato Early Blight
Potato Late Blight
Healthy Leaf
📸 Screenshot

📢 Future Improvements
🔹 Improve model accuracy with more training data.
🔹 Expand detection for other crops.
🔹 Deploy as a web-based API.

