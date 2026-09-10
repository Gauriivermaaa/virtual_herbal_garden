def _flatten_value(value):
    """Convert any JSON value (list, dict, scalar) into a readable string."""

    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, dict):
                parts.append(_flatten_dict_to_text(item))
            else:
                parts.append(str(item))
        return ", ".join(p for p in parts if p)

    if isinstance(value, dict):
        return _flatten_dict_to_text(value)

    return str(value)


def _flatten_dict_to_text(record):
    """Turn any flat/nested dict into 'Key: value. Key: value.' text,
    skipping empty values. Works regardless of what keys exist."""

    parts = []

    for key, value in record.items():

        if value is None or value == "" or value == []:
            continue

        label = str(key).replace("_", " ").strip().capitalize()
        text_value = _flatten_value(value)

        if text_value:
            parts.append(f"{label}: {text_value}.")

    return " ".join(parts)


def _guess_name(record, index):
    """Try common name-like keys; fall back to a generic label."""

    for key in ("name", "herb_name", "plant_name", "title", "botanical_name"):
        value = record.get(key)
        if value:
            return str(value).strip()

    return f"item_{index}"


def _guess_link(record):
    for key in ("imppat_url", "url", "link", "source"):
        value = record.get(key)
        if value:
            return str(value)
    return ""


def make_chunks(data):
    """
    Accepts ANY JSON structure a user uploads:
      - a list of objects (each becomes one or more chunks)
      - a single object (wrapped into a list of one)
      - nested list fields inside a record (e.g. therapeutic_uses) become
        their own sub-chunks automatically, using whatever keys they contain

    Falls back gracefully — malformed or oddly-shaped items are skipped
    instead of crashing the whole upload.
    """

    chunks = []

    # Normalize input into a list of dict records
    if isinstance(data, dict):
        records = [data]
    elif isinstance(data, list):
        records = data
    else:
        print("Unsupported JSON structure: expected an object or a list of objects.")
        return chunks

    for index, record in enumerate(records):

        if not isinstance(record, dict):
            # Skip malformed entries instead of crashing
            continue

        name = _guess_name(record, index)
        link = _guess_link(record)

        # Separate out any list-of-dicts fields (like therapeutic_uses)
        # so each nested record becomes its own focused chunk.
        nested_list_fields = {}
        flat_record = {}

        for key, value in record.items():
            if isinstance(value, list) and value and all(isinstance(v, dict) for v in value):
                nested_list_fields[key] = value
            else:
                flat_record[key] = value

        # --------------------------------------------------
        # MAIN / BASIC CHUNK (from all flat fields)
        # --------------------------------------------------

        basic_text = _flatten_dict_to_text(flat_record)

        if basic_text:
            chunks.append({
                "id": f"{name}_basic_{index}",
                "name": name,
                "link": link,
                "text": basic_text,
            })

        # --------------------------------------------------
        # SUB-CHUNKS for nested list fields (e.g. therapeutic_uses)
        # --------------------------------------------------

        for field_name, sub_records in nested_list_fields.items():

            for sub_index, sub_record in enumerate(sub_records):

                sub_text = _flatten_dict_to_text(sub_record)

                if not sub_text:
                    continue

                full_text = f"{name}. {sub_text}"

                chunks.append({
                    "id": f"{name}_{field_name}_{index}_{sub_index}",
                    "name": name,
                    "link": link,
                    "text": full_text,
                })

    print(f"Created {len(chunks)} chunks from {len(records)} record(s)")

    return chunks


if __name__ == "__main__":

    import json

    with open(
        "data/enhanced_herb.json",
        "r",
        encoding="utf-8"
    ) as f:

        plants = json.load(f)

    chunks = make_chunks(plants)

    print(f"\nTotal chunks: {len(chunks)}")

    if chunks:

        print("\nFIRST CHUNK:\n")
        print(chunks[0]["text"])

        print("\nSECOND CHUNK:\n")
        print(chunks[1]["text"])