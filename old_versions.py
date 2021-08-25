#!/usr/bin/env python3

import os

# this checks out workspaces at older tags into ./public/
# used by gitlab_ci.py (or other deployment scripts)
# make sure to push those tags to the target repo!
OLD_VERSIONS = [
    '6.6',
    '6.7',
    '6.8',
    "6.9",
    "6.10",
    "7.0",
    "7.1",
    '7.2',
    '7.3',
    '7.4',
    '7.5',
    '7.6',
    '8.0',
    '8.1',
    '8.2',
    '8.3',
    '8.4',
    '8.5',
    '8.6',
    '8.7',
    '8.8',
    '8.9',
    '9.0',
    '9.1',
    '9.2',
    '9.3',
]


def main():
    for ov in OLD_VERSIONS:
        print(f"adding worktree {ov}")
        os.system(f"git worktree add {ov} {ov}")
        print("done")


if __name__ == '__main__':
    main()
