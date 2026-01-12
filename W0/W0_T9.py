
def main()-> None:
    filename: str   = input("Insert filename to read: ")
    try:
        with open(filename, 'r') as file:
            content: str = file.read()
        print(f"#### {filename} content ####")
        print(content)
        print(f"#### {filename} content ####")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return None

if __name__ == "__main__":
    main()