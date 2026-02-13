from item import Item

class FileHandler:
    #separator defaults to ; and is basically used as csv separator
    def __init__(self, file_path, separator=';'):
        self.__file_path = file_path
        self.__separator  = separator

    def read_file(self) -> list[Item]:
        try:

            with open(self.__file_path, 'r') as file:
                itemList:list[Item] = []
                for line in file:
                    # name, price = line.strip().split(';')
                    # itemList.append(Item(name, float(price)))
                    itemList.append(Item.deserialize(line, self.__separator))

            return itemList
        except Exception as e:
            print(f"There was an error reading the file: {e}")
            return []

    def write_file(self, content: list[Item]):
        with open(self.__file_path, 'w') as file:
            for item in content:
                file.write(Item.serialize(item, self.__separator) + "\n")
                
    def append_to_file(self, content: list[Item]):
        with open(self.__file_path, 'a') as file:
            for item in content:
                file.write(Item.serialize(item, self.__separator) + "\n")
