import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

file_path = r"data/expense.csv"


def execution():
  dataframe = pd.read_csv(file_path)

  total = dataframe["Amount"].max()
  st.subheader(f"Gold coins:{str(int(total)//200)}:coins:")

  date_from = st.date_input("From Date :date:")
  date_to = st.date_input("To Date :date:")

  st.write("Amount :money_with_wings:")
  amount_min = st.slider("Minimum value",
                         min_value=0,
                         max_value=20000,
                         value=0,
                         step=10)
  amount_max = st.slider("Maximum value",
                         min_value=0,
                         max_value=20000,
                         value=20000,
                         step=10)

  category = st.multiselect("Categories :card_index_dividers:", [
      "Housing", "Utilities", "Transportation", "Food", "Healthcare",
      "Insurance", "Debt Payments", "Entertainment", "Personal Care",
      "Education", "Savings", "Taxes", "Miscellaneous"
  ],
                            placeholder="You can choose multiple option(s)")

  dataframe["Date"] = pd.to_datetime(dataframe["Date"])
  date_from, date_to = pd.to_datetime(date_from), pd.to_datetime(date_to)
  st.title("Expenses :receipt:")
  st.dataframe(
      dataframe[["Category", "Description", "Currency Type",
                 "Amount"]].reset_index(drop=True))

  st.title("Amount :money_with_wings:")
  st.line_chart(dataframe["Amount"])

  st.title("Categories :card_index_dividers:")
  category_dataframe = dataframe.groupby('Category')['Amount'].sum()
  fig, ax = plt.subplots()
  ax.pie(category_dataframe,
         labels=category_dataframe.index,
         autopct='%.2f',
         textprops={
             'fontsize': 8.5,
             "color": "black"
         },
         shadow=True)
  fig.set_facecolor('none')
  st.pyplot(fig)
  if len(category) == 0:
    condition = ((dataframe["Date"] >= date_from) &
                 (dataframe["Date"] <= date_to) &
                 (dataframe["Amount"] >= amount_min) &
                 (dataframe["Amount"] <= amount_max))
    dataframe = dataframe[condition]
  else:
    condition = ((dataframe["Date"] >= date_from) &
                 (dataframe["Date"] <= date_to) &
                 (dataframe["Amount"] >= amount_min) &
                 (dataframe["Amount"] <= amount_max) &
                 (dataframe["Category"].isin(category)))
    dataframe = dataframe[condition]


try:
  execution()
except Exception as e:
  st.title("Please add some expenses :money_with_wings: ")
  st.write(e)
