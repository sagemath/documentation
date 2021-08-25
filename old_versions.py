#!/usr/bin/env python3

import os

# created by the CI script, to checkout workspaces at older tags
# make sure to push those tags to the target repo!
OLD_VERSIONS = [
    #'6.7',
    #'6.8',
    #'8.8',
    #'8.9',
    #'9.0',
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
