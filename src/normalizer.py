import unicodedata, pathlib

for path in pathlib.Path("./groundt").glob("*.gt.txt"):
    text = path.read_text(encoding="utf-8")
    norm = unicodedata.normalize("NFC", text)
    path.write_text(norm, encoding="utf-8")
