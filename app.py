import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

login_page = st.Page("pages/login.py", title="Log in", icon=":material/login:")
logout_page = st.Page("pages/logout.py", title="Log out", icon=":material/logout:")

dashboard_page = st.Page(
    "pages/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
bugs_page = st.Page("pages/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts_page = st.Page(
    "pages/alerts.py", title="System alerts", icon=":material/notification_important:"
)

search_page = st.Page("pages/search.py", title="Search", icon=":material/search:")
history_page = st.Page("pages/history.py", title="History", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard_page, bugs_page, alerts_page],
            "Tools": [search_page, history_page],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
