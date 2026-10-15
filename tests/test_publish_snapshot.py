import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class PublishSnapshotTests(unittest.TestCase):
    def git(self, root, *args):
        return subprocess.check_output(['git', '-C', str(root), *args], text=True, stderr=subprocess.DEVNULL).strip()

    def test_guard_rejects_outdated_checkout_and_accepts_current_main(self):
        script = ROOT / 'scripts/publish_snapshot.py'
        self.assertTrue(script.is_file(), 'Publication guard must exist')
        with tempfile.TemporaryDirectory() as temporary:
            root = pathlib.Path(temporary)
            remote, first, second = (root / name for name in ['remote.git', 'first', 'second'])
            subprocess.run(['git', 'init', '--bare', str(remote)], check=True, capture_output=True)
            subprocess.run(['git', 'clone', str(remote), str(first)], check=True, capture_output=True)
            self.git(first, 'config', 'user.email', 'test@example.test')
            self.git(first, 'config', 'user.name', 'Test')
            self.git(first, 'checkout', '-b', 'main')
            self.git(first, 'commit', '--allow-empty', '-m', 'initial')
            self.git(first, 'push', 'origin', 'main')
            subprocess.run(['git', 'clone', '--branch', 'main', str(remote), str(second)], check=True, capture_output=True)
            current = self.git(first, 'rev-parse', 'HEAD')
            command = [sys.executable, str(script), '--expected-sha', current]
            self.assertEqual(subprocess.run(command, cwd=first, capture_output=True).returncode, 0)
            self.git(first, 'commit', '--allow-empty', '-m', 'concurrent contributor')
            self.git(first, 'push', 'origin', 'main')
            stale = subprocess.run(command, cwd=second, capture_output=True, text=True)
            self.assertNotEqual(stale.returncode, 0)
            self.assertIn('newer main', stale.stderr)
            self.assertEqual(self.git(second, 'rev-parse', 'HEAD'), current)


if __name__ == '__main__':
    unittest.main()
