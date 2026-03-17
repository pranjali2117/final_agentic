import streamlit as st

def apply_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        
        html, body, [class*="st-"] {
            font-family: 'Poppins', sans-serif;
        }
        
        .main { 
            background: linear-gradient(135deg, #1e1e2f 0%, #121212 100%);
            color: #ffffff;
        }
        
        .auth-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding-top: 50px;
        }
        
        .auth-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(10px);
            padding: 40px;
            border-radius: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            width: 100%;
            max-width: 450px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        }
        
        .stButton>button { 
            width: 100%; 
            border-radius: 10px; 
            height: 3.5rem; 
            background: linear-gradient(90deg, #00d2ff 0%, #3a7bd5 100%); 
            color: white; 
            font-weight: 600;
            border: none;
            transition: transform 0.2s ease;
        }
        
        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 5px 15px rgba(0, 210, 255, 0.4);
        }

        .secondary-button>button {
            background: transparent !important;
            border: 1px solid rgba(255, 255, 255, 0.3) !important;
            color: #ffffff !important;
            height: 3rem !important;
            margin-top: 10px;
        }

        h1, h2, h3 {
            color: #ffffff !important;
            text-align: center;
        }
        
        .stTextInput>div>div>input {
            background-color: rgba(255, 255, 255, 0.07) !important;
            color: white !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            border-radius: 10px !important;
            height: 3rem;
        }

        .stDivider {
            border-bottom: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
    </style>
    """, unsafe_allow_html=True)

def navbar():
    with st.sidebar:
        st.markdown("## 🏏 Sportlytics")

        if st.session_state.logged_in:

            if st.button("🏠 Home"):
                st.session_state.page = "Home"
                st.rerun()

            if st.button("📂 History"):
                st.session_state.page = "History"
                st.rerun()

            if st.button("🚪 Login"):
                st.session_state.logged_in = False
                st.session_state.user = None
                st.session_state.page = "Login"
                st.rerun()

        else:

            if st.button("🔐 Login"):
                st.session_state.page = "Login"
                st.rerun()

            if st.button("📝 Signup"):
                st.session_state.page = "Signup"
                st.rerun()