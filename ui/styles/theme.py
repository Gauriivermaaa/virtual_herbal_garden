import streamlit as st


def apply_theme():
    """Injects the 'Botanical Apothecary' visual identity for the app."""

    st.markdown(
        """
        <style>

        @import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,500&family=Work+Sans:wght@400;500;600;700&display=swap');

        :root {
            --ink: #16241C;
            --forest: #24382C;
            --forest-light: #2E4636;
            --paper: #F1ECDD;
            --paper-dim: #E8E1CC;
            --moss: #6B8F71;
            --turmeric: #C98A2B;
            --turmeric-dark: #A6721F;
            --cream: #F6F1E4;
            --ink-text: #20301F;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background-color: var(--ink);
            background-image: radial-gradient(circle at 15% 0%, #1C2E22 0%, var(--ink) 55%);
            color: var(--cream);
            font-family: 'Work Sans', sans-serif;
        }

        [data-testid="stHeader"] { background-color: transparent; }

        [data-testid="stAppViewContainer"] .main .block-container {
            padding-top: 2.2rem;
            padding-bottom: 3rem;
            max-width: 1180px;
        }

        h1, h2, h3, .hero-title {
            font-family: 'Fraunces', serif;
            color: var(--cream);
            letter-spacing: 0.2px;
        }

        h1 {
            font-weight: 600;
            font-size: 2.3rem;
            border-bottom: 1px solid rgba(246, 241, 228, 0.15);
            padding-bottom: 0.6rem;
            margin-bottom: 1.2rem;
        }

        p, span, label, .stMarkdown, .stCaption { color: var(--cream); }
        em { color: var(--moss); }

        /* ---------- Sidebar ---------- */

        [data-testid="stSidebar"] {
            background-color: var(--forest);
            border-right: 1px solid rgba(246, 241, 228, 0.08);
        }
        [data-testid="stSidebar"] * { color: var(--cream) !important; }

        .sidebar-logo {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            padding: 0.4rem 0 1rem 0;
        }
        .sidebar-logo-icon {
            font-size: 1.8rem;
            background: linear-gradient(135deg, var(--turmeric), var(--moss));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .sidebar-badge {
            display: inline-block;
            font-size: 0.7rem;
            background-color: rgba(201, 138, 43, 0.18);
            color: var(--turmeric) !important;
            border: 1px solid rgba(201, 138, 43, 0.4);
            border-radius: 20px;
            padding: 0.1rem 0.6rem;
            margin-left: 0.3rem;
        }

        /* ---------- Buttons ---------- */

        .stButton > button {
            background-color: var(--turmeric);
            color: var(--ink);
            border: none;
            border-radius: 6px;
            font-weight: 600;
            padding: 0.55rem 1.1rem;
            transition: all 0.18s ease;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
        }
        .stButton > button:hover {
            background-color: var(--turmeric-dark);
            color: var(--cream);
            transform: translateY(-1px);
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
        }
        .stButton > button:focus-visible {
            outline: 2px solid var(--moss);
            outline-offset: 2px;
        }

        .stButton > button[kind="secondary"] {
            background-color: transparent;
            color: var(--cream);
            border: 1px solid rgba(246, 241, 228, 0.25);
            box-shadow: none;
        }
        .stButton > button[kind="secondary"]:hover {
            background-color: rgba(201, 138, 43, 0.15);
            color: var(--turmeric);
            border-color: var(--turmeric);
        }
        .stButton > button[kind="primary"] {
            background-color: var(--turmeric);
            color: var(--ink);
        }

        /* ---------- Inputs ---------- */

        .stTextInput input, .stTextArea textarea {
            background-color: var(--paper);
            color: var(--ink-text);
            border: 1px solid var(--moss);
            border-radius: 6px;
        }
        .stTextInput input::placeholder { color: #6b6551; }

        /* ---------- Hero banner (home + herb detail) ---------- */

        .hero-banner {
            background: linear-gradient(120deg, var(--forest) 0%, var(--forest-light) 60%, #3A5A43 100%);
            border-radius: 10px;
            padding: 2.2rem 2.4rem;
            margin-bottom: 1.6rem;
            border: 1px solid rgba(201, 138, 43, 0.25);
            position: relative;
            overflow: hidden;
        }
        .hero-banner::after {
            content: "";
            position: absolute;
            right: -40px; top: -40px;
            width: 180px; height: 180px;
            background: radial-gradient(circle, rgba(201,138,43,0.25) 0%, transparent 70%);
        }
        .hero-title {
            font-size: 2rem;
            font-weight: 600;
            margin: 0 0 0.4rem 0;
        }
        .hero-subtitle {
            font-size: 1rem;
            color: var(--paper-dim);
            max-width: 560px;
            margin: 0;
        }

        /* ---------- Stat chips ---------- */

        .stat-chip {
            background-color: var(--forest);
            border: 1px solid rgba(201, 138, 43, 0.3);
            border-radius: 8px;
            padding: 0.9rem 1rem;
            text-align: center;
        }
        .stat-number {
            font-family: 'Fraunces', serif;
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--turmeric);
            display: block;
        }
        .stat-label {
            font-size: 0.78rem;
            color: var(--paper-dim);
            text-transform: uppercase;
            letter-spacing: 0.6px;
        }

        /* ---------- Herb specimen card ---------- */

        .herb-card {
            background-color: var(--paper);
            color: var(--ink-text);
            border: 1px solid var(--paper-dim);
            border-top: 3px solid var(--moss);
            border-radius: 6px;
            padding: 1.3rem 1.4rem 1.1rem 1.4rem;
            margin-bottom: 0.7rem;
            min-height: 210px;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }
        .herb-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.35);
            border-top-color: var(--turmeric);
        }
        .herb-name {
            font-family: 'Fraunces', serif;
            font-size: 1.25rem;
            font-weight: 600;
            margin-bottom: 0.7rem;
            color: var(--ink-text);
        }
        .herb-info p { margin-bottom: 0.65rem; line-height: 1.45; color: var(--ink-text); }
        .herb-info strong {
            font-family: 'Fraunces', serif;
            font-weight: 600;
            font-size: 0.82rem;
            color: var(--turmeric-dark);
        }
        .herb-info em { color: var(--ink-text); font-style: italic; }

        .herb-tag {
            display: inline-block;
            background-color: rgba(107, 143, 113, 0.15);
            color: var(--moss);
            border: 1px solid var(--moss);
            border-radius: 20px;
            padding: 0.1rem 0.7rem;
            font-size: 0.72rem;
            margin-top: 0.3rem;
        }

        /* ---------- Property pill (herb detail) ---------- */

        .property-pill {
            display: inline-block;
            background-color: var(--forest);
            color: var(--cream);
            border: 1px solid var(--moss);
            border-radius: 20px;
            padding: 0.35rem 1rem;
            margin: 0 0.4rem 0.5rem 0;
            font-size: 0.85rem;
            transition: transform 0.15s ease;
        }
        .property-pill:hover { transform: translateY(-2px); }
        .property-pill strong { color: var(--turmeric); }

        /* ---------- Home feature cards ---------- */

        .feature-card {
            background-color: var(--paper);
            color: var(--ink-text);
            border-radius: 6px;
            border-left: 4px solid var(--turmeric);
            padding: 1.6rem 1.5rem;
            min-height: 220px;
            margin-bottom: 0.8rem;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }
        .feature-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.3);
        }
        .feature-icon { font-size: 1.8rem; margin-bottom: 0.5rem; }
        .feature-title {
            font-family: 'Fraunces', serif;
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 0.5rem;
            color: var(--ink-text);
        }
        .feature-text { font-size: 0.92rem; line-height: 1.5; color: #45412f; }

        /* ---------- Info card (herb detail - basic info) ---------- */

        .info-card {
            background-color: var(--paper);
            color: var(--ink-text);
            border-radius: 6px;
            border-left: 4px solid var(--moss);
            padding: 1.6rem 1.7rem;
            min-height: 240px;
        }
        .info-card .section-title {
            font-family: 'Fraunces', serif;
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--ink-text);
        }
        .info-card p { margin-bottom: 0.7rem; line-height: 1.5; color: var(--ink-text); }
        .info-card strong {
            font-family: 'Fraunces', serif;
            font-weight: 600;
            font-size: 0.82rem;
            color: var(--turmeric-dark);
        }

        /* ---------- Properties panel (herb detail - ayurvedic) ---------- */

        .properties-panel {
            background-color: var(--forest);
            border: 1px solid rgba(201, 138, 43, 0.25);
            border-radius: 6px;
            padding: 1.6rem 1.7rem;
            min-height: 240px;
        }
        .properties-panel .section-title {
            font-family: 'Fraunces', serif;
            font-size: 1.15rem;
            font-weight: 600;
            margin-bottom: 1rem;
            color: var(--cream);
        }

        /* ---------- Login card ---------- */

        [data-testid="stVerticalBlockBorderWrapper"] {
            background-color: var(--forest);
            border-radius: 10px;
            border: 1px solid rgba(201, 138, 43, 0.2);
        }

        /* ---------- File uploader ---------- */

        [data-testid="stFileUploader"] section {
            background-color: var(--forest);
            border: 1px dashed var(--moss);
            border-radius: 6px;
        }

        /* ---------- Footer ---------- */

        .app-footer {
            text-align: center;
            color: rgba(246, 241, 228, 0.4);
            font-size: 0.8rem;
            margin-top: 3rem;
            padding-top: 1.2rem;
            border-top: 1px solid rgba(246, 241, 228, 0.08);
        }

        hr { border-color: rgba(246, 241, 228, 0.15); }

        </style>
        """,
        unsafe_allow_html=True,
    )