import streamlit as st

st.write("Hello World")
st.write("how do I stop this session?")
st.write("try again...")
st.write("Today is Thursday")

st.header("This is header")
st.subheader("This is subheader")
st.caption("This is caption")

st.markdown("*Streamlit* is **really** ***cool***")
st.markdown(''' :red[Streamlit] :orange[is] :green[fun]''')
st.markdown("Here's a bouquet &mdash;\ :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 36px;">This is advanced font manipulation!</p>'
st.markdown(new_title, unsafe_allow_html=True)

#selection box
st.selectbox("Kuala Lumpur is located at", ['Malaysia', 'Thailand', 'UK'])
st.multiselect("Select 2 states", ['Selangor','Johor','Kedah'])

#button
st.button("Click Here to Proceed")
st.slider("Select the length of stay", 1,10, value=3)

#input box
number = st.number_input("Insert a number", value=None, placeholder="Type a number...")
st.write("The current number is ", number)

#insert graphic
from PIL import Image
im = Image.open('shrdc_logo.png')
st.image(im, width=300)

#dataframe
import pandas as pd
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)

#barchart
st.bar_chart(df, x="Location", y="Income")

#linechart
st.line_chart(df, x="Household", y="Month Fees")

#scatterchart
st.scatter_chart(df, x="Household", y="Income")

#multi-tabpage
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

#multi-columns
col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

import pandas as pd
df = pd.read_excel('banking.csv')
st.dataframe(df)