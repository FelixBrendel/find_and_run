import os.path
import sys
import subprocess
from pathlib import PurePath


help_string = """
Usage:
    find_and_run <executable> [parameters for the executable]

    This tool  searches for the  specified executable in  the currrent
    working directory and if it is not  found there it will look up to
    20 directories above that. Once the exceutable is found, it is run
    with the specified parameters.
"""

if len(sys.argv) == 1:
    print(sys.argv)
    print(help_string)
    sys.exit(1)

directory = "./"
executable = sys.argv[1]
params = "" if len(sys.argv) == 2 else " ".join(sys.argv[2:])

dirCount = 20

while dirCount > 0:
    if os.path.isfile(directory+executable):
        break

    if directory == "./":
        directory = "../"
    else:
        directory += "../"

    dirCount -= 1
else:
    print(f"The exceutable '{executable}' was not found.")
    sys.exit(2)

# convert to platform specific path string
path = str(PurePath(directory+executable))
executable_return = subprocess.call(path+" "+params)
sys.exit(executable_return)
