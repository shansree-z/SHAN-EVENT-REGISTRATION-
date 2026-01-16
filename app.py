import streamlit as st

# CSS for the Bold Gradient
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}
[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 30px;
}
</style>
""", unsafe_allow_html=True)

st.title("🚀 Global Tech Registration")

with st.form("my_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    event = st.selectbox("Event", ["AI Summit", "Coding Hackathon"])
    submit = st.form_submit_button("Register")
    
    if submit:
        st.success(f"Awesome, {name}! You're on the list.")

