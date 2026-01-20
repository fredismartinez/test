from markdown import Markdown


def render_markdown(content: str) -> str:
    engine = Markdown(extensions=["fenced_code", "tables", "toc"])
    return engine.convert(content)
