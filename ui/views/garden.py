import streamlit as st

from utils.herb_loader import load_herbs
from utils.html import flatten_html
from components.cards import herb_card


def garden_page():

    herbs = load_herbs()

    st.markdown(
        flatten_html(
            f"""
            <div class="hero-banner">
                <div class="hero-title">🌱 Virtual Herbal Garden</div>
                <p class="hero-subtitle">
                    {len(herbs) if herbs else 0} medicinal plants catalogued and ready to explore.
                </p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    if not herbs:
        st.warning("No herbs available.")
        return

    search_text = st.text_input("🔍 Search for a herb", placeholder="Try Tulsi...")

    if search_text:
        herbs = [
            herb for herb in herbs
            if search_text.lower() in herb.get("name", "").lower()
        ]
        if not herbs:
            st.info(f'No herbs matching "{search_text}".')
            return

    st.write("")

    for i in range(0, len(herbs), 3):
        columns = st.columns(3, gap="large")
        for index, (column, herb) in enumerate(zip(columns, herbs[i:i + 3])):
            with column:
                herb_card(herb=herb, key=f"herb_{i}_{index}")

    st.markdown(
        '<div class="app-footer">🌿 Virtual Herbal Garden — Streamlit · FastAPI · RAG</div>',
        unsafe_allow_html=True,
    )