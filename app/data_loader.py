import markdown
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_markdown(file_path):
    full_path = BASE_DIR / file_path

    if not full_path.exists():
        return "<p>Content not found.</p>"

    with open(full_path, "r", encoding="utf-8") as f:
        text = f.read()

    return markdown.markdown(text)
