# Customer Churn Prediction 🎯

This project predicts whether a customer is likely to **churn (leave the telecom company)** or **stay**, based on their service usage and profile. It uses **Logistic Regression** for binary classification and is deployed as a web app using **Streamlit**.

---

## 📌 Problem Statement

Telecom companies often struggle with customer churn. Retaining customers is cheaper than acquiring new ones, so being able to predict churn is valuable. This model helps the company identify customers at risk of leaving based on features like contract type, monthly charges, internet service, etc.

---

## 🚀 Technologies Used

* Python
* Pandas & NumPy
* Scikit-learn
* Streamlit
* Pickle / Joblib

---

## 📁 Dataset Features

The dataset contains the following features:

| Feature            | Description                                         |
| ------------------ | --------------------------------------------------- |
| `gender`           | Customer gender (Male/Female)                       |
| `SeniorCitizen`    | Whether the customer is a senior citizen (1/0)      |
| `Partner`          | Whether the customer has a partner (Yes/No)         |
| `Dependents`       | Whether the customer has dependents (Yes/No)        |
| `tenure`           | Number of months the customer has stayed            |
| `PhoneService`     | Whether the customer has phone service (Yes/No)     |
| `MultipleLines`    | Whether the customer has multiple lines             |
| `InternetService`  | Type of internet service                            |
| `OnlineSecurity`   | Whether the customer has online security            |
| `OnlineBackup`     | Whether the customer has online backup              |
| `DeviceProtection` | Whether the customer has device protection          |
| `TechSupport`      | Whether the customer has tech support               |
| `StreamingTV`      | Whether the customer streams TV                     |
| `StreamingMovies`  | Whether the customer streams movies                 |
| `Contract`         | Type of contract (Month-to-month/One year/Two year) |
| `PaperlessBilling` | Whether billing is paperless                        |
| `PaymentMethod`    | Customer’s payment method                           |
| `MonthlyCharges`   | Amount charged monthly                              |
| `TotalCharges`     | Total amount charged over the tenure                |
| `Churn`            | Target variable – Yes (1), No (0)                   |

---

## 🧠 Model Training

* All categorical columns were encoded using `LabelEncoder`
* Features were scaled using `StandardScaler`
* Logistic Regression was used for training the model
* The trained model and scaler were saved using `pickle`

---

## 🖥️ Streamlit Web App

The web app allows users to:

* Input customer data using dropdowns and sliders
* Get real-time predictions on churn
* View a clear message: “Customer is likely to churn” or “Customer is not likely to churn”

---

## 📦 Files in This Repository

* `app.py`: Streamlit app code
* `customer_model.pkl`: Trained Logistic Regression model
* `scaler.pkl`: StandardScaler used for feature scaling
* `requirements.txt`: Required packages for the project
* `README.md`: Project description and setup instructions

---

## 📂 How to Run the Project Locally

1. Clone the repo:

   ```
   git clone https://github.com/your-username/customer-churn-prediction.git
   cd customer-churn-prediction
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Run the app:

   ```
   streamlit run app.py
   ```

---

## 🌐 Live App

You can try the deployed app here:
**\[https://customerchurnprediction-ufqpst4of6yzu79lmxpkbf.streamlit.app/]**

---

