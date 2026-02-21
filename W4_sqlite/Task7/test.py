import os
from pathlib import Path
from unittest import TestCase
from sqlite3 import Connection, ProgrammingError
import sqlite3
from io import StringIO
import importlib

import main
import db_conn
import product
import menu_product

DBNAME = "dev.db"

PRAGMA_TABLE = [
    (0, 'id', 'INTEGER', 0, None, 1),
    (1, 'manufacturer', 'VARCHAR(255)', 1, None, 0),
    (2, 'brand', 'VARCHAR(255)', 1, None, 0),
    (3, 'cost', 'REAL', 1, None, 0),
    (4, 'price', 'REAL', 1, None, 0)
]

RECORDS = [
    ("FizzWorks", "ColaFusion", 1.5, 3.99),
    ("SoftCarbo", "SparkleSplash", 0.85, 2.35)
]

# def test_program_exit(capsys, monkeypatch):
#     insertions = '0\n'
#     monkeypatch.setattr('sys.stdin', StringIO(insertions))
#     main.Main()
#     expected_out = """Program starting.
# Options:
# 1 - Add product
# 2 - Show products
# 0 - Exit
# Your choice: Program ending."""
#     captured = capsys.readouterr()
#     assert captured.out.rstrip('\n') == expected_out
#     return None

def test_menu_product_askChoice(capsys, monkeypatch):
    insertions = '8\n'
    monkeypatch.setattr('sys.stdin', StringIO(insertions))
    _menu = menu_product.MenuProduct()
    choice = _menu.askChoice()
    expected_out = "Your choice: "
    captured = capsys.readouterr()
    assert choice == 8
    assert captured.out == expected_out
    return None

def test_menu_product_showOptions(capsys, monkeypatch):
    insertions = '\n'
    monkeypatch.setattr('sys.stdin', StringIO(insertions))
    menu_product.MenuProduct().showOptions()
    expected_out = "Options:\n1 - Add product\n2 - Show products\n0 - Exit\n"
    captured = capsys.readouterr()
    assert captured.out == expected_out
    return None

def test_product_create(capsys, monkeypatch):
    insertions = "{}\n{}\n{}\n{}\n".format(*RECORDS[0])
    monkeypatch.setattr('sys.stdin', StringIO(insertions))
    _product = product.Product.createProduct()
    capsys.readouterr()
    assert type(_product.manufacturer) == str, f"manufacturer type is {type(_product.manufacturer)}, but type 'str' was expected."
    assert type(_product.brand) == str, f"brand type is {type(_product.brand)}, but type 'str' was expected."
    assert type(_product.cost) == float, f"cost type is {type(_product.cost)}, but type 'float' was expected."
    assert type(_product.price) == float, f"price type is {type(_product.price)}, but type 'float' was expected."
    return None

class DBTests(TestCase):
    def test_db_existence(self):
        self.assertTrue(os.path.exists(DBNAME), f"'{DBNAME}' doesn't exist. Are you sure you created connection to the correct database?")
        return None
    def test_dbfilepath(self):
        self.assertIsInstance(db_conn.DB_FILEPATH, Path, "Couldn't find DB_FILEPATH object or the object is not instance of pathlib.Path type.")
        return None
    def test_dbconn_type(self):
        self.assertIsInstance(main.DB_CONN, Connection, "Couldn't find DB_CONN object or the object is not instance of sqlite3.Connection type.")
        return None
    def test_product_table(self):
        dbconn = sqlite3.connect(DBNAME)
        cursor = dbconn.cursor()
        cursor.execute(f'PRAGMA table_info("product")')
        table_info = cursor.fetchall()
        self.assertListEqual(PRAGMA_TABLE, table_info, "Are you sure the table 'product' is defined correctly?")
        dbconn.commit()
        cursor.close()
        return None
