# debug_easymark.py
#! RUN THIS SCRIPT IN PROJECT DIRECTORY TO DIRECTLY TEST OR DEBUG EASYMARK

import sys
import os

# Adds the package root to the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'ezmk')))

from ezmk import load_config#*, mark, bind
from tests import test_mark, test_bind

# Initializes and tests easymark
load_config()

test_mark()

test_bind()

print("XXX: Debug script executed.")
