#!/usr/bin/env bash
# applies the analytics-code patch
cd ~/sage-git
git apply ../documentation/analytics-code.patch
git apply ../documentation/thebe.patch

