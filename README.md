# 🏦 Loan Approval Prediction

## 📌 About
This project is a **Machine Learning-based Loan Approval Prediction System** designed to help financial institutions determine whether a loan application should be **approved (Y)** or **rejected (N)** based on applicant details.

---

## 🔑 Key Features
- ✅ **Automated Model Selection**  
  Utilizes **GridSearchCV** to automatically find the best algorithm and parameters.

- ✅ **Preprocessing Pipeline**  
  Handles log transformations and feature encoding for clean and efficient data processing.

- ✅ **Interactive Web App**  
  Built with **Streamlit**, enabling users to input data and receive real-time predictions.

- ✅ **Model Persistence**  
  Best-trained model saved as a `.pkl` file for easy production deployment.


  ## Live
  Code version is live [here](https://loan-prediction-9pmmuclvj2mkahowbvpsrz.streamlit.app/)

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/loan-approval-prediction.git
cd loan-approval-prediction
```

## Install Dependencies

```
pip intall -r requirement

```

## Project Structure
loan-approval-prediction/
├── data/
│   └── loan_data.csv          # Loan application records  
├── models/
│   └── best_loan_model.pkl    # Trained model  
├── app.py                     # Streamlit application  
├── model_training.py          # Training script  
└── README.md                  # Documentation  

