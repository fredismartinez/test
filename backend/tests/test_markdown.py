import pytest

pytest.importorskip("markdown")

from app.services.markdown import render_markdown


def test_render_markdown_converts_basic_markup() -> None:
    content = "# Titulo\n\n- Item"
    html = render_markdown(content)
    assert "<h1" in html
    assert "<li>Item</li>" in html
