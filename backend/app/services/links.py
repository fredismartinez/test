import re

LINK_PATTERN = re.compile(r"\[\[([^\]]+)\]\]")


def extract_links(markdown_text: str) -> list[str]:
    return sorted({match.strip() for match in LINK_PATTERN.findall(markdown_text)})
