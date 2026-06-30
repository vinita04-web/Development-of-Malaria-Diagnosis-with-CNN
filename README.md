# 🦟 Development of Malaria Diagnosis with CNN

A deep learning project that implements a **Custom Convolutional Neural Network (CNN)** for detecting malaria from microscopic blood cell images. The model classifies images as **Parasitized (Malaria Infected)** or **Uninfected**. This project is based on the research paper **"Development of Malaria Diagnosis with Convolutional Neural Network Architectures: A CNN-Based Software for Accurate Cell Image Analysis."**

---

## 📌 Project Overview

Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites. Early diagnosis is essential for timely treatment. This project uses a **Custom CNN model** to automatically classify microscopic blood cell images into infected and uninfected categories.

---

## ✨ Features

- Custom CNN architecture (No VGG19 or EfficientNetB3)
- Image preprocessing and resizing to **50 × 50 × 3**
- Train, Validation, and Test data split
- Model trained for **50 epochs**
- Performance evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix
- Prediction on unseen blood cell images
- Interactive Streamlit web application

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- OpenCV
- Matplotlib
- Scikit-learn
- Pandas
- Pillow
- Streamlit
- Jupyter Notebook

---

## 📂 Dataset

**Malaria Cell Images Dataset**

https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria

Dataset Classes:
- Parasitized
- Uninfected

---

## 🧠 CNN Model Workflow

1. Load the malaria cell image dataset
2. Resize all images to **50 × 50 × 3**
3. Normalize pixel values
4. Split data into Train, Validation, and Test sets
5. Build the proposed Custom CNN architecture
6. Train the model for **50 epochs**
7. Evaluate the model using classification metrics
8. Predict malaria infection on unseen images
9. Save the trained model
10. Deploy using Streamlit

---

## 📊 Model Evaluation

The model was evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The trained model achieved approximately **95% test accuracy**.

---

## 🚀 Streamlit Application

The project includes a simple Streamlit web application where users can:

- Upload a microscopic blood cell image
- Predict whether the cell is:
  - 🦠 Parasitized (Malaria Infected)
  - ✅ Uninfected

Run the application locally:

```bash
streamlit run app.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/vinita04-web/Development-of-Malaria-Diagnosis-with-CNN.git
```

Move to the project folder:

```bash
cd Development-of-Malaria-Diagnosis-with-CNN
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Development-of-Malaria-Diagnosis-with-CNN/
│
├── app.py
├── malaria_cnn.ipynb
├── malaria_model.keras
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 📷 Results

The project includes:

- Training Results
- Accuracy Graph
- Loss Graph
- Classification Report
- Confusion Matrix
- Sample Predictions
- Streamlit Application Output

---

## 👩‍💻 Author

**Vinita Vinayak Pawar**

**GitHub:** https://github.com/vinita04-web

**LinkedIn:** https://www.linkedin.com/in/vinita-pawar-158792352/

---

## 📄 License

This project is developed for educational and research purposes.
