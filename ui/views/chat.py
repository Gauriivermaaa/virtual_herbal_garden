import streamlit as st
import requests

from config import API_URL


def chat_page():

    st.title(
        "🤖 Herbal AI Assistant"
    )


    st.write(
        "Ask questions about herbs and their therapeutic uses."
    )


    # SHOW PREVIOUS MESSAGES

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.write(
                message["content"]
            )


    default_question = st.session_state.pop(
        "herb_question",
        ""
    )


    question = st.chat_input(
        "Ask something about herbs..."
    )


    if default_question and not question:

        question = default_question


    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )


        with st.chat_message(
            "user"
        ):

            st.write(
                question
            )


        with st.chat_message(
            "assistant"
        ):

            with st.spinner(
                "Searching herbal knowledge..."
            ):

                try:

                    response = requests.post(
                        f"{API_URL}/ask",
                        json={
                            "question": question
                        },
                        timeout=120
                    )


                    response.raise_for_status()


                    data = response.json()


                    answer = data.get(
                        "answer",
                        "No answer received."
                    )


                    st.write(
                        answer
                    )


                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )


                except requests.exceptions.ConnectionError:

                    st.error(
                        "Could not connect to FastAPI. "
                        "Make sure the API is running."
                    )


                except Exception as error:

                    st.error(
                        f"Error: {error}"
                    )