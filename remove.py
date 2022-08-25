import os
import glob

py_files = glob.glob('./image/*.png')

for py_file in py_files:
    try:
        os.remove(py_file)
    except OSError as e:
        print(f"Error:{ e.strerror}")