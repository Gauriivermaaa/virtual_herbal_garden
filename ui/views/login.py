import streamlit as st

from auth import create_user, verify_user


def login_page():

    st.write("")
    st.write("")

    left_col, center_col, right_col = st.columns(
        [1.3, 2, 1.3]
    )

    with center_col:

        with st.container(border=True):

            icon_left, icon_center, icon_right = st.columns(
                [1, 1, 1]
            )

            with icon_center:
                st.markdown(
                    "## 🌿"
                )

            st.markdown(
                "## Virtual Herbal Garden"
            )

            st.caption(
                "Welcome back! Sign in to explore the world "
                "of medicinal herbs."
            )

            st.write("")

            tab_signin, tab_signup = st.tabs(["Sign In", "Sign Up"])

            # ---------------- SIGN IN ----------------
            with tab_signin:

                signin_email = st.text_input(
                    "Email",
                    placeholder="Enter your email",
                    key="signin_email",
                )

                signin_password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Enter your password",
                    key="signin_password",
                )

                st.write("")

                if st.button(
                    "Login 🌿",
                    use_container_width=True,
                    key="signin_button",
                ):

                    if not signin_email or not signin_password:
                        st.error("Please enter email and password.")
                    else:
                        success, message = verify_user(signin_email, signin_password)

                        if success:
                            st.session_state.logged_in = True
                            st.session_state.user_email = signin_email.lower().strip()
                            st.session_state.page = "Home"
                            st.rerun()
                        else:
                            st.error(message)

            # ---------------- SIGN UP ----------------
            with tab_signup:

                signup_email = st.text_input(
                    "Email",
                    placeholder="Enter your email",
                    key="signup_email",
                )

                signup_password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Create a password",
                    key="signup_password",
                )

                signup_confirm = st.text_input(
                    "Confirm Password",
                    type="password",
                    placeholder="Re-enter your password",
                    key="signup_confirm",
                )

                st.write("")

                if st.button(
                    "Create Account 🌱",
                    use_container_width=True,
                    key="signup_button",
                ):

                    if not signup_email or not signup_password or not signup_confirm:
                        st.error("Please fill in all fields.")
                    elif signup_password != signup_confirm:
                        st.error("Passwords do not match.")
                    else:
                        success, message = create_user(signup_email, signup_password)

                        if success:
                            # Auto-login after signup
                            st.session_state.logged_in = True
                            st.session_state.user_email = signup_email.lower().strip()
                            st.session_state.page = "Home"
                            st.rerun()
                        else:
                            st.error(message)