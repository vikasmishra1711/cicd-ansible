import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Simple Streamlit App", page_icon="🚀")

# 2. Header and Title
st.title("Welcome to My Streamlit App")
st.write("This is a simple, pure Streamlit web interface.")

st.divider()

# 3. User Input Section
st.header("Interactive Widgets")

# Text Input
user_name = st.text_input("Enter your name:", placeholder="Type here...")

# Slider Input
age = st.slider("Select your age:", min_value=0, max_value=100, value=25)

# 4. Action Button and Output
if st.button("Submit"):
    if user_name:
        st.success(f"Hello {user_name}! You are {age} years old.")
        st.balloons()
    else:
        st.warning("Please enter a name before clicking submit.")

st.divider()

# 5. Sidebar Section
st.sidebar.header("Sidebar Settings")
st.sidebar.write("This content appears in the sidebar.")
theme_choice = st.sidebar.selectbox("Choose a vibe:", ["Energetic", "Calm", "Professional"])
st.sidebar.write(f"You selected: **{theme_choice}**")