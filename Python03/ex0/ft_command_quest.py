import sys


def ft_command_quest() -> None:
    print("Program name: ", sys.argv[0])
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        print("Arguments recieved: ", len(sys.argv) - 1)
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: ", sys.argv[i])
        print("Total arguments: ", len(sys.argv))


if __name__ == "__main__":
    print("=== Command Quest ===")

    ft_command_quest()
