"""Pruebas del mapa CWE del laboratorio devsecops-pipeline (`cwe-map.json`).

Garantizan que cada defecto plantado en `repo-vulnerable/` está en el mapa, que cada marcador existe de verdad
en su archivo, que los CWE son entradas vigentes del catálogo y que la honestidad del mapa se mantiene:
nada se declara «oficial» sin que la correspondencia sea literal ni se inventa un CWE donde no hay.

    python -m unittest discover -s labs/devsecops-pipeline/tests -v
"""
from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

LAB = Path(__file__).resolve().parents[1]
RAIZ = LAB.parents[1]
MAPA = json.loads((LAB / "cwe-map.json").read_text(encoding="utf-8"))
DEFECTOS = MAPA["defectos"]


class MapaDelLaboratorio(unittest.TestCase):
    def test_los_identificadores_son_unicos(self):
        ids = [d["id"] for d in DEFECTOS]
        self.assertEqual(len(ids), len(set(ids)))

    def test_cada_marcador_existe_en_su_archivo(self):
        for d in DEFECTOS:
            with self.subTest(defecto=d["id"]):
                texto = (LAB / d["archivo"]).read_text(encoding="utf-8")
                self.assertIn(d["marcador"], texto)

    def test_todo_defecto_numerado_de_los_archivos_esta_en_el_mapa(self):
        """Los [DKR-n] del Dockerfile y los [CI-n] del workflow deben estar mapeados (o declarados sin correspondencia)."""
        ids = {d["id"] for d in DEFECTOS}
        dockerfile = (LAB / "repo-vulnerable" / "Dockerfile").read_text(encoding="utf-8")
        workflow = (LAB / "repo-vulnerable" / ".github" / "workflows" / "deploy.yml").read_text(encoding="utf-8")
        for n in re.findall(r"\[(DKR-\d+)\]", dockerfile) + re.findall(r"\[(CI-\d+)\]", workflow):
            self.assertIn(n, ids, f"{n} está plantado pero no mapeado")

    def test_tipo_de_correspondencia_valido_y_coherente_con_los_cwe(self):
        for d in DEFECTOS:
            with self.subTest(defecto=d["id"]):
                self.assertIn(d["correspondencia"], MAPA["tipos_de_correspondencia"])
                if d["correspondencia"] == "ninguna":
                    self.assertEqual(d["cwe"], [], "«ninguna» no puede llevar CWE")
                else:
                    self.assertTrue(d["cwe"], "una correspondencia sin CWE es «ninguna»")
                self.assertTrue(d["motivo"].strip())
                self.assertTrue(d["correccion"].strip())

    def test_la_mayoria_de_las_correspondencias_inferidas_declaran_su_limite(self):
        """Una correspondencia «inferida» debe decir por qué no es oficial (que la ficha no cubre el caso)."""
        for d in DEFECTOS:
            if d["correspondencia"] == "inferida":
                with self.subTest(defecto=d["id"]):
                    self.assertRegex(d["motivo"].lower(), r"(ficha|catálogo|aunque|no (menciona|habla|tiene|cita))")

    def test_hay_defectos_de_los_tres_tipos(self):
        tipos = {d["correspondencia"] for d in DEFECTOS}
        self.assertEqual(tipos, {"oficial", "inferida", "ninguna"})

    def test_los_cwe_existen_y_estan_vigentes_en_el_catalogo_local(self):
        sys.path.insert(0, str(RAIZ / "scripts"))
        import cwe_lib as L
        if not (L.NORMALIZADO / "cwe.jsonl").is_file():
            self.skipTest("base CWE no importada")
        base = L.BaseCWE.cargar()
        for d in DEFECTOS:
            for cid in d["cwe"]:
                with self.subTest(defecto=d["id"], cwe=cid):
                    self.assertIn(cid, base)
                    e = base.obtener(cid)
                    self.assertNotEqual(e["estado"], "Deprecated")
                    self.assertEqual(e["tipo"], "weakness")
                    self.assertNotIn(e["notas_mapeo"].get("uso"), ("Prohibited", "Discouraged"),
                                     f"{cid} no es adecuado para clasificar un defecto concreto")


if __name__ == "__main__":
    unittest.main()
