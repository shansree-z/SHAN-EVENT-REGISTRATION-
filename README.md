# ShanEventz Registration Website 

[![Python](https://img.shields.io/badge/PYTHON-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/STREAMLIT-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![GitHub](https://img.shields.io/badge/GITHUB-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/)
![Live App](https://img.shields.io/badge/LIVE_APP-FF4B4B?style=for-the-badge)

> **A high-performance, serverless event registration portal with a premium Glassmorphism UI.**

---

## 🚀 Live Demo
Access the live application here:  
👉 **[ShanEventz Live Portal](https://qz39wrtk9q7rts43lpocje.streamlit.app/)**

---

## 📖 Project Overview
ShanEventz is a custom-branded web application designed for seamless attendee registration. By integrating a **Streamlit** frontend with a **Google Forms** backend, the system achieves a secure, low-latency data pipeline without the need for expensive database hosting.

---

## ✨ Key Features
* **Modern Aesthetic:** Bold Red & Black gradient background with Glassmorphism UI effects.
* **White-Label Experience:** Custom CSS overrides to hide default Streamlit headers and GitHub branding for a professional look.
* **Smart Data Pipeline:** Real-time data synchronization with Google Sheets via HTTP POST requests.
* **Categorized Selection:** Multiselect interface for Technical and Non-Technical event tracks.
* **Responsive Design:** Optimized for both desktop and mobile browsers.

---

## 🏗️ Technical Architecture
This project follows a **Serverless Architecture**:
* **Frontend:** [Streamlit](https://streamlit.io/) (Python) for UI rendering and state management.
* **Transport:** Python `requests` library for secure data transmission.
* **Backend Storage:** Google Forms API (formResponse) & Google Sheets for data persistence and easy management.

---

## 🗂️ Repository Contents
* `app.py`: The core application script featuring custom CSS and submission logic.
* `requirements.txt`: Necessary dependencies (`streamlit`, `requests`).
* `README.md`: Technical documentation and architecture overview.

---

## ⚙️ Setup & Installation

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/shansree-z/event-registration.git](https://github.com/shansree-z/event-registration.git)
    cd event-registration
    ```

2.  **Create a Virtual Environment (Optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuration:**
    Open `app.py` and replace the Google Form entry IDs and URL with your own to connect it to your specific Google Sheet.

5.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```

---

## 🛠️ Technologies Used
* **Python 3.9+**
* **Streamlit** (UI Framework)
* **Pandas** (Data Handling)
* **Requests** (API communication)
* **CSS3** (Custom Styling & Glassmorphism)

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/shansree-z/event-registration/issues).

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).

Developed with ❤️ by [Shansree-z](https://github.com/shansree-z)
