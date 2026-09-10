import streamlit as st


NAV_ITEMS = [
    ("Home", "🏡", "Home"),
    ("Garden", "🌱", "Garden"),
    ("Herbal AI", "🤖", "Chat"),
    ("Add Data", "📄", "Upload"),
]


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div class="sidebar-logo">
                <span class="sidebar-logo-icon">🌿</span>
                <div>
                    <div style="font-family:'Fraunces',serif; font-size:1.15rem; font-weight:600;">
                        Herbal Garden
                    </div>
                    <span class="sidebar-badge">v1.0 · RAG</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("---")

        current_page = st.session_state.get("page", "Home")

        for label, icon, target in NAV_ITEMS:

            is_current = current_page == target

            if st.button(
                f"{icon}  {label}",
                key=f"nav_{target}",
                use_container_width=True,
                type="primary" if is_current else "secondary",
            ):
                st.session_state.page = target
                st.rerun()

        st.write("")
        st.markdown("---")

        if st.button("Log out", key="logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.page = "Home"
            st.rerun()

        st.markdown(
            '<div style="font-size:0.72rem; color:rgba(246,241,228,0.4); '
            'margin-top:1rem;">Built with Streamlit + FastAPI + RAG</div>',
            unsafe_allow_html=True,
        )