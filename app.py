import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('customer_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the scaler (assumes you've saved it as 'scaler.pkl')
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

st.title('Customer Churn Prediction')

# --- User Inputs ---
gender = st.selectbox('Select Gender', ['Male', 'Female'])
senior = st.selectbox('Senior Citizen', [0, 1])
partner = st.selectbox('Do you have a partner?', ['Yes', 'No'])
dependents = st.selectbox('Do you have any dependents?', ['Yes', 'No'])
phoneservice = st.selectbox('Do you have phone service?', ['Yes', 'No'])
multiplelines = st.selectbox('Do you have multiple lines?', ['Yes', 'No', 'No phone service'])
internetservice = st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'])
onlinesecurity = st.selectbox('Online Security', ['Yes', 'No', 'No internet service'])
onlinebackup = st.selectbox('Online Backup', ['Yes', 'No', 'No internet service'])
deviceprotection = st.selectbox('Device Protection', ['Yes', 'No', 'No internet service'])
techsupport = st.selectbox('Tech Support', ['Yes', 'No', 'No internet service'])
streamingtv = st.selectbox('Streaming TV', ['Yes', 'No', 'No internet service'])
streamingmovies = st.selectbox('Streaming Movies', ['Yes', 'No', 'No internet service'])
contract = st.selectbox('Contract Type', ['Month-to-month', 'One year', 'Two year'])
paperlessbilling = st.selectbox('Paperless Billing', ['Yes', 'No'])
paymentmethod = st.selectbox('Payment Method', [
    'Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'
])
totalcharges = st.number_input('Total Charges', min_value=0.0)
tenure = st.slider('Tenure (in months)', 0, 72, 1)
monthlycharges = st.number_input('Monthly Charges', min_value=0.0)

# --- Encoding input (this must match how you trained your LabelEncoders) ---

# Manual encoding (should match LabelEncoder transforms)
def encode(val, mapping):
    return mapping[val]

# Create mapping based on your LabelEncoder training
gender_map = {'Male': 1, 'Female': 0}
partner_map = {'Yes': 1, 'No': 0}
dependents_map = {'Yes': 1, 'No': 0}
phoneservice_map = {'Yes': 1, 'No': 0}
multiplelines_map = {'No': 0, 'Yes': 1, 'No phone service': 2}
internet_map = {'DSL': 0, 'Fiber optic': 1, 'No': 2}
online_map = {'Yes': 1, 'No': 0, 'No internet service': 2}
contract_map = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
paperless_map = {'Yes': 1, 'No': 0}
payment_map = {
    'Electronic check': 0,
    'Mailed check': 1,
    'Bank transfer (automatic)': 2,
    'Credit card (automatic)': 3
}

# Apply encoding
input_data = [
    encode(gender, gender_map),
    senior,
    encode(partner, partner_map),
    encode(dependents, dependents_map),
    tenure,
    encode(phoneservice, phoneservice_map),
    encode(multiplelines, multiplelines_map),
    encode(internetservice, internet_map),
    encode(onlinesecurity, online_map),
    encode(onlinebackup, online_map),
    encode(deviceprotection, online_map),
    encode(techsupport, online_map),
    encode(streamingtv, online_map),
    encode(streamingmovies, online_map),
    encode(contract, contract_map),
    encode(paperlessbilling, paperless_map),
    encode(paymentmethod, payment_map),
    monthlycharges,
    totalcharges
]

# --- Scale the data using the loaded StandardScaler ---
scaled_input = scaler.transform([input_data])

# --- Predict ---
if st.button('Predict'):
    prediction = model.predict(scaled_input)[0]
    if prediction == 1:
        st.error("This customer is likely to churn.")
    else:
        st.success("This customer is not likely to churn.")
