def multiply(*args):
    """Multiply any number of inputs together."""
    result = 1
    for num in args:
        result *= num
    return result


def main():
    print("Hello from interactive-coding-sessions-2!")


if __name__ == "__main__":
    main()
