import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from py_modules.init import inject_external_modules
inject_external_modules()
