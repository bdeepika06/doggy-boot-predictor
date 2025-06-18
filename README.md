# Doggy Boot Size Predictor

A self-contained demo that takes you from raw data to a live web app—predicting dog boot sizes from harness measurements using Python, scikit-learn, and Streamlit.

---

## ✨ Features

- **Exploratory Data Analysis**  
  - Load and inspect 50 avalanche-rescue dog records  
  - Summary statistics, head/tail views, and scatter plots in both cm and inches  
- **Statistical Modeling**  
  - Linear regression (`LinearRegression`) with scikit-learn  
  - Printout of R² (≈ 0.57), slope, and intercept  
- **Interactive Web App**  
  - Streamlit UI with a harness-size slider  
  - Real-time boot-size predictions and sizing advice  

---

## 🚀 Live Demo

View the app in your browser:  
https://share.streamlit.io/bdeepika06/doggy-boot-predictor/main/app.py

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+  
- Git  

### 1. Clone this repository

```bash
git clone https://github.com/bdeepika06/doggy-boot-predictor.git  
cd doggy-boot-predictor
```

### 2. Create & activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
# .\venv\Scripts\Activate.ps1   # Windows PowerShell
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Explore the data

Launch Jupyter and run the EDA notebook:

```bash
jupyter notebook eda.ipynb
```

- Examine the dataset with `df.describe()`, `df.head()`, and `df.tail()`  
- View scatter plots for full data, filtered subset, and imperial-unit conversion  

### 5. Train the regression model

```bash
python train_model.py
```

- Prints R², slope, and intercept  
- Saves the trained model to `boot_model.pkl`  

### 6. Run the Streamlit app

```bash
streamlit run app.py
```

- Open `http://localhost:8501` in your browser  
- Adjust the harness-size slider and see live boot-size predictions and sizing advice  

---

## 📂 Repository Structure

```
doggy-boot-predictor/
├── eda.ipynb                # Exploratory Data Analysis notebook
├── doggy-boot-harness.csv   # Original CSV data (harness & boot sizes)
├── train_model.py           # Script to train & save the regression model
├── boot_model.pkl           # Serialized trained LinearRegression model
├── app.py                   # Streamlit web application
├── requirements.txt         # Python dependencies
└── README.md                # Project overview, setup, and usage
```

---

## 🤝 Acknowledgments

- **Microsoft Learn** “Introduction to Machine Learning” module for the tutorial dataset and exercises  
- **scikit-learn** for easy linear regression  
- **Streamlit** for rapid interactive app development  

---

Feel free to **fork**, **modify**, and **share** your improvements!
