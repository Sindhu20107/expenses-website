import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#st.set_option('deprecation.showPyplotGlobalUse', False)
excel_file_path = "data/expense.csv"

def execution():
    try:
        dataframe = pd.read_csv(excel_file_path)

        if len(dataframe) == 0:
            st.header("No data available. Please add some expenses before analyzing.")
            return

        # Find the maximum spending
        max_Amount = dataframe[dataframe["Amount"] == dataframe["Amount"].max()]
        st.subheader("You are spending the most here :cry:")
        st.dataframe(max_Amount.reset_index(drop=True))

        # Find the minimum spending
        min_Amount = dataframe[dataframe["Amount"] == dataframe["Amount"].min()]
        st.subheader("You are spending the least here :blush:")
        st.dataframe(min_Amount.reset_index(drop=True))

        # Date with most transactions
        most_transactions_date = dataframe.groupby("Date").size().nlargest(1)
        st.subheader("You made the most number of transactions on :date:")
        st.dataframe(most_transactions_date.reset_index(name='Transactions'))

        # Date with least transactions
        least_transactions_date = dataframe.groupby("Date").size().nsmallest(1)
        st.subheader("You made the least number of transactions on :date:")
        st.dataframe(least_transactions_date.reset_index(name='Transactions'))

        # Most common category
        mode_Category = dataframe["Category"].mode()
        st.subheader("The categories for which you are spending the most :cry:")
        st.dataframe(mode_Category.reset_index(drop=True))

        # Least common category
        least_spent_category = dataframe['Category'].value_counts().idxmin()
        st.subheader("The categories for which you are spending the least :blush:")
        st.dataframe(dataframe[dataframe['Category'] == least_spent_category]["Category"].reset_index(drop=True))

        # Word cloud from descriptions
        Description_data = ' '.join(list(dataframe["Description"].values))

        def generate_wordcloud(text):
            # wordcloud = WordCloud(width=400, height=400, background_color='white').generate(text)
            # plt.imshow(wordcloud, interpolation='bilinear')
            # plt.axis('off')
            # st.pyplot()
            fig, ax = plt.subplots(figsize=(8, 8)) # Create a figure and axis 
            wordcloud = WordCloud(width=400, height=400, background_color='white').generate(text) 
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off') 
            st.pyplot(fig)

        st.subheader("Description cloud :cloud:")
        generate_wordcloud(Description_data)

    except FileNotFoundError:
        st.header("File not found. Please add some expenses before analyzing.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

execution()
