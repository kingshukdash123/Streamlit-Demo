import streamlit as st

st.title("Hello chai app")
st.subheader("Made with streamlit")
st.text("Welcome to your first interactive app")
st.write("Make your chai from our app")

name = st.text_input("Enter your name : ")
if name : 
    st.write(f"Welcome {name}")
date = st.date_input("Select today's date : ", value=None)
time = st.time_input("When to order : ")
chai = st.selectbox("Your fav chai : ", ["Choose one...", "Masala Chai", "Adrak Chai", "Special Chai", "kesar Chai"])
tea_type = st.radio("Pick your chai base : ", ["Milk", "Honey", "Water"])
masala = st.checkbox("Add masala")
suger = st.slider("Suger level : ", 0, 5, 2)
cupNumber = st.number_input("How many cups : ", min_value=1, max_value=10)
if st.button("Make Chai") :
    st.success("Congratulation! Your chai is ready.")


st.title("Vote for Chai")
col1, col2 = st.columns(2)
with col1 : 
    st.header("Masala Chai")
    st.image("https://www.shutterstock.com/image-photo/fresh-milk-masala-tea-indian-600nw-2498823945.jpg", width=200)
    vote1 = st.button("Vote for Masala Chai")
with col2 : 
    st.header("Adrak Chai")
    st.image("https://www.shutterstock.com/image-photo/fresh-milk-masala-tea-indian-600nw-2498823945.jpg", width=200)
    vote2 = st.button("Vote for Adrak Chai")   
if vote1 :
    st.success("Thanks for voting Masala Chai")
elif vote2 :
    st.success("Thanks for voting Adrak Chai")
st.sidebar.text_input("Enter your name")
st.sidebar.selectbox("Select your chai", ["Choose one...", "Masala Chai", "Adrak Chai", "Special Chai", "kesar Chai"])

with st.expander("Show chai making instruction") :
    st.write("""
    1. Boil water with tea leaves
    2. Add tea and milk
    3. Serve hot
""")
    
st.markdown('## markdown text')
st.markdown('> blockquote')