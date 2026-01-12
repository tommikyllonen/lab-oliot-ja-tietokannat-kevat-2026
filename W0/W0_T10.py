def main()-> None:
    word: str = input("Insert word: ")
    search_term: str = input("Insert search term: ")
    if (search_term in word):
        print(f"Search term '{search_term}' do appear in word '{word}'")
    else:
        print(f"Search term '{search_term}' doesn't appears in word '{word}'")
    return None

if __name__ == "__main__":
    main()