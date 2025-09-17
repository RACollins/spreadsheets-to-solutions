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

    summary_page = st.Page(
        "pages/summary.py",
        title="Summary",
        icon=":material/person:",
        default=True,
    )
    bugs_page = st.Page(
        "pages/bugs.py", title="Bug reports", icon=":material/bug_report:"
    )
    alerts_page = st.Page(
        "pages/alerts.py",
        title="System alerts",
        icon=":material/notification_important:",
    )

    search_page = st.Page("pages/search.py", title="Search", icon=":material/search:")
    history_page = st.Page(
        "pages/history.py", title="History", icon=":material/history:"
    )

    if st.session_state.logged_in:
        pg = st.navigation(
            {
                "Account": [logout_page],
                "Reports": [summary_page, bugs_page, alerts_page],
                "Tools": [search_page, history_page],
            }
        )
    else:
        pg = st.navigation([login_page])

    pg.run()


if __name__ == "__main__":
    main()
