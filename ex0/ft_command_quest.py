import sys

def print_argument() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {(len(sys.argv) - 1)}")
        n = 1
        while n < len(sys.argv):
            print(f"Argument {n}: {sys.argv[n]}")
            n += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    print_argument()
