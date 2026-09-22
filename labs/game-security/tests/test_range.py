import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from game_security.core import Vec3, angle_degrees, in_fov, predict_intercept, world_to_screen
from game_security.datasets import generate, write_csv
from game_security.detection import DetectionEngine
from game_security.server import GameServer, Mode, PlayerCommand


class VectorTests(unittest.TestCase):
    def test_normalization_and_angle(self):
        self.assertAlmostEqual(Vec3(3, 4, 0).normalized().length(), 1.0)
        self.assertAlmostEqual(angle_degrees(Vec3(1, 0, 0), Vec3(0, 1, 0)), 90.0)
        self.assertTrue(in_fov(Vec3(1, 0, 0), Vec3(1, 0.1, 0), 30))

    def test_zero_vector_is_rejected(self):
        with self.assertRaises(ValueError):
            Vec3(0, 0, 0).normalized()

    def test_prediction_and_projection(self):
        point = predict_intercept(Vec3(0, 0, 0), Vec3(10, 0, 0), Vec3(0, 2, 0), 10)
        self.assertEqual(point, Vec3(10, 2, 0))
        identity = ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1))
        screen = world_to_screen(Vec3(0, 0, 0), identity, 1920, 1080)
        self.assertAlmostEqual(screen.x, 960)
        self.assertAlmostEqual(screen.y, 540)


class AuthorityTests(unittest.TestCase):
    def test_secure_server_rejects_impossible_state(self):
        server = GameServer(Mode.SECURE)
        decision = server.apply(PlayerCommand(1000, 1, position=Vec3(500, 0, 0), claimed_health=999))
        self.assertFalse(decision.accepted)
        self.assertIn("impossible_speed", decision.reasons)
        self.assertEqual(server.state.health, 100)

    def test_vulnerable_server_demonstrates_wrong_trust(self):
        server = GameServer(Mode.VULNERABLE)
        decision = server.apply(PlayerCommand(1000, 1, claimed_health=999, claimed_ammo=999))
        self.assertTrue(decision.accepted)
        self.assertEqual(server.state.health, 999)
        self.assertEqual(server.state.ammo, 999)

    def test_replay_and_fire_rate(self):
        server = GameServer(Mode.SECURE)
        self.assertTrue(server.apply(PlayerCommand(1000, 1, fire=True)).accepted)
        decision = server.apply(PlayerCommand(1050, 1, fire=True))
        self.assertFalse(decision.accepted)
        self.assertEqual(set(decision.reasons), {"sequence_replay", "fire_rate_violation"})


class DetectionAndDatasetTests(unittest.TestCase):
    def test_alert_explains_signal(self):
        alerts = DetectionEngine().evaluate({"speed": 14, "shot_interval_ms": 50, "aim_delta_degrees": 40, "reaction_ms": 42})
        self.assertEqual({a.rule for a in alerts}, {"impossible_speed", "fire_rate", "snap_aim_candidate"})
        self.assertTrue(all(a.evidence and a.legitimate_explanations for a in alerts))

    def test_dataset_is_reproducible_and_writable(self):
        self.assertEqual(generate("normal", 5, 7), generate("normal", 5, 7))
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.csv"
            write_csv(path, "snap-aim", 3, 7)
            self.assertEqual(len(path.read_text(encoding="utf-8").splitlines()), 4)


if __name__ == "__main__":
    unittest.main()
