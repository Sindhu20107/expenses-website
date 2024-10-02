import streamlit as st
import pandas as pd
import os

folder_path = "data"
file_path = r"data/feedback.csv"

# Create folder and CSV file if not exists
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

if not os.path.exists(file_path):
    feedback_data = pd.DataFrame(columns=["Name", "Feedback", "Rating"])
    feedback_data.to_csv(file_path, index=False)


# Function to clear input fields
def clear():
    st.session_state.name = ""
    st.session_state.feedback = ""
    st.session_state.rating = 1


# Function to insert feedback into the CSV
def insert(name, feedback, rating):
    df = pd.read_csv(file_path)
    length = len(df)
    if name != "" and feedback != "" and 1 <= rating <= 5:
        df.loc[length] = [name, feedback, rating]
        df.to_csv(file_path, index=False)
        st.success('Thank you for your feedback!')
        st.balloons()
    else:
        st.error(
            'Please provide your name, feedback, and a rating between 1 and 5.'
        )


# User Input Fields
st.title("Feedback Form")

name = st.text_input("Enter your name", key='name')
feedback = st.text_area('Please provide your feedback', key='feedback')
rating = st.slider("Please provide a rating on a scale of 1 - 5",
                   1,
                   5,
                   key='rating')

# Buttons for Submit and Clear
col1, col2 = st.columns([0.24, 0.9])

with col1:
    submit = st.button("Submit 😊")
with col2:
    clear_button = st.button("Clear ✂️", on_click=clear)

# Add feedback to the CSV if the user clicks submit
if submit:
    insert(name, feedback, rating)
st.subheader("Past Feedback")
df = pd.read_csv(file_path)
st.dataframe(df)