import tempfile
import unittest
from pathlib import Path

from scripts import generar_glosario_global as glossary


CLASS = """# Clase 001 — Prueba UTF-8

## 📔 Glosario operativo

| Término | Definición |
|---|---|
| CTF | Competición con una flag. |
| Capture The Flag | Competición con una flag. |
| SIEM | Correlación y búsqueda. |

## 🔗 Referencias

Fin.
"""


class GlossaryTests(unittest.TestCase):
    def test_valid_table_and_utf8(self):
        rows = glossary.parse_glossary_table(
            "| Término | Definición concisa |\n|---|---|\n| Señal | Evidencia útil. |"
        )
        self.assertEqual(rows, [("Señal", "Evidencia útil.")])

    def test_non_glossary_table_is_ignored(self):
        rows = glossary.parse_glossary_table("| Herramienta | Uso |\n|---|---|\n| rg | Buscar |")
        self.assertEqual(rows, [])

    def test_aliases_and_acronyms_are_normalized(self):
        self.assertEqual(glossary.canonical_name("CTF"), "CTF — Capture The Flag")
        self.assertEqual(glossary.canonical_name("Capture The Flag"), "CTF — Capture The Flag")
        self.assertEqual(glossary.canonical_name("  ingeniería INVERSA "), "Reversing")

    def test_duplicates_merge_and_links_are_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            class_dir = root / "parte-0-prueba" / "001-prueba"
            class_dir.mkdir(parents=True)
            (class_dir / "README.md").write_text(
                CLASS.replace("Competición con una flag.", "Consulta [CTFd](https://ctfd.io/)."),
                encoding="utf-8",
            )
            old_root = glossary.ROOT
            try:
                glossary.ROOT = root
                entries, scanned = glossary.collect(root)
            finally:
                glossary.ROOT = old_root
            entry = entries[glossary.normalize("CTF — Capture The Flag")]
            self.assertEqual(scanned, 1)
            self.assertEqual(len(entry.classes), 1)
            self.assertIn("[CTFd](https://ctfd.io/)", glossary.best(entry.definitions))

    def test_sorting_and_render_are_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            class_dir = root / "parte-0-prueba" / "001-prueba"
            class_dir.mkdir(parents=True)
            (class_dir / "README.md").write_text(CLASS, encoding="utf-8")
            old_root = glossary.ROOT
            try:
                glossary.ROOT = root
                first = glossary.render(*glossary.collect(root))
                second = glossary.render(*glossary.collect(root))
            finally:
                glossary.ROOT = old_root
            self.assertEqual(first, second)
            self.assertLess(first.index("\n## A\n"), first.index("\n## C\n"))


if __name__ == "__main__":
    unittest.main()
