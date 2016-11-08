#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

from .base import *

try:
    from .local import *

    live = False
except:
    live = True

if live:
    from .production import *
