import streamlit as st
import requests

# 1. HIDE GITHUB HEADER & FORK ICON + STYLING
st.set_page_config(page_title="ShanEventz", layout="centered")

st.markdown("""
    <style>
    /* Hides the GitHub Fork icon and Streamlit header */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #GithubIcon {visibility: hidden;}

    /* Your Bold Red and Black Theme */
    .stApp { background: linear-gradient(135deg, #000000 0%, #8b0000 100%); color: white; }
    [data-testid="stForm"] {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        border: 1px solid #ff4b4b;
        padding: 25px;
    }
    label { color: #ff4b4b !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 ShanEventz Registration")

# 2. GOOGLE FORM SUBMISSION URL (Endpoint for data)
FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSc88KKudFh42JScl6jNf_mchbespeaIChDLrv7OSmMfYmx1uA/formResponse"

with st.form("registration_form", clear_on_submit=True):
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
    tech = st.multiselect("Technical", ["Coding War", "Ai Hackathon", "Web Design", "Robot Race", "Data Quiz"])
    non_tech = st.multiselect("Non-Technical", ["Photography", "Gaming (BGMI)", "Standup Comedy", "Treasure Hunt"])

    if st.form_submit_button("REGISTER NOW"):
        if fname and email:
            # Mapping to your exact Entry IDs
            # IMPORTANT: Multiselect values must be joined into one string
            form_payload = {
                "entry.290432123": fname,
                "entry.37629806": lname,
                "entry.1833594203": age,
                "entry.1720808553": str(dob),
                "entry.743410951": phone,
                "entry.1526759683": email,
                "entry.1830788331": ", ".join(tech),
                "entry.1742901975": ", ".join(non_tech)
            }
            try:
                # Using a timeout to prevent the app from hanging
                response = requests.post(FORM_URL, data=form_payload, timeout=10)
                if response.status_code == 200:
                    st.success(f"🎉 Success! {fname}, your registration is recorded.")
                    st.balloons()
                else:
                    st.error("Submission failed. Check if your Form is accepting responses.")
            except Exception as e:
                st.error("Network issue. Please try again.")
        else:
            st.error("Please fill in First Name and Email.")
            
