import streamlit as st
import requests

from config import API_URL


def upload_page():

    st.title(
        "📄 Add Herbal Data"
    )


    st.write(
        "Upload a JSON file containing herbal information."
    )


    uploaded_file = st.file_uploader(
        "Upload JSON file",
        type=["json"]
    )


    if uploaded_file:

        st.write(
            f"Selected file: "
            f"**{uploaded_file.name}**"
        )


        if st.button(
            "⬆️ Upload to Herbal Database",
            use_container_width=True
        ):

            with st.spinner(
                "Processing herbal data..."
            ):

                try:

                    response = requests.post(
                        f"{API_URL}/upload",
                        files={
                            "file": (
                                uploaded_file.name,
                                uploaded_file.getvalue(),
                                "application/json"
                            )
                        },
                        timeout=300
                    )


                    response.raise_for_status()


                    data = response.json()


                    if data.get("status") == "success":

                        st.success(
                            "Herbal data uploaded successfully!"
                        )


                        st.write(
                            f"**File:** "
                            f"{data.get('filename')}"
                        )


                        st.write(
                            f"**Plants loaded:** "
                            f"{data.get('plants_loaded')}"
                        )


                        st.write(
                            f"**Chunks created:** "
                            f"{data.get('chunks_created')}"
                        )


                    else:

                        st.error(
                            data.get(
                                "message",
                                "Upload failed."
                            )
                        )


                except requests.exceptions.ConnectionError:

                    st.error(
                        "Could not connect to FastAPI."
                    )


                except Exception as error:

                    st.error(
                        f"Error: {error}"
                    )