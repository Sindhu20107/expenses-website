import streamlit as st

tab1, tab2, tab3 = st.tabs(['About', 'Hobbies', 'Contact'])

with tab1:
  col1, col2 = st.columns([0.3, 0.7])
  with col1:
    st.image("pikachu.webp")
  st.subheader("Sindhu Adhikari:sunglasses:")

  with col2:
    st.write(
        "Hi, My name is Sindhu Adhikari and I am 14 years old. I've created a website to help people track and manage they're expenses. I think this website was important and needed to be created because many people struggle with keeping track of they're finances and money. I hope you enjoy this website! Thank you!")
with tab2:
  st.write("I love to hang out with friends and watch shows. I also enjoy dancing and playing tennis.:tennis:")

with tab3:
  st.write("You can contact me at sindhu.adhikari77@gmail.com")
  st.write("Website: Sindhu's website.com")
