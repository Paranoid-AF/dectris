import sys
import os

# A hack to assign installed modules' path
def inject_external_modules():
    exec_path = os.path.dirname(os.path.realpath(__file__))
    modules_path = os.path.join(exec_path, "externals")
    sys.path.insert(1, modules_path)
