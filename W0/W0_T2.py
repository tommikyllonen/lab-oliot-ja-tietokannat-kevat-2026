def main():
    print("Per Miller's Law, humans can retain ~7 items in short-term memory.")
    memorable_string = input("Insert memorable string:")
    if len(memorable_string) <= 7:
        print("This string will be easy to remember.")
    else:
        print("This string will be hard to remember.")


if __name__ == "__main__":
    main()