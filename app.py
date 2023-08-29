import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('https://github.com/aloksharma-1/Credit-card-fraud-detection-Full-project/blob/main/pipe.pkl','rb'))

# Set the app title
st.title('Machine Learning Model')

guidelines = 'Input for "Type" of Transaction is not case sensitive,\nThe allowed inputs are:- \n["payment", "transfer", "cash_in", "cash_out", "debit"]'
st.warning(guidelines)
# Create input fields for user to enter values

ttype= st.text_input('Type')
amount = st.text_input('Amount:')
oldbalance = st.text_input('Old Balance:')
newbalance = st.text_input('New Balance:')
newbalanceDest=st.text_input('New Balance Dest:')
oldbalanceDest=st.text_input('Old  Balance Dest:')

ttype = ttype.upper()
type_payment = ['CASH_IN','CASH_OUT','DEBIT','PAYMENT', 'TRANSFER']
for i in range(len(type_payment)):
    if ttype == type_payment[i]:
        paymentType = i
# Create a button to trigger the prediction
if st.button('Predict'):
    # Prepare the input data for prediction
    data = pd.DataFrame({
        'type':[paymentType],
        'amount': [float(amount)],
        'oldbalanceOrg': [float(oldbalance)],
        'newbalanceOrig': [float(newbalance)],
        'oldbalanceDest': [float(oldbalanceDest)],
        'newbalanceDest': [float(newbalanceDest)],
    })  
    st.write(data)

    # Make the prediction using the loaded model
    prediction = model.predict(data)
    if prediction[0] == 0.:
        st.success('Transaction is Geniune !!')
    else:
        st.success('Transaction is Fishy')

    # Display the prediction result
    st.success('Prediction: {}'.format(prediction[0]))
   
