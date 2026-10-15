#!/usr/bin/env python3
"""Reject publication when a checkout has been superseded on main."""
import argparse
import subprocess
import sys


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expected-sha', required=True)
    args = parser.parse_args(argv)
    try:
        head = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
        remote = subprocess.check_output(['git', 'ls-remote', 'origin', 'refs/heads/main'], text=True).split()
        if head != args.expected_sha or not remote or remote[0] != args.expected_sha:
            print('Publication stopped: a newer main or a different checkout exists.', file=sys.stderr)
            return 1
        print('Publication snapshot matches current main.')
        return 0
    except subprocess.SubprocessError:
        print('Publication stopped: unable to verify current main.', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
