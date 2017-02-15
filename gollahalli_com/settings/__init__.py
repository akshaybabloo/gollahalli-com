#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli
"""
This file checks if `local.py` is present or not, if its present `local.py` is used else `production.py` is used to load the database and static assets.
"""

from .base import *

try:
    from .local import *

    live = False
except:
    live = True

if live:
    from .production import *
