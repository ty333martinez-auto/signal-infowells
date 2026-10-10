import json
import tempfile
import unittest
from pathlib import Path

from src.signal_infowells.capcut_intent import (
    build_capcut_intent,
    requires_capcut_intent,
    write_pmcr_task,
)


class CapCutIntentTests(unittest.TestCase):
    def test_detects_explicit_video_work(self):
        self.assertTrue(requires_capcut_intent("Create a CapCut reel prompt"))
        self.assertTrue(requires_capcut_intent("unrelated wording", "video_editing"))

    def test_does_not_emit_for_unrelated_task(self):
        self.assertFalse(requires_capcut_intent("Review reasoning framework invariants"))

    def test_unknowns_are_preserved_not_invented(self):
        record = build_capcut_intent({"task_id": "test-reel", "objective": "Create a reel"})
        self.assertIsNone(record["intent"]["platform"])
        self.assertIsNone(record["intent"]["audience"])
        self.assertTrue(record["unresolved_questions"])
        self.assertEqual(record["status"], "NOT-YET-VERIFIED")
        self.assertIn("UNKNOWN", record["portable_prompt"])

    def test_pmcr_task_is_written_and_portable(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = write_pmcr_task({
                "task_id": "launch-reel-001",
                "objective": "Create a short product reel",
                "platform": "Facebook Reels",
                "aspect_ratio": "9:16",
                "target_duration_seconds": 20,
                "source_assets": [{"path": "assets/clip.mp4", "role": "primary footage"}],
            }, tmp)
            self.assertEqual(path.relative_to(tmp).as_posix(),
                             ".pmcro/tasks/capcut/launch-reel-001.json")
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["task_type"], "capcut_intent")
            self.assertIn("Create/edit the video", data["portable_prompt"])
            with self.assertRaises(FileExistsError):
                write_pmcr_task({"task_id": "launch-reel-001", "objective": "Create a reel"}, tmp)

    def test_requires_objective(self):
        with self.assertRaises(ValueError):
            build_capcut_intent({})


if __name__ == "__main__":
    unittest.main()
