def flatten_html(html: str) -> str:
    """Strip leading whitespace from every line of an HTML string.

    Streamlit's Markdown renderer treats any line indented 4+ spaces as a
    literal code block. Writing HTML as a nicely-indented multi-line
    f-string (for readability in the .py file) triggers this, so raw tags
    get printed instead of rendered. textwrap.dedent() is NOT enough,
    because it only removes whitespace common to *all* lines — nested
    tags still keep extra indentation relative to their parent, which is
    still 4+ spaces and still triggers the code block.

    Call this on any multi-line HTML string right before passing it to
    st.markdown(..., unsafe_allow_html=True).
    """
    return "\n".join(line.strip() for line in html.strip().splitlines())