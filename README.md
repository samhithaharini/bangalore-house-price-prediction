#  Bangalore House Price Prediction (Batch Gradient Descent)

This project predicts house prices based on **area (sq ft)** and **number of bedrooms** using a model built from scratch with **Batch Gradient Descent** and deployed using **Streamlit**.

---

##  Overview

- Input: Area (sq ft), Bedrooms  
- Output: Predicted house price (in Lakhs)  
- Model: Linear Regression (implemented manually)  
- Optimization: Batch Gradient Descent  

---

##  Model Logic

The model follows a simple linear equation:

price = w1 * area + w2 * bedrooms + b

- Entire dataset is used in each iteration  
- Loss function: Mean Squared Error (MSE)  
- Parameters updated using gradient descent  

---

## ⚙️ Tech Stack

- Python  
- NumPy  
- Pandas  
- Scikit-learn (for scaling only)  
- Streamlit  

---


## ⚠️ Limitations

- Small dataset (20 samples)  
- Linear model (cannot capture complex relationships)  
- Predictions may vary for extreme inputs  

---

