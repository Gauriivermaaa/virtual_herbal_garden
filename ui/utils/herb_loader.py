import json
from pathlib import Path
import streamlit as st

# Resolve the project root no matter which folder `streamlit run` was launched from.
# This file lives at: virtual_herbal_garden/ui/utils/herb_loader.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # -> virtual_herbal_garden/
DATA_FILE = BASE_DIR / "data" / "enhanced_herb.json"


@st.cache_data
def load_herbs():

    if not DATA_FILE.exists():
        st.error(
            f"Herb data file not found at: `{DATA_FILE}`\n\n"
            "Create a `data/enhanced_herb.json` file in your project root, "
            "or update `DATA_FILE` in `herb_loader.py` to point at your file."
        )
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        st.error(f"enhanced_herb.json is not valid JSON: {e}")
        return []

    # Supports either a flat list [...] or a wrapper {"herbs": [...]}
    if isinstance(data, dict) and "herbs" in data:
        return data["herbs"]

    return data