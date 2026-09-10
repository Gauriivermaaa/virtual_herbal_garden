import streamlit as st

from utils.html import flatten_html


def herb_card(
    herb,
    key
):

    name = herb.get(
        "name",
        "Unknown"
    )


    botanical = herb.get(
        "botanical_name",
        "Not available"
    )


    family = herb.get(
        "family",
        "Not available"
    )


    st.markdown(
        flatten_html(
            f"""
            <div class="herb-card">
                <div class="herb-name">
                    🌿 {name}
                </div>
                <div class="herb-info">
                    <p>
                        <strong>Botanical Name</strong>
                        <br>
                        <em>{botanical}</em>
                    </p>
                    <p>
                        <strong>Plant Family</strong>
                        <br>
                        {family}
                    </p>
                </div>
            </div>
            """
        ),
        unsafe_allow_html=True
    )


    if st.button(
        "View Plant Details 🌱",
        key=key,
        use_container_width=True
    ):

        st.session_state.selected_herb = herb

        st.session_state.page = "Herb"

        st.rerun()