import streamlit as st


def _pill(label, value):
    st.markdown(
        f'<span class="property-pill"><strong>{label}:</strong> {value}</span>',
        unsafe_allow_html=True,
    )


def herb_page():

    herb = st.session_state.get("selected_herb")

    if not herb:
        st.session_state.page = "Garden"
        st.rerun()

    name = herb.get("name", "Unknown")

    st.markdown(
        f"""
        <div class="hero-banner">
            <div class="hero-title">🌿 {name}</div>
            <p class="hero-subtitle"><em>{herb.get('botanical_name', '')}</em></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="section-title">🌱 Basic Information</div>
                <p><strong>English name:</strong> {herb.get('english_name', 'N/A')}</p>
                <p><strong>Family:</strong> {herb.get('family', 'N/A')}</p>
                <p><strong>Parts used:</strong> {herb.get('part_used', 'N/A')}</p>
                <p><strong>Main indications:</strong> {herb.get('main_indications', 'N/A')}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        pills_html = "".join(
            f'<span class="property-pill"><strong>{label}:</strong> {herb.get(key, "N/A")}</span>'
            for label, key in [
                ("Rasa", "rasa"),
                ("Guna", "guna"),
                ("Virya", "virya"),
                ("Vipaka", "vipaka"),
            ]
        )
        st.markdown(
            f"""
            <div class="properties-panel">
                <div class="section-title">🌿 Ayurvedic Properties</div>
                {pills_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")

    button_col1, button_col2 = st.columns(2)

    with button_col1:
        if st.button("🤖 Ask AI about this herb", use_container_width=True):
            st.session_state.page = "Chat"
            st.session_state.herb_question = (
                f"What are the therapeutic uses of {name}?"
            )
            st.rerun()

    with button_col2:
        if st.button("← Back to Garden", use_container_width=True):
            st.session_state.page = "Garden"
            st.rerun()