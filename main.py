#! /c/Users/arama/AppData/Local/Microsoft/WindowsApps/python

import sys
import shutil

def main():
    
    builtin = ["echo", "exit"]

    while True:

        sys.stdout.write("$ ")

        user_input = input("")
        command = user_input.split()[0]
        args = user_input.split()[1:]

        if command == "echo":
            sys.stdout.write(str.join(" ", args) + "\n")
        elif command == "type":
            if args in builtin:
                sys.stdout.write(f"{args} is a shell builtin\n")
            elif path := shutil.which(args):
                print(f"{args} is {path}")
        elif command == "exit" and args == "0":
            sys.exit(0)
        else:
            sys.stdout.write(f"{command[0]}: command not found\n")

if __name__ == "__main__":
    main()