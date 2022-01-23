#!/usr/bin/env python3

import sys;

if sys.version_info.major < 3:
    print("Require python version 3")
    quit()

__import__("roblox-linux-launcher")
