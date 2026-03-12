import streamlit as st
import re
from database import add_user, check_user, reset_password

def validate_password(password):
    if len(password) < 4:
        return False, "Password must be at least 4 characters long."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, ""

def login_page():
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.title("🏏 Sportlytics")
        st.markdown("<p style='text-align: center; color: #aaa;'>Login to your account</p>", unsafe_allow_html=True)
        
        email = st.text_input("Email", placeholder="your@email.com")
        password = st.text_input("Password", type="password", placeholder="••••••••")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Login", key="login_btn"):
            if not email or not password:
                st.error("Please fill in all fields.")
            else:
                user = check_user(email, password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.user = user
                    st.session_state.page = "Home"
                    st.rerun()
                else:
                    st.error("Invalid email or password.")
        
        st.markdown('<div class="primary-button">', unsafe_allow_html=True)
        if st.button("Create new account", key="goto_signup"):
            st.session_state.page = "Signup"
            st.rerun()
        if st.button("Forgot Password?", key="goto_forgot"):
            st.session_state.page = "Forgot"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def signup_page():
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.title("📝 Join Sportlytics")
        st.markdown("<p style='text-align: center; color: #aaa;'>Start your sports analysis journey</p>", unsafe_allow_html=True)
        
        name = st.text_input("Full Name", placeholder="John Doe")
        email = st.text_input("Email", placeholder="john@example.com")
        password = st.text_input("Password", type="password", placeholder="Min. 4 chars, 1 num, 1 symbol")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Repeat password")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Sign Up", key="signup_btn"):
            if not all([name, email, password, confirm_password]):
                st.error("All fields are required.")
            elif password != confirm_password:
                st.error("Passwords do not match.")
            else:
                is_valid, msg = validate_password(password)
                if not is_valid:
                    st.error(msg)
                else:
                    if add_user(name, email, password):
                        st.success("Account created! Redirecting to login...")
                        st.session_state.page = "Login"
                        st.rerun()
                    else:
                        st.error("Email already registered.")
        
        st.markdown('<div class="secondary-button">', unsafe_allow_html=True)
        if st.button("Already have an account? Login", key="goto_login"):
            st.session_state.page = "Login"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def forgot_password_page():
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="auth-card">', unsafe_allow_html=True)
        st.title("🔄 Reset Access")
        st.markdown("<p style='text-align: center; color: #aaa;'>Enter your email to set a new password</p>", unsafe_allow_html=True)
        
        email = st.text_input("Email", placeholder="registered@email.com")
        new_password = st.text_input("New Password", type="password", placeholder="Min. 4 chars, 1 num, 1 symbol")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Reset Password", key="reset_btn"):
            is_valid, msg = validate_password(new_password)
            if not is_valid:
                st.error(msg)
            elif reset_password(email, new_password):
                st.success("Success! Redirecting to login...")
                st.session_state.page = "Login"
                st.rerun()
            else:
                st.error("Email not found.")
        
        st.markdown('<div class="secondary-button">', unsafe_allow_html=True)
        if st.button("Back to Login", key="back_login_btn"):
            st.session_state.page = "Login"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
