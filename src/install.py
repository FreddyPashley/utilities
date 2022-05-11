"""
WARNING:
If you run this program, it will move the main 'utilities.py' file into your local library.
Do not run this if you are developing. Only to be used at user-level.
"""

import os
from shutil import move

original = os.getcwd()
dir = "\\".join(i for i in str(os).split("from ")[-1].replace("'","").replace(">","").split("\\")[:-2])
try:
	move(original+"/utilities.py", dir)
	print("Sucessfully installed the module.\nYou can close this window and use 'import utilities' in any program on this computer.")
except Exception:
	print("There was an error when installing the module.\nYou can try manually by moving 'utilities.py' into your Python Lib directory, in AppData Local.")
while True: pass