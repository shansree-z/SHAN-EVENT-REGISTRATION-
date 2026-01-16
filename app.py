import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. VISUALS: Bold Red/Black Gradient
st.markdown("""
<style>
.stApp { background: linear-gradient(135deg, #000000 0%, #8b0000 100%); color: white; }
[data-testid="stForm"] {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    border: 1px solid #ff0000;
    padding: 25px;
}
label { color: #ff4b4b !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

st.title("ShanEventz Registration")

# 2. GOOGLE SHEETS CONNECTION
conn = st.connection("gsheets", type=GSheetsConnection)

with st.form("registration_form"):
    col1, col2 = st.columns(2)
    with col1:
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        age = st.number_input("Age", 1, 100)
    with col2:
        email = st.text_input("Email ID")
        phone = st.text_input("Phone Number")
        dob = st.date_input("Date of Birth")

    st.write("### Choose Your Tracks")
    tech = st.multiselect("Technical", ["Coding War", "AI Hackathon", "Web Design", "Robot Race", "Data Quiz"])
    non_tech = st.multiselect("Non-Technical", ["Photography", "Gaming (BGMI)", "Standup Comedy", "Treasure Hunt", "Film Making"])

    if st.form_submit_button("REGISTER"):
        if fname and email and (tech or non_tech):
            # Format data for the sheet
            new_row = pd.DataFrame([{
                "First Name": fname, "Last Name": lname, "Age": age,
                "Date of Birth": str(dob), "Phone Number": phone, "Email ID": email,
                "Technical Events": ", ".join(tech), "Non-Technical Events": ", ".join(non_tech)
            }])
            
            # Read existing, append new, and update
            existing_data = conn.read()
            updated_df = pd.concat([existing_data, new_row], ignore_index=True)
            conn.update(data=updated_df)
            
            st.success(f"Successfully Registered, {fname}!")
            st.balloons()
        else:
            st.error("Please fill required fields!")
            
