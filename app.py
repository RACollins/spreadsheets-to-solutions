import streamlit as st

page_config = st.set_page_config(
    layout="wide",
    initial_sidebar_state="auto",
)


def main():
    """Main function to run the app."""

    st.logo(
        "data/assets/marketing-magic-high-resolution-logo-transparent.png", size="large"
    )

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    login_page = st.Page("pages/login.py", title="Log in", icon=":material/login:")
    logout_page = st.Page("pages/logout.py", title="Log out", icon=":material/logout:")

    home_page = st.Page("pages/home.py", title="Home", icon=":material/home:")

    summary_page = st.Page(
        "pages/summary.py",
        title="Summary",
        icon=":material/analytics:",
        default=True,
    )
    campaigns_page = st.Page(
        "pages/campaigns.py", title="Campaigns", icon=":material/campaign:"
    )

    if st.session_state.logged_in:
        pg = st.navigation(
            {
                "Home": [home_page],
                "Insights": [summary_page, campaigns_page],
                "Account": [logout_page],
            }
        )
    else:
        pg = st.navigation([login_page])

    pg.run()


if __name__ == "__main__":
    main()
