# pure data class ot represent an item in the shopping cart
# containing nothing but the name and price of the item

from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float

    @staticmethod
    def deserialize(item_string: str, separator: str) -> 'Item':
        name, price = item_string.strip().split(separator)
        return Item(name, float(price))
        
    @staticmethod
    def serialize(item: 'Item', separator: str) -> str:
        # strItem =  f"{item.name}{separator}{item.price}" #OR LIKE THIS:
        strItem = separator.join([item.name, str(item.price)])
        return strItem
