#!/usr/bin/python3

import os, sys
userid=os.getuid
os.chown("/Applications/Slack.app", {userid}, -1)


