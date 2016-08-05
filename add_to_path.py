"""
Adds the hacker-scripts base directory to environment variable PATH
"""

import os
from src.initialize import Initialize

initializer = Initialize()


def main():
    """ Checks if the base directory already exists in PATH,
    if not then adds it """
    # The base directory
    BASE_DIRECTORY = initializer.BASE_DIRECTORY
    # PATH environment variable
    PATH = os.environ['PATH']
    if BASE_DIRECTORY not in PATH.split(os.pathsep):
        os.system("setx PATH \"\"")
        os.system("setx PATH \"{0};{1}\"".format(PATH, BASE_DIRECTORY))

if __name__ == "__main__":
    main()
    print("""
            The hacker-scripts has been added to PATH.
            -----
            To view the hacker-scripts commands from your terminal,
            open a new terminal window and type hs-help.
        """)
