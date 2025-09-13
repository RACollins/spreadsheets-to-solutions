import streamlit as st


def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()


def main():
    left_margin, main_content, right_margin = st.columns([1, 5, 1])
    with main_content:
        logo = st.image(
            "data/assets/marketing-magic-high-resolution-logo-transparent.png"
        )
        login()


if __name__ == "__main__":
    main()
