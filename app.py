import streamlit as st
import requests

# 1. UI Styling (Red & Black Gradient)
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

st.title("🔥 ShanEventz Registration")

# Google Form Submission URL (Change 'viewform' to 'formResponse')
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc88KKudFh42JScl6jNf_mchbespeaIChDLrv7OSmMfYmx1uA/formResponse"

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

    st.write("### Select Your Events")
    tech = st.multiselect("Technical", ["Coding War", "AI Hackathon", "Web Design", "Robot Race", "Data Quiz"])
    non_tech = st.multiselect("Non-Technical", ["Photography", "Gaming (BGMI)", "Standup Comedy", "Treasure Hunt"])

    if st.form_submit_button("REGISTER NOW"):
        if fname and email:
            # Mapping data to your Google Form IDs
            form_data = {
                "entry.290432123": fname,
                "entry.37629806": lname,
                "entry.1833594203": age,
                "entry.1720808553": str(dob),
                "entry.743410951": phone,
                "entry.1526759683": email,
                "entry.1830788331": tech, # Multiselects work as lists
                "entry.1742901975": non_tech
            }
            
            try:
                # Sending the data
                response = requests.post(FORM_URL, data=form_data)
                st.success(f"🎉 Success! {fname}, your registration is recorded.")
                st.balloons()
            except:
                st.error("Submission failed. Check your internet connection.")
        else:
            st.error("Please fill in the required fields!")
            
