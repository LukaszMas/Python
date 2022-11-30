#!/usr/bin/env python3

"""
This script will rename all files with given extension recursively
"""

# --- Standard Library --------------------------------------------------------

import os
import sys
import argparse

# --- Main function -----------------------------------------------------------

def main(args: argparse.Namespace):
    """Renames files in current directory recursively"""

    cwd = os.path.abspath(args.workdir);
    print(f'Going to rename files in {cwd}')
    confirm_operation()

    # Execute renameing operation
    recursive_rename(cwd, args)

# --- Helpers -----------------------------------------------------------------

def confirm_operation() -> int:
    """Confirm operation."""
    confirm = input("[y]Confirm or other key to cancel: ")
    if confirm.lower() != 'y':
        abort(f"Pressed \"{confirm}\".")
    return confirm

def recursive_rename(cwd: str, args: argparse.Namespace):
    for (root, dirs, files) in os.walk(cwd, topdown=True):
        #dirs.clear() #with topdown true, this will prevent walk from going into subs
        for f in files:
            if f.endswith(args.ext):
                name, ext = os.path.splitext(f)
                if args.place == "prefix":
                    new_name = args.text + name + ext
                else:
                    new_name = name + args.text + ext
                # debug log
                print(f.rjust(35) + ' => renamed to => ' + new_name.ljust(35))
                os.rename(f, new_name)

def abort(reason: str, return_code: int = 1):
    """Abort execution and print reason."""
    print(reason + " Exiting." + '\n')
    sys.exit(return_code)

# --- init --------------------------------------------------------------------

if __name__ == "__main__":
    P = argparse.ArgumentParser(description=("Rename all files of given extension"))
    P.add_argument("-d", "--workdir", type=str, metavar='', default=".",
                   help="Work directory to be used for recursive rename operation.")
    P.add_argument("-x", "--ext", type=str, metavar='', required=True,
                   help="Extension of files to be renamed recursively.")
    P.add_argument("-t", "--text", type=str, metavar='', required=True,
                   help="Text to be added.")
    P.add_argument("-p", "--place", type=str, metavar='', default="suffix",
                   choices=["prefix", "suffix"], help="Place to add the text.")
    main(P.parse_args())
