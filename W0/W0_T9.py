
def main():
    filename = input("Insert filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"### {filename} content ####")
        print(content)
        print(f"\n### {filename} content ####")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()