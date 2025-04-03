import sys


def main():
    
    while True:

        sys.stdout.write("$ ")

        command = input("").split(" ")

        if command[0] == "echo":
            sys.stdout.write(str.join(" ", command[1:]) + "\n")
        elif command[0] == "exit" and command[1] == "0":
            sys.exit(0)
        else:
            sys.stdout.write(f"{command[0]}: command not found")

if __name__ == "__main__":
    main()