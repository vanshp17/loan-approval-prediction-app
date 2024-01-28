import streamlit as st 
import pandas as pd 
import pickle as pk 

model = pk.load(open('loan.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

st.header('Loan Approval App')

no_of_dep = st.slider('choose No of Dependent', 0, 5)
grad = st.selectbox('choose Education',['Graduate','Not Graduate'])
self_emp = st.selectbox('choose self employed?',['Yes','No'])
annual_income = st.slider('choose Annual Income', 0, 10000000)
loan_amount = st.slider('choose Loan Amount', 0, 10000000)
loan_dur = st.slider('choose Loan Duration', 0, 20)
cibil_score = st.slider('choose Cibil Score', 0, 1000)
assets = st.slider('choose Assets', 0, 10000000)


if grad=='Graducated':
    grad_s=1
else:
    grad_s=0

if self_emp=='Yes':
    self_emp_s=1
else:
    self_emp_s=0


if st.button('Predict'):
    pred_data = pd.DataFrame([[no_of_dep,grad_s,self_emp_s,annual_income,loan_amount,loan_dur,cibil_score,assets]],
                         columns=['no_of_dependents',	'education',	'self_employed',	'income_annum',	'loan_amount',	'loan_term',	'cibil_score','assets'])
    

    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)

    if predict[0] == 1:
        st.markdown('Loan Is Approved')
    else:
        st.markdown('Loan Is Rejected')
