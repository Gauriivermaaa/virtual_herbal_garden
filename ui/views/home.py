import streamlit as st

from utils.herb_loader import load_herbs


def home_page():

    herbs = load_herbs() or []

    st.markdown(
        f"""
        <div class="hero-banner">
            <div class="hero-title">🌱 Explore Your Herbal Knowledge Journey</div>
            <p class="hero-subtitle">
                Browse medicinal plants, ask the Ayurveda-aware AI assistant,
                or expand the garden's knowledge base with your own data.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    stat_col1, stat_col2, stat_col3 = st.columns(3)

    with stat_col1:
        st.markdown(
            f'<div class="stat-chip"><span class="stat-number">{len(herbs)}</span>'
            '<span class="stat-label">Herbs Catalogued</span></div>',
            unsafe_allow_html=True,
        )
    with stat_col2:
        st.markdown(
            '<div class="stat-chip"><span class="stat-number">RAG</span>'
            '<span class="stat-label">AI Assistant</span></div>',
            unsafe_allow_html=True,
        )
    with stat_col3:
        st.markdown(
            '<div class="stat-chip"><span class="stat-number">Live</span>'
            '<span class="stat-label">Ayurvedic Data</span></div>',
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        st.markdown(
            '<div class="feature-card">'
            '<div class="feature-icon">🌱</div>'
            '<div class="feature-title">Explore Herbs</div>'
            '<div class="feature-text">Browse medicinal plants and discover their '
            'botanical information and herbal knowledge.</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        if st.button("Explore Garden 🌿", key="explore_garden", use_container_width=True):
            st.session_state.page = "Garden"
            st.rerun()

    with col2:
        st.markdown(
            '<div class="feature-card">'
            '<div class="feature-icon">🌿</div>'
            '<div class="feature-title">Herbal AI</div>'
            '<div class="feature-text">Ask questions and explore herbal knowledge '
            'using the RAG-powered AI assistant.</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        if st.button("Ask Herbal AI 🌿", key="herbal_ai", use_container_width=True):
            st.session_state.page = "Chat"
            st.rerun()

    with col3:
        st.markdown(
            '<div class="feature-card">'
            '<div class="feature-icon">📄</div>'
            '<div class="feature-title">Add Herbal Data</div>'
            '<div class="feature-text">Upload structured herbal information to expand '
            'the knowledge available in your garden.</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        if st.button("Add Herbal Data 📄", key="upload_data", use_container_width=True):
            st.session_state.page = "Upload"
            st.rerun()

    st.markdown(
        '<div class="app-footer">🌿 Virtual Herbal Garden — Streamlit · FastAPI · RAG</div>',
        unsafe_allow_html=True,
    )