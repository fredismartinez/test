from app.services.links import extract_links


def test_extract_links_deduplicates_and_sorts() -> None:
    text = """
    Nota con [[Alpha]] y [[Beta]] y [[Alpha ]].
    Otra linea con [[Gamma]].
    """
    assert extract_links(text) == ["Alpha", "Beta", "Gamma"]
