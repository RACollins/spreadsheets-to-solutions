import streamlit as st
import time


def check_password():
    """Checks whether the user has entered the correct password."""
    if st.session_state.get("password"):
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False
    else:
        # No password entered
        st.session_state["password_correct"] = False
    return st.session_state["password_correct"]


def login():
    if not st.session_state.get("password_correct", False):
        st.text_input("Password", type="password", key="password")

        # Check if user pressed Enter (password field has value) or clicked login button
        login_button = st.button("Log in")
        login_triggered = login_button or st.session_state.get("password")

        if login_triggered:
            if check_password():
                st.session_state["password_correct"] = True
                st.session_state["logged_in"] = True
                del st.session_state["password"]  # don't keep password in session
                st.success("Logged in successfully")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Password incorrect")
                st.stop()


def main():
    left_margin, main_content, right_margin = st.columns([1, 1, 1])
    with main_content:
        st.image("data/assets/marketing-magic-high-resolution-logo-transparent.png")
        login()


if __name__ == "__main__":
    main()
