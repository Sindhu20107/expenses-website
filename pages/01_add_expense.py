#add_expenses
import streamlit as st
import pandas as pd
import os

folder_path="data"
file_path=r"data/expense.csv"

if not os.path.exists(folder_path):
  os.makedirs(folder_path)

if not os.path.exists(file_path):
  expenses=pd.DataFrame(columns=["Date","Category","Description","Currency Type", "Amount"])
  expenses.to_csv(file_path,index=False)
  
def clear():
  st.session_state.desc=""
  st.session_state.amt=0

def insert(date,category,description,currency_type,amount):
  df=pd.read_csv(file_path)
  length=len(df)
  if description!="" and amount>0:
    df.loc[length]=[date,category,description, currency_type, amount]
    df.to_csv(file_path,index=False)
    st.balloons()
  else:
    st.error(
      'Please provide a description and a valid amount value greater than zero', icon="🚨")



date = st.date_input("Date: 	:calendar:")
category = st.selectbox("Category", [
    "Housing", "Food", "Transport", "Entertainment", "Shopping", "Insurance",
    "Debt Payments", "Personal Care", "Education", "Savings", "Taxes",
    "Miscellaneous"
])
description = st.text_area('Description:flashlight:', key='desc')
currency_type = st.selectbox("Currency Type 	:heavy_dollar_sign:", ["USD", "INR", "EUR"])
amount = st.number_input("Amount	:moneybag:", key='amt')

col1, col2 = st.columns([0.3, 0.7])
with col1:
  add_expense = st.button("Add expense :money_with_wings:")
with col2:
  clear_button = st.button("Clear:scissors:", on_click=clear)

if add_expense:
  insert(date,category, description, currency_type, amount)
