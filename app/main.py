import sys


def main():
     while True:
             sys.stdout.write("$ ")
             sys.stdout.flush()
             try:
                     command = input()
             except KeyboardInterrupt:
                     print()
                     continue
             except EOFError:
                     print()
                     break
             if not command.strip():
                     continue
             if command == "exit" or command == "exit 0":
                     break
             elif command == "echo" or command.startswith("echo "):
                     args = command[5:] if command.startswith("echo ") else ""
                     print(args)
             else:
                     print(f"{command}: command not found")


if __name__ == "__main__":
    main()
